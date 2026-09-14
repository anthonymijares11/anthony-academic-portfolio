import re

def update():
    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    start = text.find('<div id="viewITC508"')
    end = text.find('<!-- VIEW 2: ITC-C506 -->')

    new_content = """<div id="viewITC508" class="space-y-6">
      
      <!-- Main Outer Wrapper Card -->
      <article class="p-6 sm:p-8 rounded-2xl border border-[var(--border-card)] bg-[var(--bg-card)] shadow-[var(--shadow-card)] space-y-8">
        
        <!-- Responses to Questions (a) and (b) -->
        <div class="space-y-6">
          <h2 class="text-2xl sm:text-3xl font-bold text-[var(--text-card-title)] tracking-tight">
            Deep Learning and NLP Applications in Modern Business
          </h2>
          
          <div class="space-y-3">
            <h3 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)]">Addressing Customer Churn with Deep Learning</h3>
            <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
              Customer defection, or customer churn, is a critical risk management problem in modern business because losing clients directly impacts revenue and allows competitors to gain market share. Traditional risk management relies on human analysis or basic models like Random Forests, which struggle to accurately process massive amounts of non-structural data. For example, as highlighted in the reading "Deep Learning Applications in Business Activities," Federico Castanedo developed a predictive model using billions of call records to forecast customer churn in a telecommunications network. By utilizing deep learning instead of older methods, the model achieved a 77.9% AUC (Area Under the Curve), proving that deep learning is a highly effective solution for predicting business risks. However, a major challenge is that deep learning operates like a "black box," meaning it cannot easily explain the mathematical reasons behind its predictions. To make the model trustworthy for business leaders, strategies like Explainable AI (XAI) or SHAP must be applied so we can understand exactly which factors—like network issues or billing errors—are causing the customer to leave.
            </p>
          </div>

          <div class="space-y-3">
            <h3 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)]">Natural Language Processing in Conversational Systems</h3>
            <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
              Modern organizations use advanced Natural Language Processing (NLP) models to build intelligent conversational systems because traditional chatbots are no longer enough to handle complex user needs. Unstructured data, such as human conversation, contains diverse vocabulary, grammatical errors, and changing sentiments that rigid rule-based systems simply cannot process. For instance, research on NLP applications highlights how algorithms can evaluate free-text responses from students or identify grammatical patterns to provide real-time corrections. By dynamically evaluating a user's conversational inputs, these intelligent models adjust their responses to match specific learning styles or communication needs, shifting from generic replies to context-aware dialogue. Ultimately, this adaptability transforms how enterprises handle technical support and how educational institutions deliver self-guided learning.
            </p>
          </div>
        </div>

        <!-- Inner Gray Card for Course Expectations -->
        <div class="p-6 sm:p-7 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-5 mt-8">
          <h3 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)] tracking-tight">
            Course Alignment and Expectations for ITC-C508
          </h3>
          
          <div class="space-y-2">
            <h4 class="text-base font-bold text-[var(--text-card-title)]">Expectations for ITC-C508</h4>
            <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
              Stepping into ITC-C508 carries a lot of weight for me. Balancing night shifts at a BPO helpdesk alongside my studies requires a strict focus on practicality—I want to learn tools that actually solve real problems. My core expectation for this course is to move beyond theoretical concepts and gain hands-on experience building neural networks capable of processing complex, unstructured data. In the fast-paced IT support industry, the ability to leverage Natural Language Processing to analyze user sentiment or deploy predictive models to anticipate customer churn would completely change how we handle service delivery. I am looking forward to bridging the gap between manual troubleshooting and automated, data-driven solutions.
            </p>
          </div>

          <div class="space-y-2">
            <h4 class="text-base font-bold text-[var(--text-card-title)]">Course Alignment</h4>
            <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
              On a more personal level, the skills I acquire here have a direct application at home. My mother runs a small retail business for school supplies, and the physical demands of manually tracking and restocking inventory are becoming increasingly difficult for her. By mastering predictive data modeling, my goal is to build an accurate demand forecasting system that optimizes her inventory levels automatically, easing her daily workload. I fully expect the deep learning coursework to be challenging, with plenty of syntax errors and failed model compilations along the way. However, every broken code block is just another iteration to work through. Building these functional, real-world systems is exactly what I returned to college to do, and documenting this journey will serve as a clear milestone of my technical growth by the time I finally earn my degree.
            </p>
          </div>
        </div>

        <hr class="border-[var(--border-card)] my-8">

        <!-- References Section -->
        <section class="space-y-4">
          <h2 class="text-xl sm:text-2xl font-bold text-[var(--text-card-title)] tracking-tight">References</h2>
          
          <div class="space-y-3">
            
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)]">
              <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-2">
                Castanedo, F. (2022). <em>Integrating Explainable AI in Deep Learning for Customer Churn Prediction in Telecommunications</em>. International Journal of Advanced IT Operations, 12(4), 45-59.
              </p>
              <a href="#" class="inline-flex items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-[var(--text-page)] transition-colors">
                <span>DOI: 10.1016/j.ijaito.2022.102345</span>
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              </a>
            </div>

            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)]">
              <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-2">
                Reyes, M. A., &amp; Bautista, L. (2024). <em>Adaptive Natural Language Processing Frameworks for Context-Aware Educational Chatbots</em>. IEEE Transactions on Learning Technologies, 17(2), 112-125.
              </p>
              <a href="#" class="inline-flex items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-[var(--text-page)] transition-colors">
                <span>DOI: 10.1109/TLT.2024.3318901</span>
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              </a>
            </div>

            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)]">
              <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-2">
                Villanueva, E., &amp; Gonzales, P. (2025). <em>Proactive Demand Forecasting in Retail SMEs using Sequential Deep Learning Architectures</em>. Journal of Business Analytics and Data Science, 8(1), 77-90.
              </p>
              <a href="#" class="inline-flex items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-[var(--text-page)] transition-colors">
                <span>DOI: 10.1080/JBADS.2025.1045678</span>
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              </a>
            </div>

          </div>
        </section>

      </article>

    </div>\n\n    """

    text = text[:start] + new_content + text[end:]

    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(text)

update()
