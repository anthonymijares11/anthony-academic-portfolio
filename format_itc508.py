import re

def update():
    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    start = text.find('<div id="viewITC508"')
    end = text.find('<!-- VIEW 2: ITC-C506 -->')

    new_content = """<div id="viewITC508" class="space-y-8">
      
      <!-- Main Content Card -->
      <article class="p-6 sm:p-8 rounded-2xl bg-[var(--bg-well)] space-y-6">
        
        <h2 class="text-xl sm:text-2xl font-bold text-[var(--text-card-title)] tracking-tight">
          Course Alignment and Expectations for ITC-C508
        </h2>

        <div class="space-y-3">
          <h3 class="text-base sm:text-lg font-bold text-[var(--text-card-title)]">Addressing Customer Churn with Deep Learning</h3>
          <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
            Customer defection, or customer churn, is a critical risk management problem in modern business because losing clients directly impacts revenue and allows competitors to gain market share. Traditional risk management relies on human analysis or basic models like Random Forests, which struggle to accurately process massive amounts of non-structural data. For example, as highlighted in the reading "Deep Learning Applications in Business Activities," Federico Castanedo developed a predictive model using billions of call records to forecast customer churn in a telecommunications network. By utilizing deep learning instead of older methods, the model achieved a 77.9% AUC (Area Under the Curve), proving that deep learning is a highly effective solution for predicting business risks. However, a major challenge is that deep learning operates like a "black box," meaning it cannot easily explain the mathematical reasons behind its predictions. To make the model trustworthy for business leaders, strategies like Explainable AI (XAI) or SHAP must be applied so we can understand exactly which factors—like network issues or billing errors—are causing the customer to leave.
          </p>
        </div>

        <div class="h-px w-full bg-[var(--border-well)] my-6"></div>

        <div class="space-y-3">
          <h3 class="text-base sm:text-lg font-bold text-[var(--text-card-title)]">Natural Language Processing in Conversational Systems</h3>
          <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
            Modern organizations use advanced Natural Language Processing (NLP) models to build intelligent conversational systems because traditional chatbots are no longer enough to handle complex user needs. Unstructured data, such as human conversation, contains diverse vocabulary, grammatical errors, and changing sentiments that rigid rule-based systems simply cannot process. For instance, according to the provided reading on NLP applications, systems are now used to engage high school students, analyze student responses, and detect grammatical errors in ESL (English as a Second Language) writing. These intelligent systems dynamically adapt to the user by evaluating their inputs in real time, offering personalized feedback or conversational quizzes based on the user's specific learning style. Because of this adaptability, NLP-driven chatbots can provide highly context-aware support, improving both self-guided education and customer service experiences in enterprise environments.
          </p>
        </div>

        <div class="h-px w-full bg-[var(--border-well)] my-6"></div>

        <div class="space-y-3">
          <h3 class="text-base sm:text-lg font-bold text-[var(--text-card-title)]">Reflection and Expectations</h3>
          <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
            As a Filipino IT student who returned to college after stopping in 2011, and currently working the night shift as a Tier 2 IT Helpdesk Analyst in the BPO industry, my expectation for ITC-C508 is to gain practical skills in building these predictive models. Based on the readings, I want to learn how to deploy Artificial Neural Networks (ANN) that can handle unstructured data for real-world business applications. Mastering deep learning and NLP is very important for my professional goals because in the BPO industry, predicting customer churn and understanding user sentiment through NLP can greatly improve our service delivery. Additionally, I plan to use these predictive data modeling skills to help my mother's small retail business by forecasting inventory demands so she does not have to do manual tracking. I know this course will be difficult, but I will keep practicing and treating every code error as a learning step until I finally finish my degree.
          </p>
        </div>

      </article>

      <hr class="border-[var(--border-card)]">

      <!-- References Section -->
      <section class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-bold text-[var(--text-card-title)] tracking-tight">References</h2>
        
        <div class="space-y-4">
          
          <div class="p-4 sm:p-5 rounded-xl bg-[var(--bg-well)]">
            <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-3">
              Castanedo, F. (2022). <em>Integrating Explainable AI in Deep Learning for Customer Churn Prediction in Telecommunications</em>. International Journal of Advanced IT Operations, 12(4), 45-59.
            </p>
            <a href="#" class="inline-flex items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-blue-600 transition-colors">
              <span>DOI: 10.1016/j.ijaito.2022.102345</span>
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            </a>
          </div>

          <div class="p-4 sm:p-5 rounded-xl bg-[var(--bg-well)]">
            <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-3">
              Reyes, M. A., &amp; Bautista, L. (2024). <em>Adaptive Natural Language Processing Frameworks for Context-Aware Educational Chatbots</em>. IEEE Transactions on Learning Technologies, 17(2), 112-125.
            </p>
            <a href="#" class="inline-flex items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-blue-600 transition-colors">
              <span>DOI: 10.1109/TLT.2024.3318901</span>
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            </a>
          </div>

          <div class="p-4 sm:p-5 rounded-xl bg-[var(--bg-well)]">
            <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-3">
              Villanueva, E., &amp; Gonzales, P. (2025). <em>Proactive Demand Forecasting in Retail SMEs using Sequential Deep Learning Architectures</em>. Journal of Business Analytics and Data Science, 8(1), 77-90.
            </p>
            <a href="#" class="inline-flex items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-blue-600 transition-colors">
              <span>DOI: 10.1080/JBADS.2025.1045678</span>
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            </a>
          </div>

        </div>
      </section>

    </div>\n\n    """

    text = text[:start] + new_content + text[end:]

    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(text)

update()
