import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

# output 폴더 관리를 위한 임포트
from output_manager import setup_output_dirs, get_crawl_filename

class QnACrawler:
    def __init__(self, headless=True):
        """
        Q&A 크롤러 초기화
        
        Args:
            headless (bool): 헤드리스 모드로 실행할지 여부
        """
        self.setup_driver(headless)
        self.base_url = "https://b-flow.co.kr/p-posts/qna#/"
        self.qna_data = []
        
    def setup_driver(self, headless):
        """Chrome 드라이버 설정"""
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def debug_pagination(self):
        """페이지네이션 상태 자세히 확인"""
        try:
            print("\n=== 페이지네이션 디버깅 ===")
            
            # 1. 현재 URL 확인
            current_url = self.driver.current_url
            print(f"현재 URL: {current_url}")
            
            # 2. 페이지네이션 HTML 구조 출력
            pagination = self.driver.find_element(By.CSS_SELECTOR, "ul.pagination")
            pagination_html = pagination.get_attribute("outerHTML")
            print(f"페이지네이션 HTML:")
            print(pagination_html[:500] + "...")
            
            # 3. 모든 페이지 링크 상태 확인
            all_links = pagination.find_elements(By.TAG_NAME, "a")
            print(f"\n모든 링크 정보:")
            for i, link in enumerate(all_links):
                parent_li = link.find_element(By.XPATH, "..")
                li_class = parent_li.get_attribute("class")
                link_text = link.text.strip()
                href = link.get_attribute("href")
                print(f"  [{i}] 텍스트: '{link_text}', class: '{li_class}', href: '{href}'")
            
            # 4. 현재 활성 페이지 확인
            try:
                active_link = pagination.find_element(By.CSS_SELECTOR, "li.active a, .active a")
                active_text = active_link.text.strip()
                active_parent_class = active_link.find_element(By.XPATH, "..").get_attribute("class")
                print(f"\n활성 페이지: '{active_text}', class: '{active_parent_class}'")
            except NoSuchElementException:
                print("\n활성 페이지를 찾을 수 없습니다!")
            
            # 5. JavaScript로 페이지 상태 확인
            js_check = """
            const pagination = document.querySelector('ul.pagination');
            const activeItem = pagination.querySelector('li.active, li.page-item.active');
            const result = {
                activePage: activeItem ? activeItem.textContent.trim() : 'not found',
                allPageTexts: Array.from(pagination.querySelectorAll('a')).map(a => a.textContent.trim()),
                paginationClasses: pagination.className
            };
            return result;
            """
            
            js_result = self.driver.execute_script(js_check)
            print(f"\nJavaScript 체크 결과:")
            print(f"  활성 페이지: {js_result['activePage']}")
            print(f"  모든 페이지: {js_result['allPageTexts']}")
            print(f"  페이지네이션 클래스: {js_result['paginationClasses']}")
            
            print("=== 디버깅 완료 ===\n")
            
        except Exception as e:
            print(f"디버깅 중 오류: {e}")

    def get_current_page(self):
        """현재 활성 페이지 번호 반환 - 최적화된 버전"""
        try:
            # active 클래스를 가진 페이지 찾기
            active_element = self.driver.find_element(
                By.CSS_SELECTOR, 
                "li.page-item.pagination-page-nav.active a.page-link"
            )
            current_page = int(active_element.text.strip())
            return current_page
            
        except (NoSuchElementException, ValueError) as e:
            print(f"    현재 페이지 확인 실패: {e}")
            return 1

    def get_visible_pages(self, pagination):
        """현재 보이는 페이지 번호들 반환 - 최적화"""
        visible_pages = []
        try:
            page_links = pagination.find_elements(
                By.CSS_SELECTOR, 
                "li.page-item.pagination-page-nav a.page-link"
            )
            
            for link in page_links:
                page_text = link.text.strip()
                if page_text != "..." and page_text.isdigit():
                    visible_pages.append(int(page_text))
            
            return sorted(visible_pages)
            
        except Exception as e:
            print(f"    보이는 페이지 확인 중 오류: {e}")
            return []

    def wait_for_active_page_change(self, target_page, max_attempts=100):
        """active 클래스가 목표 페이지로 바뀔 때까지 대기"""
        print(f"    활성 페이지가 {target_page}로 바뀔 때까지 대기 중...")
        
        for attempt in range(max_attempts):
            try:
                # 현재 활성 페이지 확인
                current_active = self.get_current_page()
                
                if current_active == target_page:
                    print(f"    ✅ 활성 페이지 변경 완료: {target_page}")
                    
                    # 테이블 데이터도 로딩될 때까지 추가 대기
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "table.data-table tbody tr"))
                    )
                    time.sleep(1)  # 데이터 안정화
                    return True
                
                print(f"    대기 중... 현재 활성: {current_active}, 목표: {target_page} ({attempt + 1}/{max_attempts})")
                time.sleep(1)
                
            except Exception as e:
                print(f"    활성 페이지 확인 중 오류: {e}")
                time.sleep(1)
        
        print(f"    ❌ 활성 페이지 변경 시간 초과: {target_page}")
        return False

    def click_page_with_js_wait(self, page_num):
        """JavaScript 클릭 + 활성 페이지 변경 대기"""
        try:
            print(f"    {page_num}페이지 클릭 시도...")
            
            # 이동 전 현재 페이지 확인
            current_page = self.get_current_page()
            print(f"    클릭 전 활성 페이지: {current_page}")
            
            if current_page == page_num:
                print(f"    이미 {page_num}페이지에 있습니다.")
                return True
            
            # JavaScript로 페이지 클릭
            js_click_script = f"""
            // 페이지네이션에서 {page_num} 페이지 링크 찾기
            const pagination = document.querySelector('ul.pagination');
            const pageLinks = pagination.querySelectorAll('li.page-item.pagination-page-nav a.page-link');
            
            let targetLink = null;
            for (let link of pageLinks) {{
                if (link.textContent.trim() === '{page_num}') {{
                    targetLink = link;
                    break;
                }}
            }}
            
            if (targetLink) {{
                console.log('페이지 {page_num} 링크 클릭');
                targetLink.click();
                return true;
            }} else {{
                console.log('페이지 {page_num} 링크를 찾을 수 없음');
                return false;
            }}
            """
            
            click_result = self.driver.execute_script(js_click_script)
            
            if not click_result:
                print(f"    {page_num}페이지 링크를 찾을 수 없습니다.")
                return False
            
            # 활성 페이지 변경 대기
            return self.wait_for_active_page_change(page_num)
            
        except Exception as e:
            print(f"    페이지 클릭 중 오류: {e}")
            return False

    def click_next_button(self):
        """Next 버튼 클릭"""
        try:
            next_button = self.driver.find_element(
                By.CSS_SELECTOR, 
                "li.page-item.pagination-next-nav a.page-link"
            )
            
            # JavaScript로 Next 버튼 클릭
            self.driver.execute_script("arguments[0].click();", next_button)
            print("    Next 버튼 클릭 완료")
            return True
            
        except NoSuchElementException:
            print("    Next 버튼을 찾을 수 없습니다.")
            return False
        except Exception as e:
            print(f"    Next 버튼 클릭 중 오류: {e}")
            return False

    def navigate_with_next_button(self, target_page):
        """Next 버튼으로 목표 페이지까지 이동"""
        max_next_clicks = 20  # 최대 클릭 횟수 제한
        next_click_count = 0
        
        while next_click_count < max_next_clicks:
            try:
                # 현재 보이는 페이지 범위 확인
                pagination = self.driver.find_element(By.CSS_SELECTOR, "ul.pagination")
                visible_pages = self.get_visible_pages(pagination)
                current_page = self.get_current_page()
                
                print(f"    Next 시도 {next_click_count + 1}: 현재 페이지 {current_page}, 보이는 범위 {visible_pages}")
                
                # 목표 페이지가 이제 보이는지 확인
                if target_page in visible_pages:
                    print(f"    목표 페이지 {target_page}가 이제 보입니다!")
                    return self.click_page_with_js_wait(target_page)
                
                # Next 버튼 클릭
                next_success = self.click_next_button()
                if not next_success:
                    print("    Next 버튼 클릭 실패")
                    return False
                
                next_click_count += 1
                
                # Next 클릭 후 페이지네이션 변경 대기
                time.sleep(2)
                
            except Exception as e:
                print(f"    Next 버튼 이동 중 오류: {e}")
                return False
        
        print(f"    최대 Next 클릭 횟수 초과: {max_next_clicks}")
        return False
        
    def get_total_pages_accurate(self):
        """마지막 페이지 번호를 더 정확하게 파악"""
        try:
            pagination = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.pagination"))
            )
            
            page_links = pagination.find_elements(
                By.CSS_SELECTOR, 
                "li.page-item.pagination-page-nav a.page-link"
            )
            
            max_page = 1
            for link in page_links:
                page_text = link.text.strip()
                if page_text.isdigit():
                    page_num = int(page_text)
                    if page_num > max_page:
                        max_page = page_num
            
            print(f"감지된 최대 페이지: {max_page}")
            return max_page
            
        except Exception as e:
            print(f"총 페이지 수 확인 중 오류: {e}")
            return None
    
    def navigate_to_page(self, page_num):
        """특정 페이지로 이동 - 패턴 분석 기반 최적화"""
        try:
            if page_num == 1:
                # 1페이지는 처음 로딩된 상태이므로 확인만
                current = self.get_current_page()
                return current == 1
            
            print(f"    {page_num}페이지로 이동 중...")
            
            # 현재 페이지네이션에서 보이는 페이지들 확인
            pagination = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.pagination"))
            )
            
            visible_pages = self.get_visible_pages(pagination)
            print(f"    현재 보이는 페이지: {visible_pages}")
            
            # 목표 페이지가 보이는 경우
            if page_num in visible_pages:
                return self.click_page_with_js_wait(page_num)
            
            # 목표 페이지가 보이지 않는 경우 Next 버튼으로 이동
            print(f"    {page_num}페이지가 보이지 않음. Next 버튼 사용...")
            return self.navigate_with_next_button(page_num)
            
        except Exception as e:
            print(f"    {page_num}페이지 이동 중 오류: {e}")
            return False
    
    def get_qna_list_from_current_page(self):
        """현재 페이지의 Q&A 목록 가져오기"""
        try:
            # 테이블의 모든 행 가져오기
            rows = self.driver.find_elements(By.CSS_SELECTOR, "table.data-table tbody tr")
            
            qna_items = []
            
            for row in rows:
                try:
                    # 기본 정보 추출
                    cells = row.find_elements(By.TAG_NAME, "td")
                    
                    if len(cells) < 9:  # 필요한 칼럼 수 확인
                        continue
                    
                    # 우선순위 확인 (danger 클래스 여부)
                    row_classes = row.get_attribute("class")
                    is_urgent = "danger" in row_classes if row_classes else False
                    
                    inquiry_id = cells[0].text.strip()
                    
                    # 구분(카테고리) 정보 상세 추출
                    category_cell = cells[1]
                    assigned_team = None
                    sub_category = None
                    
                    try:
                        # 담당팀 정보 추출
                        team_label = category_cell.find_element(By.CSS_SELECTOR, "label.assigned-team")
                        assigned_team = team_label.text.strip()
                    except NoSuchElementException:
                        assigned_team = None
                    
                    try:
                        # 세부 카테고리 추출
                        category_span = category_cell.find_element(By.TAG_NAME, "span")
                        sub_category = category_span.text.strip()
                    except NoSuchElementException:
                        sub_category = None
                    
                    # 전체 카테고리 텍스트 (기존 방식 유지)
                    category_full = cells[1].text.strip()
                    
                    product_order_num = cells[2].text.strip() if cells[2].text.strip() else None
                    breach_order_num = cells[3].text.strip() if cells[3].text.strip() else None
                    seller = cells[4].text.strip()
                    
                    # 질문 링크 요소 찾기
                    question_cell = cells[5]
                    question_link = question_cell.find_element(By.CSS_SELECTOR, "div[style*='font-weight: bold'] i.fa-external-link")
                    question_text = question_cell.text.strip()
                    
                    answer_status = cells[6].text.strip()
                    registration_date = cells[7].text.strip()
                    last_answer_date = cells[8].text.strip() if cells[8].text.strip() else None
                    
                    qna_item = {
                        "inquiry_id": inquiry_id,
                        "is_urgent": is_urgent,
                        "category": {
                            "assigned_team": assigned_team,
                            "sub_category": sub_category,
                            "full_text": category_full
                        },
                        "product_order_number": product_order_num,
                        "breach_order_number": breach_order_num,
                        "seller": seller,
                        "question_preview": question_text,
                        "answer_status": answer_status,
                        "registration_date": registration_date,
                        "last_answer_date": last_answer_date,
                        "question_link_element": question_link
                    }
                    
                    qna_items.append(qna_item)
                    
                except Exception as e:
                    print(f"행 처리 중 오류: {e}")
                    continue
            
            print(f"현재 페이지에서 {len(qna_items)}개의 Q&A 항목 발견")
            return qna_items
            
        except Exception as e:
            print(f"Q&A 목록 가져오기 중 오류: {e}")
            return []
    
    def close_modal(self):
        """모달 창 닫기"""
        try:
            # 방법 1: close-btn 클릭
            try:
                close_button = self.driver.find_element(By.CSS_SELECTOR, "span.close-btn")
                self.driver.execute_script("arguments[0].click();", close_button)
                print("    close-btn 클릭으로 모달 닫기")
                time.sleep(0.5)
            except NoSuchElementException:
                print("    close-btn을 찾을 수 없음")
            
            # 방법 2: ESC 키 사용 (백업)
            if self.driver.find_elements(By.CSS_SELECTOR, "div.dialog-modal-box"):
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                print("    ESC 키로 모달 닫기")
                time.sleep(0.5)
            
            # 방법 3: 모달 외부 클릭 (최후 수단)
            if self.driver.find_elements(By.CSS_SELECTOR, "div.dialog-modal-box"):
                try:
                    overlay = self.driver.find_element(By.CSS_SELECTOR, ".modal-backdrop, .overlay")
                    self.driver.execute_script("arguments[0].click();", overlay)
                    print("    오버레이 클릭으로 모달 닫기")
                except NoSuchElementException:
                    # 모달 외부 빈 공간 클릭
                    self.driver.execute_script("document.body.click();")
                    print("    빈 공간 클릭으로 모달 닫기")
                time.sleep(0.5)
            
            # 모달이 사라질 때까지 대기
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.dialog-modal-box"))
            )
            
            print("    ✅ 모달 닫기 완료")
            return True
            
        except Exception as e:
            print(f"    ❌ 모달 닫기 실패: {e}")
            return False
    
    def wait_for_modal_close(self):
        """모달이 완전히 닫힐 때까지 대기"""
        try:
            # 모달이 화면에서 완전히 사라질 때까지 대기
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.dialog-modal-box"))
            )
            time.sleep(0.5)  # 추가 안정화 시간
            return True
        except TimeoutException:
            print("    모달 닫기 대기 시간 초과")
            return False

    def get_qna_detail(self, qna_item):
        """개별 Q&A 상세 정보 가져오기"""
        try:
            print(f"    모달 열기: {qna_item['inquiry_id']}")
            
            # 이전 모달이 있다면 먼저 닫기
            try:
                existing_modal = self.driver.find_element(By.CSS_SELECTOR, "div.dialog-modal-box")
                if existing_modal.is_displayed():
                    print("    기존 모달 발견, 닫는 중...")
                    self.close_modal()
                    self.wait_for_modal_close()
            except NoSuchElementException:
                pass
            
            # 질문 링크 클릭
            question_link = qna_item["question_link_element"]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", question_link)
            time.sleep(0.3)
            self.driver.execute_script("arguments[0].click();", question_link)
            
            # 새 모달 로딩 대기
            print("    모달 로딩 대기 중...")
            modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.dialog-modal-box"))
            )
            
            # 모달 내용이 완전히 로드될 때까지 추가 대기
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.dialog-modal-box .box-body"))
            )
            time.sleep(1)  # 내용 로딩 안정화
            
            print("    모달 로딩 완료, 내용 추출 중...")
            
            # 문의 내용 추출
            question_content = ""
            try:
                content_element = modal.find_element(By.CSS_SELECTOR, "pre.post-content")
                question_content = content_element.text.strip()
                print(f"    문의 내용 길이: {len(question_content)} 글자")
            except NoSuchElementException:
                print("    문의 내용을 찾을 수 없습니다.")
            
            # 작성자 정보 추출
            author_info = {}
            try:
                # 작성자명 추출
                author_elements = modal.find_elements(By.XPATH, "//label[contains(text(), '작성자')]/following-sibling::div")
                if author_elements:
                    author_text = author_elements[0].text.strip()
                    author_info["author"] = author_text
                
                # 이메일 추출
                email_elements = modal.find_elements(By.XPATH, "//label[contains(text(), '이메일')]/following-sibling::div")
                if email_elements:
                    author_info["email"] = email_elements[0].text.strip()
                
                # 연락처 추출
                phone_elements = modal.find_elements(By.XPATH, "//label[contains(text(), '연락처')]/following-sibling::div")
                if phone_elements:
                    phone_text = phone_elements[0].text.strip()
                    author_info["phone"] = phone_text.split('\n')[0] if phone_text else ""
                    
            except Exception as e:
                print(f"    작성자 정보 추출 중 오류: {e}")
            
            # 답변 목록 추출
            answers = []
            try:
                # 답변 테이블 찾기
                answer_tables = modal.find_elements(By.CSS_SELECTOR, "table.comment-table")
                
                for table in answer_tables:
                    tbody = table.find_element(By.TAG_NAME, "tbody")
                    answer_rows = tbody.find_elements(By.TAG_NAME, "tr")
                    
                    # 첫 번째 행은 헤더일 수 있으므로 확인
                    for row in answer_rows:
                        cells = row.find_elements(By.TAG_NAME, "td")
                        if len(cells) >= 3:
                            try:
                                # 작성자 정보 추출
                                author_cell = cells[0]
                                author_spans = author_cell.find_elements(By.TAG_NAME, "span")
                                author_name = author_spans[0].text.strip() if author_spans else ""
                                
                                # 부서 정보
                                dept_divs = author_cell.find_elements(By.CSS_SELECTOR, "div.text-sm")
                                author_dept = ""
                                answer_date = ""
                                
                                for div in dept_divs:
                                    text = div.text.strip()
                                    if "(" in text and ")" in text:
                                        author_dept = text
                                    elif "-" in text and ":" in text:  # 날짜 형식
                                        answer_date = text
                                
                                # 답변 내용
                                answer_content_element = cells[1].find_element(By.CSS_SELECTOR, "pre.comment_content")
                                answer_content = answer_content_element.text.strip()
                                
                                if author_name and answer_content:  # 유효한 답변만 추가
                                    answer = {
                                        "author_name": author_name,
                                        "author_department": author_dept,
                                        "answer_date": answer_date,
                                        "content": answer_content
                                    }
                                    answers.append(answer)
                                    
                            except Exception as e:
                                print(f"    답변 행 처리 중 오류: {e}")
                                continue
                                
                print(f"    답변 {len(answers)}개 추출 완료")
                        
            except NoSuchElementException:
                print("    답변 테이블을 찾을 수 없습니다.")
            except Exception as e:
                print(f"    답변 추출 중 오류: {e}")
            
            # 모달 확실히 닫기
            print("    모달 닫는 중...")
            modal_closed = self.close_modal()
            
            if not modal_closed:
                print("    ⚠️ 모달 닫기 실패, 다시 시도...")
                self.wait_for_modal_close()
            else:
                self.wait_for_modal_close()
            
            # 상세 정보 반환
            detail = {
                **{k: v for k, v in qna_item.items() if k != "question_link_element"},
                "question_content": question_content,
                "author_info": author_info,
                "answers": answers
            }
            
            print(f"    처리 완료: {qna_item['inquiry_id']}")
            return detail
            
        except TimeoutException:
            print(f"    모달 로딩 시간 초과: {qna_item['inquiry_id']}")
            self.close_modal()
            return None
        except Exception as e:
            print(f"    상세 정보 가져오기 중 오류: {e}")
            self.close_modal()
            return None
    
    def manual_login_and_navigate(self):
        """수동 로그인 후 Q&A 페이지로 이동"""
        print("로그인 페이지로 이동 중...")
        self.driver.get("https://b-flow.co.kr/login")
        
        print("\n" + "="*50)
        print("수동 로그인을 진행해주세요!")
        print("1. 브라우저에서 아이디/비밀번호를 입력하세요")
        print("2. 로그인이 완료되면 아무 키나 눌러주세요")
        print("="*50)
        
        input("로그인 완료 후 Enter를 눌러주세요...")
        
        print("Q&A 페이지로 이동 중...")
        self.driver.get(self.base_url)
        
        try:
            # Q&A 페이지 로딩 확인
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.data-table"))
            )
            print("Q&A 페이지 로딩 완료!")
            return True
        except TimeoutException:
            # 로그인이 안되었거나 페이지 로딩 실패시
            current_url = self.driver.current_url
            if "login" in current_url:
                print("로그인이 필요합니다. 다시 로그인을 진행해주세요.")
                return self.manual_login_and_navigate()
            else:
                print("Q&A 페이지 로딩에 실패했습니다.")
                return False

    def crawl_all_qna(self, max_pages=None, debug_mode=False):
        """모든 Q&A 크롤링"""
        try:
            # 수동 로그인
            if not self.manual_login_and_navigate():
                return
                
            # 디버그 모드면 페이지네이션 상태 확인
            if debug_mode:
                self.debug_pagination()
                
            # 전체 페이지 수 확인 (추정치)
            estimated_total_pages = self.get_total_pages_accurate()
            
            if max_pages:
                estimated_total_pages = min(estimated_total_pages, max_pages)
            
            print(f"\n📄 1페이지부터 크롤링 시작 (최대 {estimated_total_pages}페이지까지)")
            print("=" * 50)
            
            # 1페이지부터 시작하여 페이지가 없을 때까지 크롤링
            page_num = 1
            consecutive_failures = 0
            
            while page_num <= estimated_total_pages:
                print(f"\n🔍 [{page_num}] 페이지 처리 중...")
                
                # 디버그 모드면 각 페이지에서 상태 확인
                if debug_mode and page_num > 1:
                    self.debug_pagination()
                
                # 페이지 이동
                if not self.navigate_to_page(page_num):
                    consecutive_failures += 1
                    if consecutive_failures >= 3:
                        print(f"❌ 연속 {consecutive_failures}회 페이지 이동 실패. 크롤링 종료.")
                        break
                    print(f"❌ {page_num}페이지 이동 실패, 다음 페이지로...")
                    page_num += 1
                    continue
                
                # 실패 카운터 리셋
                consecutive_failures = 0
                
                # 페이지 안정화 대기
                time.sleep(1)
                
                # 현재 페이지의 Q&A 목록 가져오기
                qna_items = self.get_qna_list_from_current_page()
                
                if not qna_items:
                    print(f"⚠️  {page_num}페이지에서 Q&A를 찾을 수 없습니다. 마지막 페이지일 가능성이 높습니다.")
                    break
                
                print(f"📋 {len(qna_items)}개의 Q&A 발견됨")
                
                # 각 Q&A의 상세 정보 가져오기
                success_count = 0
                for i, qna_item in enumerate(qna_items):
                    print(f"  📝 [{i+1}/{len(qna_items)}] 처리 중: {qna_item['inquiry_id']}")
                    
                    detail = self.get_qna_detail(qna_item)
                    if detail:
                        self.qna_data.append(detail)
                        success_count += 1
                        print(f"    ✅ 수집 완료 (총 {len(self.qna_data)}개)")
                    else:
                        print(f"    ❌ 수집 실패")
                    
                    # 각 Q&A 처리 후 안정화 시간
                    time.sleep(1)
                
                print(f"✅ {page_num}페이지 완료: {success_count}/{len(qna_items)}개 성공 (총 {len(self.qna_data)}개 수집됨)")
                
                # 다음 페이지로
                page_num += 1
            
            print(f"\n🎉 크롤링 완료! 총 {len(self.qna_data)}개의 Q&A 수집됨 (마지막 페이지: {page_num - 1})")
            print("=" * 50)
            
        except Exception as e:
            print(f"크롤링 중 오류 발생: {e}")
        
        finally:
            self.driver.quit()
    
    def save_to_json(self, filename=None):
        """수집된 데이터를 JSON 파일로 저장 - output 폴더에!"""
        try:
            if filename is None:
                filename = get_crawl_filename()
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.qna_data, f, ensure_ascii=False, indent=2)
            print(f"✅ 데이터 저장: {filename}")
        except Exception as e:
            print(f"❌ 파일 저장 중 오류: {e}")
    
    def get_data(self):
        """수집된 데이터 반환"""
        return self.qna_data

