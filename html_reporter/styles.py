# html_reporter/styles.py
"""CSS 스타일 모음"""

def get_main_styles():
    return """
body {
    font-family: 'Pretendard', -apple-system, sans-serif;
    margin: 0;
    padding: 1rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    background: white;
    border-radius: 16px;
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);
    overflow: hidden;
}

.header {
    background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
    color: white;
    padding: 2rem;
    text-align: center;
}

.header h1 {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.main-content {
    padding: 2rem;
}

.major-section {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
}

.major-section-header {
    background: #f8fafc;
    padding: 1.5rem;
    border-bottom: 1px solid #e2e8f0;
}

.major-section-header h2 {
    font-size: 1.5rem;
    font-weight: 600;
    margin: 0;
}

.major-section-content {
    padding: 1.5rem;
}

.entity-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.2s ease;
}

.entity-card:hover {
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    transform: translateY(-2px);
}

.entity-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid #e2e8f0;
}

.entity-card-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin: 0;
}

.entity-card-badge {
    background: #2563eb;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 500;
}

.data-overview {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    transition: all 0.2s ease;
}

.data-overview:hover {
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    transform: translateY(-2px);
}

.data-overview-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid #e2e8f0;
}

.data-stats {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 4rem;
    margin: 0;
    padding: 1rem 0;
}

.data-stat {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.data-stat-name {
    font-size: 0.85rem;
    color: #475569;
    margin-bottom: 0.25rem;
}

.data-stat-number {
    font-size: 1.5rem;
    font-weight: 700;
    color: #2563eb;
}

.grid {
    display: grid;
    gap: 1.5rem;
}

.grid-3 {
    grid-template-columns: repeat(3, 1fr);
}

.grid-4 {
    grid-template-columns: repeat(4, 1fr);
}

.metrics-list {
    list-style: none;
    padding: 0;
    margin: 1rem 0;
}

.metrics-list li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0;
    border-bottom: 1px solid #f1f5f9;
}

.metrics-list li:last-child {
    border-bottom: none;
}

.metric-name {
    font-size: 0.8rem;
    color: #64748b;
}

.metric-number {
    font-size: 1rem;
    font-weight: 600;
    color: #2563eb;
}

.modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}

.modal-overlay.active {
    display: flex;
}

.modal-content {
    background: white;
    border-radius: 12px;
    width: 90%;
    max-width: 800px;
    max-height: 80vh;
    overflow: hidden;
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem;
    border-bottom: 1px solid #e2e8f0;
    background: #f8fafc;
}

.modal-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #374151;
}

.modal-close {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #6b7280;
    padding: 0.25rem;
}

.modal-close:hover {
    color: #374151;
}

.modal-body {
    padding: 1.5rem;
    max-height: 60vh;
    overflow-y: auto;
}

.modal-trigger {
    width: 100%;
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.75rem;
    margin-top: 1rem;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
}

.modal-trigger:hover {
    background: #1d4ed8;
}

.footer {
    text-align: center;
    padding: 2rem;
    background: #f8fafc;
    border-top: 1px solid #e2e8f0;
    color: #475569;
    font-size: 0.875rem;
}

@media (max-width: 1200px) {
    .grid-4 { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
    .main-content { padding: 1rem; }
    .grid-3, .grid-4 { grid-template-columns: 1fr; }
    .data-stats {
        flex-direction: column;
        gap: 1rem;
    }
}
"""
