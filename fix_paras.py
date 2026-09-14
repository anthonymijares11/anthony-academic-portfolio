import re

def update():
    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    start = text.find('<h4 class="text-base font-bold text-[var(--text-card-title)]">Course Alignment</h4>')
    if start != -1:
        end = text.find('</div>', start)
        
        new_block = """<h4 class="text-base font-bold text-[var(--text-card-title)]">Course Alignment</h4>
              <div class="space-y-3.5 text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
                <p>
                  Driven by a desire to apply predictive modeling to real-world challenges, the goal is to explore how data science can transform the retail sector. This interest is deeply personal, inspired by my mother’s small school-supplies business. By mastering demand forecasting and dynamic pricing, the aim is to optimize inventory management and reduce the physical burden of manual restocking. This would allow the business owner, which is my mom, to stay at home more often, easing the stress of travel to suppliers as she gets older.
                </p>
                <p>
                  While retail is a primary focus, there is still an openness to exploring other industries as the course progresses. Rather than rushing a final decision, the current strategy is to focus on the immediate lessons and tasks. This &ldquo;step-by-step&rdquo; mindset is essential for maintaining mental well-being while navigating medical treatments and being neurodivergent. By focusing on the present, the work remains manageable and the sense of curiosity stays high.
                </p>
                <p>
                  The process of building and fine-tuning a model for the first time is seen as a highly rewarding milestone. This journey will be documented in a research portfolio to serve as a professional retrospective. Looking back at these early phases after the course is finished will provide a clear view of the growth and technical progress achieved during the program.
                </p>
              </div>"""
        
        text = text[:start] + new_block + text[end:]
        
        with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
            f.write(text)

update()