# 사용 예시
if __name__ == "__main__":
    
    print("🚀 Q&A 크롤러 시작")
    print("=" * 50)
    
    # output 폴더 설정
    setup_output_dirs()
    
    # 수동 로그인으로 크롤링
    print("📌 수동 로그인으로 크롤링을 시작합니다.")
    print("   브라우저 창에서 로그인을 완료한 후 Enter를 눌러주세요.")
    
    crawler = QnACrawler(headless=False)  # 브라우저 창을 보여줌
    
    try:
        # 디버그 모드로 실행 (첫 번째 실행시)
        # crawler.crawl_all_qna(max_pages=2, debug_mode=True)
        
        # 일반 모드로 실행
        crawler.crawl_all_qna(max_pages=None)
        
        # JSON 파일로 저장 - output 폴더에!
        crawler.save_to_json()
        
        # 수집된 데이터 출력 (샘플)
        data = crawler.get_data()
        if data:
            print("\n" + "=" * 50)
            print("📊 수집 결과 요약")
            print("=" * 50)
            
            # 기본 통계
            total_count = len(data)
            answered_count = sum(1 for item in data if item['answer_status'] == '답변완료')
            urgent_count = sum(1 for item in data if item['is_urgent'])
            
            print(f"📋 총 수집된 Q&A: {total_count}개")
            print(f"✅ 답변 완료: {answered_count}개")
            print(f"⏳ 미답변: {total_count - answered_count}개")
            print(f"🚨 긴급 문의: {urgent_count}개")
            
            # 카테고리별 통계
            print(f"\n📂 카테고리별 통계:")
            category_stats = {}
            
            for item in data:
                team = item['category']['assigned_team'] or "미분류"
                sub_cat = item['category']['sub_category'] or "미분류"
                
                if team not in category_stats:
                    category_stats[team] = {}
                if sub_cat not in category_stats[team]:
                    category_stats[team][sub_cat] = 0
                category_stats[team][sub_cat] += 1
            
            for team, subcats in category_stats.items():
                print(f"\n[{team}]")
                for subcat, count in subcats.items():
                    print(f"  📌 {subcat}: {count}개")
            
            # 샘플 데이터 출력
            print(f"\n📄 샘플 데이터:")
            print(json.dumps(data[0], ensure_ascii=False, indent=2)[:500] + "...")
            
            print(f"\n✅ 크롤링 완료! 데이터가 output/crawl_data/ 폴더에 저장되었습니다.")
            
        else:
            print("❌ 수집된 데이터가 없습니다.")
            
    except KeyboardInterrupt:
        print("\n⚠️  사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        
    print("\n🏁 프로그램 종료")