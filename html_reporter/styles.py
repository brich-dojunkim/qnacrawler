# html_reporter/styles.py
"""CSS 스타일 모음 - 단순화된 모던 디자인"""

def get_main_styles():
    return """
/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    margin: 0;
    padding: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #333;
    line-height: 1.6;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    overflow: hidden;
}

/* Header Styles */
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 40px 30px;
    text-align: center;
    position: relative;
}

.header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 15px;
    text-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.header p {
    font-size: 1.1rem;
    margin-bottom: 10px;
    opacity: 0.95;
}

/* Main Content */
.main-content {
    padding: 40px 30px;
}

/* Major Section Styles */
.major-section {
    background: white;
    border: none;
    border-radius: 16px;
    margin-bottom: 30px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    overflow: hidden;
}

.major-section-header {
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    padding: 25px 30px;
    border-bottom: 1px solid #e2e8f0;
    position: relative;
}

.major-section-header::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.major-section-header h2 {
    font-size: 1.8rem;
    font-weight: 700;
    margin: 0;
    color: #1e293b;
}

.major-section-content {
    padding: 30px;
}

/* Card Styles */
.entity-card, .data-overview {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 24px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.entity-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.entity-card:hover::before {
    transform: scaleX(1);
}

.entity-card:hover, .data-overview:hover {
    border-color: #c7d2fe;
}

.entity-card-header, .data-overview-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid #f1f5f9;
}

.entity-card-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
    color: #1e293b;
}

.entity-card-badge {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.875rem;
    font-weight: 600;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

/* Stats Grid */
.data-stats {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 60px;
    margin: 0;
    padding: 20px 0;
}

.data-stat {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    position: relative;
}

.data-stat::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 40px;
    height: 3px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    border-radius: 2px;
}

.data-stat-name {
    font-size: 0.9rem;
    color: #64748b;
    margin-bottom: 8px;
    font-weight: 500;
}

.data-stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Grid Layouts */
.grid {
    display: grid;
    gap: 24px;
}

.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }
.grid-5 { grid-template-columns: repeat(5, 1fr); }

/* Metrics List */
.metrics-list {
    list-style: none;
    padding: 0;
    margin: 16px 0;
}

.metrics-list li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    margin-bottom: 8px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    transition: background 0.2s ease;
}

.metrics-list li:hover {
    background: linear-gradient(135deg, #e0f2fe, #e3f2fd);
}

.metrics-list li:last-child {
    margin-bottom: 0;
}

.metric-name {
    font-size: 0.9rem;
    color: #475569;
    font-weight: 500;
}

.metric-number {
    font-size: 1.1rem;
    font-weight: 700;
    color: #667eea;
}

/* Modal Styles */
.modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(8px);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}

.modal-overlay.active {
    display: flex;
}

.modal-content {
    background: white;
    border-radius: 20px;
    width: 90%;
    max-width: 900px;
    max-height: 85vh;
    overflow: hidden;
    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.3);
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 25px 30px;
    border-bottom: 1px solid #e2e8f0;
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
}

.modal-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
}

.modal-close {
    background: none;
    border: none;
    font-size: 1.8rem;
    cursor: pointer;
    color: #64748b;
    padding: 8px;
    border-radius: 8px;
    transition: all 0.2s ease;
}

.modal-close:hover {
    background: #f1f5f9;
    color: #374151;
    transform: scale(1.1);
}

.modal-body {
    padding: 30px;
    max-height: 65vh;
    overflow-y: auto;
}

/* Button Styles */
.modal-trigger {
    width: 100%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    margin-top: 16px;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.modal-trigger:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

/* Filter Buttons */
.filter-buttons {
    display: flex;
    gap: 12px;
    margin-bottom: 24px;
    justify-content: center;
    flex-wrap: wrap;
}

.filter-btn {
    padding: 10px 20px;
    border: 2px solid #e2e8f0;
    background: white;
    border-radius: 25px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 600;
    color: #64748b;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.filter-btn:hover {
    border-color: #667eea;
    color: #667eea;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
}

.filter-btn.active {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-color: #667eea;
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

/* Badge Styles */
.journey-badge {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

.team-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 12px 0;
}

.team-badge {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(245, 158, 11, 0.3);
}

/* Section Titles */
.small-subsection-title {
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 12px;
    margin-top: 20px;
    color: #374151;
    display: flex;
    align-items: center;
    gap: 8px;
}

.small-subsection-title::before {
    content: '';
    width: 4px;
    height: 16px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 2px;
}

/* Ranking Styles */
.rank-table-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #374151;
}

.rank-row {
    display: flex;
    align-items: center;
    margin-bottom: 8px;
    padding: 12px 16px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    transition: background 0.3s ease;
}

.rank-row:hover {
    background: linear-gradient(135deg, #e0f2fe, #e3f2fd);
}

.rank-number {
    min-width: 40px;
    font-size: 0.9rem;
    font-weight: 700;
    color: #667eea;
    text-align: center;
    background: white;
    border-radius: 20px;
    padding: 4px 8px;
    margin-right: 16px;
}

.rank-name {
    flex: 1;
    font-size: 0.9rem;
    font-weight: 600;
    color: #374151;
}

.rank-value {
    min-width: 100px;
    text-align: right;
    font-size: 0.9rem;
    font-weight: 700;
    color: #667eea;
}

.rank-summary {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid #e2e8f0;
    display: flex;
    gap: 24px;
    font-size: 0.8rem;
    color: #64748b;
    justify-content: center;
    font-weight: 500;
}

/* Simple List Styles */
.simple-list {
    margin: 16px 0;
}

.simple-list-title {
    font-size: 0.9rem;
    font-weight: 700;
    margin-bottom: 12px;
    color: #374151;
}

.simple-item {
    display: flex;
    align-items: center;
    margin-bottom: 6px;
    padding: 8px 12px;
    background: #f8fafc;
    border-radius: 8px;
    font-size: 0.85rem;
    transition: background 0.2s ease;
}

.simple-item:hover {
    background: #e0f2fe;
}

.simple-rank {
    min-width: 24px;
    font-weight: 700;
    color: #667eea;
}

.simple-name {
    flex: 1;
    margin-left: 8px;
    color: #374151;
    font-weight: 500;
}

.simple-value {
    min-width: 60px;
    text-align: right;
    font-weight: 700;
    color: #667eea;
}

/* Inquiry Card Styles */
.inquiry-card {
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    transition: background 0.3s ease;
    border-left: 4px solid #667eea;
}

.inquiry-card:hover {
    background: linear-gradient(135deg, #e0f2fe, #e3f2fd);
}

.inquiry-card:last-child {
    margin-bottom: 0;
}

.inquiry-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
}

.inquiry-content {
    color: #374151;
    line-height: 1.6;
    font-size: 0.95rem;
}

/* Urgency Badge */
.urgency-badge {
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.urgency-urgent {
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    color: #dc2626;
    border: 1px solid #fca5a5;
}

.urgency-normal {
    background: linear-gradient(135deg, #e0f2fe, #bae6fd);
    color: #0369a1;
    border: 1px solid #7dd3fc;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px;
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    border-top: 1px solid #e2e8f0;
    color: #64748b;
    font-size: 0.9rem;
    font-weight: 500;
}

/* Tab Navigation Styles */
.tab-navigation {
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    border-bottom: 1px solid #e2e8f0;
    padding: 0;
}

.tab-nav {
    display: flex;
    gap: 0;
    overflow-x: auto;
}

.tab-btn {
    padding: 18px 28px;
    border: none;
    background: none;
    font-size: 1rem;
    font-weight: 600;
    color: #64748b;
    cursor: pointer;
    border-bottom: 4px solid transparent;
    transition: all 0.3s ease;
    white-space: nowrap;
    position: relative;
}

.tab-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    opacity: 0;
    transition: opacity 0.3s ease;
}

.tab-btn:hover::before {
    opacity: 1;
}

.tab-btn.active {
    color: #667eea;
    border-bottom-color: #667eea;
    background: white;
    box-shadow: 0 -2px 8px rgba(102, 126, 234, 0.1);
}

.tab-btn:hover:not(.active) {
    color: #374151;
    background: rgba(255,255,255,0.7);
}

.tab-content {
    display: none;
    padding: 30px;
}

.tab-content.active {
    display: block;
}

/* Responsive Design */
@media (max-width: 1200px) {
    .grid-4 { grid-template-columns: repeat(2, 1fr); }
    .grid-5 { grid-template-columns: repeat(3, 1fr); }
    .data-stats { gap: 40px; }
}

@media (max-width: 768px) {
    body {
        padding: 10px;
    }
    
    .container {
        border-radius: 16px;
    }
    
    .header {
        padding: 30px 20px;
    }
    
    .header h1 {
        font-size: 2rem;
    }
    
    .main-content {
        padding: 20px;
    }
    
    .major-section-content {
        padding: 20px;
    }
    
    .grid-2, .grid-3, .grid-4, .grid-5 { 
        grid-template-columns: 1fr; 
    }
    
    .data-stats {
        flex-direction: column;
        gap: 20px;
    }
    
    .data-stat-number {
        font-size: 2rem;
    }
    
    .filter-buttons {
        flex-wrap: wrap;
        justify-content: center;
        gap: 8px;
    }
    
    .filter-btn {
        padding: 8px 16px;
        font-size: 0.85rem;
    }
    
    .rank-row {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        text-align: left;
    }
    
    .rank-number {
        min-width: auto;
        text-align: left;
        margin-right: 0;
        align-self: flex-start;
    }
    
    .rank-name {
        margin-left: 0;
    }
    
    .rank-value {
        text-align: left;
        min-width: auto;
    }
    
    .rank-summary {
        flex-direction: column;
        gap: 8px;
        text-align: center;
    }
    
    .simple-item {
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
    }
    
    .simple-rank, .simple-name, .simple-value {
        min-width: auto;
        text-align: left;
        margin-left: 0;
    }
    
    .team-badges {
        justify-content: flex-start;
    }
    
    .tab-nav {
        justify-content: space-between;
    }
    
    .tab-btn {
        flex: 1;
        padding: 14px 12px;
        font-size: 0.9rem;
    }
    
    .modal-content {
        width: 95%;
        margin: 20px;
        border-radius: 16px;
    }
    
    .modal-header {
        padding: 20px;
    }
    
    .modal-body {
        padding: 20px;
    }
    
    .modal-title {
        font-size: 1.3rem;
    }
}

@media (max-width: 480px) {
    .header h1 {
        font-size: 1.8rem;
    }
    
    .major-section-header h2 {
        font-size: 1.5rem;
    }
    
    .entity-card, .data-overview {
        padding: 16px;
    }
    
    .metrics-list li {
        padding: 10px 12px;
    }
    
    .data-stat-number {
        font-size: 1.8rem;
    }
}

/* Smooth scrollbar */
.modal-body::-webkit-scrollbar {
    width: 8px;
}

.modal-body::-webkit-scrollbar-track {
    background: #f1f5f9;
    border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #5a67d8, #6b46c1);
}
"""