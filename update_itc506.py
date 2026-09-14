import re

def update():
    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    start = text.find('<!-- Course Introduction Tab -->\n      <div id="itcContentIntro"')
    end = text.find('<!-- Prelim Period Tab -->', start)

    new_content = """<!-- Course Introduction Tab -->
      <div id="itcContentIntro" class="space-y-6 animate-fade-in block">
        <article class="p-6 sm:p-8 rounded-2xl border border-[var(--border-card)] bg-[var(--bg-card)] shadow-[var(--shadow-card)] space-y-8">
          
          <div class="space-y-2.5">
            <h3 class="text-xl sm:text-2xl font-bold text-[var(--text-card-title)] tracking-tight">Introduction</h3>
            <h4 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)] tracking-tight">Introduction</h4>
            <p class="text-sm sm:text-[15px] leading-relaxed text-[var(--text-card-body)] text-justify">
              In 2026, the rapid evolution of technology has transformed data-driven intelligence from an optional advantage into a fundamental necessity for business operations and strategic decision-making. There is a growing global reliance on predictive modeling, which is a sophisticated statistical approach that leverages historical data and machine learning algorithms to forecast future outcomes. This technique has shifted from a mere competitive edge to a standard requirement for any enterprise aiming to maintain a position in the modern market. This review examines how various organizations across the retail, finance, and logistics sectors integrate these predictive frameworks to enhance their operational efficiency and drive informed decision-making.
            </p>
          </div>

          <div class="space-y-3 pt-4 border-t border-[var(--border-well)]">
            <h4 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)] tracking-tight">
              The Modern Business Impact of Predictive Models
            </h4>
            <div class="space-y-3.5 text-sm sm:text-[15px] leading-relaxed text-[var(--text-card-body)] text-justify">
              <p>
                The modern business impact is now prominent in 2026 and it is being reflected those enterprises are joining the hype-train and moving away from intuition-based strategies toward "predict-then-optimize" workflows. The standard for business performance has shifted its gear through minute-to-minute updates using Real-Time Analytics where streaming data processing allows for sub-second decision support in critical areas such as fraud detection, dynamic pricing that allows businesses to act instantly based on the provided information, mitigating and reducing risks while maximizing opportunities in order to maintain a competitive edge to a fast-moving market or economy. Predictive models promote Operational Resilience that allows Small and Medium Enterprises (SMEs) to anticipate disruptions that allows them to allocate limited resources efficiently, providing a more "personalized" approach to navigating challenges that were previously the domain of large corporations. Another critical shift is Decision Alignment, as durable business value is realized by explicitly tying predictive outputs to operational policies, such as automated inventory replenishment or calibrated credit card approval thresholds.
              </p>
              <p>
                Based on the researchers, the effectiveness of predictive modeling depends more on end-to-end decision pipelines that on algorithmic novelty alone. In retail, the researchers conclude that hierarchical demand forecasting in combination with decision-aware pricing led to a 2.8% reduction of stockouts, which results in 2.2% revenue lift. While in finance, calibrated scorecards and cost-sensitive fraud triage resulted an 8% reduction in expected credit loss and a 22% reduction in false positives. When applied to logistics, uncertainty-aware Estimated Time of Arrival (ETA) and travel-time prediction have delivered an improvement of 3.9% in on-time delivery and routing costs reduction of 6%. These studies highlighted that organization using fully aligned designs while combining temporal validation, probability calibration and explicit threshold logic benefiting in a business improvement in 93% of cases. In contrast, it requires the need for methodological rigor as designs that are minimally aligned succeed only 48% of the time.
              </p>
              <p>
                Despite those advancements, the SMEs are still continuously encountering issues such as limited data access, high adaptation and implementation costs, and a lack of in-house technical expertise, which require an external consultant to train their employees. In terms of the Quality of Data, it requires to be consistent yet high-quality which is a core foundation, and without it the model utility is severely undermined. Regarding Ethical Governance, modern framework prioritize responsible AI, which includes model interpretability for regulatory compliance and the mitigation of bias in the automation of decision-making. Although, with the rise of cloud-based AI platforms, namely Google Cloud AI and Microsoft Azure, is narrowing the gap, allowing smaller firms to access these sophisticated tools without massive upfront investments.
              </p>
            </div>
          </div>

          <!-- Inner Gray Card for Course Expectations -->
          <div class="p-6 sm:p-7 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-4 mt-8">
            <h3 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)] tracking-tight">
              Course Alignment and Expectations for ITC-C506
            </h3>
            
            <div class="space-y-2">
              <h4 class="text-base font-bold text-[var(--text-card-title)]">Expectations for ITC-C506</h4>
              <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
                My expectation for this course IT Elective 3 ITC C506 is to engage myself in rigorous, hands-on activities designed to sharpen the technical competencies required in the modern job market upon graduating prepared by our Professor. Additionally, its major focus is placed and be involved on the end-to-end development and refinement of data models to achieve high-level precision. Through these practical exercises, ultimately my goal is to develop functional systems specifically to alleviate the manual labor involved in running our family-owned retail store, as well as getting equipped for our capstone project.
              </p>
            </div>

            <div class="space-y-2">
              <h4 class="text-base font-bold text-[var(--text-card-title)]">Course Alignment</h4>
              <p class="text-sm leading-relaxed text-[var(--text-card-body)] text-justify">
                Driven by a desire to apply predictive modeling to real-world challenges, the goal is to explore how data science can transform the retail sector. This interest is deeply personal, inspired by my mother’s small school-supplies business. By mastering demand forecasting and dynamic pricing, the aim is to optimize inventory management and reduce the physical burden of manual restocking. This would allow the business owner, which is my mom, to stay at home more often, easing the stress of travel to suppliers as she gets older. While retail is a primary focus, there is still an openness to exploring otherindustries as the course progresses. Rather than rushing a final decision, the current strategy is to focus on the immediate lessons and tasks. This "step-by-step" mindset is essential for maintaining mental well-being while navigating medical treatments and being neurodivergent. By focusing on the present, the work remains manageable and the sense of curiosity stays high. The process of building and fine-tuning a model for the first time is seen as a highly rewarding milestone. This journey will be documented in a research portfolio to serve as a professional retrospective. Looking back at these early phases after the course is finished will provide a clear view of the growth and technical progress achieved during the program.
              </p>
            </div>
          </div>

          <hr class="border-[var(--border-well)] my-8">

          <!-- References Section -->
          <section class="space-y-4">
            <h2 class="text-xl sm:text-2xl font-bold text-[var(--text-card-title)] tracking-tight">References</h2>
            
            <div class="space-y-3">
              
              <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] overflow-hidden">
                <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-2">
                  Agu, Chiekezie &amp; Abhulimen, &amp; Obiki-Osafiele, P &amp; Abhulimen, Angela. (2024). Building sustainable business models with predictive analytics: Case studies from various industries. International Journal of Advanced Economics. 6. 394-406. 10.51594/ijae.v6i8.1436.
                </p>
                <a href="https://www.researchgate.net/profile/Angela-Abhulimen/publication/383860897_Building_sustainable_business_models_with_predictive_analytics_Case_studies_from_various_industries/links/66ddb6adfa5e11512ca8ed7c/Building-sustainable-business-models-with-predictive-analytics-Case-studies-from-various-industries.pdf?origin=scientificContributions" target="_blank" class="block truncate items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-[var(--text-page)] transition-colors">
                  <span>https://www.researchgate.net/profile/Angela-Abhulimen/publication/383860897_Building_sustainable_business_models_with_predictive_analytics_Case_studies_from_various_industries/links/66ddb6adfa5e11512ca8ed7c/Building-sustainable-business-models-with-predictive-analytics-Case-studies-from-various-industries.pdf?origin=scientificContributions</span>
                </a>
              </div>

              <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] overflow-hidden">
                <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-2">
                  d Redwanul Islam, &amp; Md. Zafor Ikbal. (2022). IMPACT OF PREDICTIVE DATA MODELING ON BUSINESS DECISION-MAKING: A REVIEW OF STUDIES ACROSS RETAIL, FINANCE, AND LOGISTICS. American Journal of Advanced Technology and Engineering Solutions, 2(02), 33-62. <a href="https://doi.org/10.63125/8hfbkt70" class="text-blue-500 hover:underline">https://doi.org/10.63125/8hfbkt70</a>
                </p>
                <div class="flex flex-col gap-1 mt-2">
                  <a href="https://ajates-scholarly.com/index.php/ajates/article/view/50/46" target="_blank" class="block truncate items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-[var(--text-page)] transition-colors">
                    <span>https://ajates-scholarly.com/index.php/ajates/article/view/50/46</span>
                  </a>
                </div>
              </div>

              <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] overflow-hidden">
                <p class="text-sm text-[var(--text-card-body)] leading-relaxed mb-2">
                  Archie, Oliver. (2024). Proactive Market Forecasting for SMEs: The Role of Predictive Models in Navigating Business Challenges. 10.13140/RG.2.2.30355.59682.
                </p>
                <a href="https://doi.org/10.13140/RG.2.2.30355.59682" target="_blank" class="block truncate items-center gap-1.5 text-xs font-mono font-medium text-[var(--text-card-title)] hover:text-[var(--text-page)] transition-colors">
                  <span>https://doi.org/10.13140/RG.2.2.30355.59682</span>
                </a>
              </div>

            </div>
          </section>

        </article>
      </div>\n\n      """

    text = text[:start] + new_content + text[end:]

    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(text)

update()

