# html_reporter/styles/components/__init__.py (모듈화된 패키지들만 사용)
"""컴포넌트 스타일 모듈 - 모듈화된 컴포넌트들만 사용"""

try:
    from .cards import get_card_styles
except ImportError:
    print("Warning: cards 모듈에서 get_card_styles를 import할 수 없습니다.")
    def get_card_styles():
        return ""

try:
    from .buttons import get_button_styles
except ImportError:
    print("Warning: buttons 모듈에서 get_button_styles를 import할 수 없습니다.")
    def get_button_styles():
        return ""

try:
    from .badges import get_badge_styles
except ImportError:
    print("Warning: badges 모듈에서 get_badge_styles를 import할 수 없습니다.")
    def get_badge_styles():
        return ""

try:
    from .modals import get_modal_styles
except ImportError:
    print("Warning: modals 모듈에서 get_modal_styles를 import할 수 없습니다.")
    def get_modal_styles():
        return ""

try:
    from .stats import get_stats_styles
except ImportError:
    print("Warning: stats 모듈에서 get_stats_styles를 import할 수 없습니다.")
    def get_stats_styles():
        return ""

try:
    from .ranking import get_ranking_styles
except ImportError:
    print("Warning: ranking 모듈에서 get_ranking_styles를 import할 수 없습니다.")
    def get_ranking_styles():
        return ""

# 모듈화된 패키지들만 import
try:
    from .accordion import get_accordion_styles
except ImportError:
    print("Warning: accordion 패키지에서 get_accordion_styles를 import할 수 없습니다.")
    def get_accordion_styles():
        return ""

try:
    from .category_table import get_category_table_styles
except ImportError:
    print("Warning: category_table 패키지에서 get_category_table_styles를 import할 수 없습니다.")
    def get_category_table_styles():
        return ""

try:
    from .drawer import get_drawer_styles
except ImportError:
    print("Warning: drawer 패키지에서 get_drawer_styles를 import할 수 없습니다.")
    def get_drawer_styles():
        return ""

def get_component_styles():
    """모든 UI 컴포넌트 스타일 조합 (모듈화된 패키지들만 사용)"""
    styles = [
        get_card_styles(),           # 카드 컴포넌트
        get_button_styles(),         # 버튼 컴포넌트
        get_badge_styles(),          # 배지 컴포넌트
        get_modal_styles(),          # 모달 컴포넌트
        get_stats_styles(),          # 통계 컴포넌트
        get_ranking_styles(),        # 랭킹 컴포넌트
        get_accordion_styles(),      # 모듈화된 아코디언 패키지
        get_category_table_styles(), # 모듈화된 카테고리 테이블 패키지
        get_drawer_styles(),         # 모듈화된 드로어 패키지
    ]
    
    return '\n'.join(styles)

def get_navigation_components():
    """네비게이션 관련 컴포넌트들"""
    styles = [
        get_button_styles(),         # 네비게이션 버튼들
        get_accordion_styles(),      # 아코디언 네비게이션
        get_drawer_styles(),         # 드로어 네비게이션
    ]
    
    return '\n'.join(styles)

def get_ui_components_only():
    """기본 UI 컴포넌트만"""
    styles = [
        get_card_styles(),
        get_button_styles(),
        get_badge_styles(),
        get_accordion_styles(),      # 모듈화된 아코디언 패키지
        get_category_table_styles(), # 모듈화된 카테고리 테이블 패키지
        get_drawer_styles()          # 모듈화된 드로어 패키지
    ]
    
    return '\n'.join(styles)

def get_overview_components():
    """개요 탭 컴포넌트들"""
    styles = [
        get_card_styles(),           # 분포 카드용
        get_stats_styles(),          # 통계 카드용
        get_ranking_styles(),        # 순위 아이템용
        get_accordion_styles(),      # 팀별 아코디언용
        get_category_table_styles(), # 카테고리 테이블용
        get_drawer_styles(),         # 드로어용
    ]
    
    return '\n'.join(styles)

def get_modal_components_only():
    """모달 관련 컴포넌트만"""
    styles = [
        get_button_styles(),         # modal-trigger 포함
        get_modal_styles(),          # 모달 오버레이
        get_card_styles(),           # inquiry-card 포함
        get_drawer_styles(),         # 드로어 (모달 대체)
    ]
    
    return '\n'.join(styles)

# 개별 모듈화된 패키지 기능별 접근 함수들
def get_accordion_base_styles():
    """기본 아코디언 구조만"""
    try:
        from .accordion import get_accordion_base_styles as _get_base
        return _get_base()
    except ImportError:
        return ""

def get_accordion_control_styles():
    """컨트롤 관련 스타일만"""
    try:
        from .accordion import get_accordion_control_styles as _get_control
        return _get_control()
    except ImportError:
        return ""

def get_accordion_metrics_styles():
    """메트릭 관련 스타일만"""
    try:
        from .accordion import get_accordion_metrics_styles as _get_metrics
        return _get_metrics()
    except ImportError:
        return ""

def get_category_table_header_styles():
    """카테고리 테이블 헤더 스타일만"""
    try:
        from .category_table import get_header_only
        return get_header_only()
    except ImportError:
        return ""

def get_category_table_body_styles():
    """카테고리 테이블 본문 스타일만"""
    try:
        from .category_table import get_body_only
        return get_body_only()
    except ImportError:
        return ""

def get_category_table_modal_styles():
    """카테고리 테이블 모달 스타일만"""
    try:
        from .category_table import get_modal_only
        return get_modal_only()
    except ImportError:
        return ""

def get_drawer_layout_styles():
    """드로어 기본 레이아웃만"""
    try:
        from .drawer import get_drawer_layout_styles as _get_layout
        return _get_layout()
    except ImportError:
        return ""

def get_drawer_header_combined():
    """드로어 헤더 관련 스타일만"""
    try:
        from .drawer import get_drawer_header_combined as _get_header
        return _get_header()
    except ImportError:
        return ""

def get_drawer_inquiry_styles():
    """드로어 문의 관련 스타일만"""
    try:
        from .drawer import get_drawer_inquiry_styles as _get_inquiry
        return _get_inquiry()
    except ImportError:
        return ""

__all__ = [
    # 메인 함수들
    'get_component_styles',
    'get_navigation_components',
    'get_ui_components_only', 
    'get_overview_components',
    'get_modal_components_only',
    
    # 개별 컴포넌트 함수들
    'get_card_styles',
    'get_button_styles',
    'get_badge_styles',
    'get_modal_styles',
    'get_stats_styles',
    'get_ranking_styles',
    'get_accordion_styles',          # 모듈화된 아코디언 패키지
    'get_category_table_styles',     # 모듈화된 카테고리 테이블 패키지
    'get_drawer_styles',             # 모듈화된 드로어 패키지
    
    # 개별 모듈화된 패키지 기능별 함수들
    'get_accordion_base_styles',
    'get_accordion_control_styles',
    'get_accordion_metrics_styles',
    'get_category_table_header_styles',
    'get_category_table_body_styles',
    'get_category_table_modal_styles',
    'get_drawer_layout_styles',
    'get_drawer_header_combined',
    'get_drawer_inquiry_styles',
]