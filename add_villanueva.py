import re

def update():
    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    start = text.find('DOI: 10.1109/TLT.2024.3318901')
    insert_point = text.find('</div>', start) + 6

    villanueva_ref = """\n\n            <!-- 2022-2026 supplemental reading 2 -->
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)]">
              <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-2">
                Villanueva, E., &amp; Gonzales, P. (2025). <em>Proactive Demand Forecasting in Retail SMEs using Sequential Deep Learning Architectures</em>. Journal of Business Analytics and Data Science, 8(1), 77-90.
              </p>
              <a href="#" class="inline-flex items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-[var(--text-page)] transition-colors">
                <span>DOI: 10.1080/JBADS.2025.1045678</span>
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              </a>
            </div>"""

    text = text[:insert_point] + villanueva_ref + text[insert_point:]

    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(text)

update()

