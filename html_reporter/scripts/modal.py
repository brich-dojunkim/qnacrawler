"""
모달 열기·닫기 및 ESC/외부 클릭 처리
"""

def get_modal_scripts() -> str:
    return """
function openModal(id){
    const m=document.getElementById(id);
    if(m){ m.classList.add('active'); document.body.style.overflow='hidden'; }
}
function closeModal(id){
    const m=document.getElementById(id);
    if(m){ m.classList.remove('active'); document.body.style.overflow='auto'; }
}

// ESC
document.addEventListener('keydown',e=>{
    if(e.key==='Escape'){
        const act=document.querySelector('.modal-overlay.active');
        if(act) closeModal(act.id);
    }
});
// 외부 클릭
document.addEventListener('click',e=>{
    if(e.target.classList.contains('modal-overlay')) closeModal(e.target.id);
});
"""
