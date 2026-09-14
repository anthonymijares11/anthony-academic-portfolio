import urllib.parse
html = """
      <div class="space-y-5">
        <h3 class="text-base sm:text-lg font-bold text-[var(--text-page)] pt-2">Prelim Period Coursework</h3>
      

      <!-- Activity 1: WW-P2 -->
      <article class="p-6 sm:p-7 rounded-2xl border border-[var(--border-card)] bg-[var(--bg-card)] space-y-4 shadow-[var(--shadow-card)] transition-all duration-200">
        <h4 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)] tracking-tight">
          Written Work 2: Introduction to NLP Concepts
        </h4>

        <!-- Main PDF -->
        <div class="my-3 p-3.5 sm:p-4 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex flex-wrap items-center justify-between gap-3 transition-colors duration-150">
          <div class="flex items-center gap-2.5 min-w-0 max-w-xl">
            <span class="p-2 rounded-lg bg-[var(--bg-card)] border border-[var(--border-well)] flex items-center justify-center shrink-0">
              <svg class="w-4 h-4 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            </span>
            <div class="min-w-0">
              <span class="text-xs sm:text-[13px] font-semibold text-[var(--text-card-title)] block leading-snug truncate sm:whitespace-normal">
                Research Paper: An Introductory Overview of Natural Language Processing
              </span>
            </div>
          </div>
          <div class="flex items-center gap-2 shrink-0">
            <button onclick="openAssetModal('assets/docs/itc508/WW-P2  Introduction to NLP Concepts - Mijares.pdf', 'WW-P2: NLP Concepts', 'pdf')" class="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-lg bg-[var(--bg-card)] border border-[var(--border-well)] text-[var(--text-card-title)] hover:opacity-80 transition font-medium cursor-pointer shadow-xs">
              <svg class="w-3.5 h-3.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path><polyline points="10 17 15 12 10 7"></polyline><line x1="15" y1="12" x2="3" y2="12"></line></svg>
              <span>View PDF</span>
            </button>
          </div>
        </div>

        <!-- Certificates -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div class="p-3 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex items-center justify-between gap-2">
            <div class="flex items-center gap-2 min-w-0">
              <svg class="w-3.5 h-3.5 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span class="text-xs font-semibold text-[var(--text-card-title)] truncate">Course Certificate</span>
            </div>
            <button onclick="openAssetModal('assets/docs/itc508/Introduction to natural language processing concepts-Certificate.pdf', 'Course Certificate', 'pdf')" class="text-[11px] font-medium text-[var(--text-page)] hover:underline whitespace-nowrap">View</button>
          </div>
          <div class="p-3 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex items-center justify-between gap-2">
            <div class="flex items-center gap-2 min-w-0">
              <svg class="w-3.5 h-3.5 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span class="text-xs font-semibold text-[var(--text-card-title)] truncate">Completion Record</span>
            </div>
            <button onclick="openAssetModal('assets/docs/itc508/Introduction to natural language processing concepts-completion.pdf', 'Completion Record', 'pdf')" class="text-[11px] font-medium text-[var(--text-page)] hover:underline whitespace-nowrap">View</button>
          </div>
        </div>

        <div class="space-y-1.5 pt-1">
          <h5 class="text-sm sm:text-base font-bold text-[var(--text-card-title)]">Description</h5>
          <p class="text-sm leading-relaxed text-[var(--text-card-body)] font-normal" style="text-indent: 2rem;">This written work evaluated fundamental NLP techniques using client-side, browser-based AI playgrounds across three core tasks: generative abstractive summarization using Microsoft Phi 3.5 Mini, multilingual text classification, and automated Personally Identifiable Information (PII) extraction. The experiment aimed to synthesize complex technical documents locally, test multi-lingual confidence, and automate privacy sanitization while observing NER false positives.</p>
        </div>

        <details class="course-details text-xs group pt-2 border-t border-[var(--border-well)]">
          <summary class="cursor-pointer font-semibold text-[var(--text-card-title)] hover:opacity-80 flex items-center justify-between py-1.5 select-none">
            <span class="flex items-center gap-2">
              <svg class="w-3.5 h-3.5 shrink-0 text-[var(--text-card-muted)] transition-transform duration-200 group-open:rotate-90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"></polyline></svg>
              <span>Technical Skills, Significance, and Reflection</span>
            </span>
            <span class="text-[11px] text-[var(--text-card-muted)] font-normal group-open:hidden">View details</span>
            <span class="text-[11px] text-[var(--text-card-muted)] font-normal hidden group-open:inline">Hide details</span>
          </summary>
          <div class="mt-3 space-y-2.5">
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-1.5">
              <h6 class="text-sm font-bold text-[var(--text-card-title)]">Predictive &amp; Technical Skills</h6>
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)]" style="text-indent: 2rem;">Conducted generative abstractive summarization using local Small Language Models (SLMs). Evaluated character-level n-gram patterns for multilingual classification and exposed confidence degradation limits on mixed-language inputs. Utilized Text PII Extraction Analyzers for privacy compliance, identifying the trade-offs between sparse TF-IDF matrices and dense semantic embeddings.</p>
            </div>
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-1.5">
              <h6 class="text-sm font-bold text-[var(--text-card-title)]">Professional Significance</h6>
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)]" style="text-indent: 2rem;">As a student navigating the transition toward AI engineering, mastering client-side NLP workflows is critical for developing privacy-preserving text analytics systems. The ability to deploy models locally without external cloud dependencies ensures data compliance and lays an essential architectural foundation for future capstone development.</p>
            </div>
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-1.5">
              <h6 class="text-sm font-bold text-[var(--text-card-title)]">Learning Reflection</h6>
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)] italic font-medium" style="text-indent: 2rem;">&ldquo;This activity bridged theoretical NLP concepts with practical execution. One of the most insightful challenges was observing how a multi-language document drastically reduced the model's prediction confidence, highlighting the absolute necessity of sentence-level pre-processing and chunking. Additionally, analyzing NER false positives, such as identifying a corporate brand name as a person, reinforced that while automation is powerful, human oversight remains a mandatory component of production-grade pipelines.&rdquo;</p>
            </div>
          </div>
        </details>
      </article>

      <!-- Activity 2: PT-P1 -->
      <article class="p-6 sm:p-7 rounded-2xl border border-[var(--border-card)] bg-[var(--bg-card)] space-y-4 shadow-[var(--shadow-card)] transition-all duration-200">
        <h4 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)] tracking-tight">
          Performance Task 1: Deep Learning Neural Networks
        </h4>

        <div class="my-3 p-3.5 sm:p-4 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex flex-wrap items-center justify-between gap-3 transition-colors duration-150">
          <div class="flex items-center gap-2.5 min-w-0 max-w-xl">
            <span class="p-2 rounded-lg bg-[var(--bg-card)] border border-[var(--border-well)] flex items-center justify-center shrink-0">
              <svg class="w-4 h-4 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            </span>
            <div class="min-w-0">
              <span class="text-xs sm:text-[13px] font-semibold text-[var(--text-card-title)] block leading-snug truncate sm:whitespace-normal">
                Research Paper: Evaluating Dataset Scaling and Edge Case Vulnerabilities
              </span>
            </div>
          </div>
          <div class="flex items-center gap-2 shrink-0">
            <button onclick="openAssetModal('assets/docs/itc508/Exercise PT-P1 Deep Learning Neural Networks - MIJARES.pdf', 'PT-P1: Neural Networks', 'pdf')" class="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-lg bg-[var(--bg-card)] border border-[var(--border-well)] text-[var(--text-card-title)] hover:opacity-80 transition font-medium cursor-pointer shadow-xs">
              <svg class="w-3.5 h-3.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path><polyline points="10 17 15 12 10 7"></polyline><line x1="15" y1="12" x2="3" y2="12"></line></svg>
              <span>View PDF</span>
            </button>
          </div>
        </div>

        <!-- Snapshots / Excel -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div class="p-3 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex items-center justify-between gap-2">
            <div class="flex items-center gap-2 min-w-0">
              <svg class="w-3.5 h-3.5 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span class="text-xs font-semibold text-[var(--text-card-title)] truncate">Model Snapshot</span>
            </div>
            <button onclick="openAssetModal('assets/docs/itc508/Snapshot Model Information.pdf', 'Model Snapshot', 'pdf')" class="text-[11px] font-medium text-[var(--text-page)] hover:underline whitespace-nowrap">View</button>
          </div>
          <div class="p-3 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex items-center justify-between gap-2">
            <div class="flex items-center gap-2 min-w-0">
              <svg class="w-3.5 h-3.5 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span class="text-xs font-semibold text-[var(--text-card-title)] truncate">Experimental Tally (Excel)</span>
            </div>
            <a href="assets/docs/itc508/Tally_of_Experiments_MIJARES_PTP1.xlsx" download class="text-[11px] font-medium text-[var(--text-page)] hover:underline whitespace-nowrap">Download</a>
          </div>
        </div>

        <div class="space-y-1.5 pt-1">
          <h5 class="text-sm sm:text-base font-bold text-[var(--text-card-title)]">Description</h5>
          <p class="text-sm leading-relaxed text-[var(--text-card-body)] font-normal" style="text-indent: 2rem;">This performance task focused on evaluating the efficacy and limitations of a neural network-based text classifier using the Machine Learning for Kids platform. The model was trained to dynamically categorize ITSM operational feedback into three distinct classes: Positive Praise, Negative Complaint, and Urgent Support. It involved iterative stress-testing to measure predictive confidence against standard reports, sarcastic phrasing, and unclassified administrative edge cases.</p>
        </div>

        <details class="course-details text-xs group pt-2 border-t border-[var(--border-well)]">
          <summary class="cursor-pointer font-semibold text-[var(--text-card-title)] hover:opacity-80 flex items-center justify-between py-1.5 select-none">
            <span class="flex items-center gap-2">
              <svg class="w-3.5 h-3.5 shrink-0 text-[var(--text-card-muted)] transition-transform duration-200 group-open:rotate-90" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"></polyline></svg>
              <span>Technical Skills, Significance, and Reflection</span>
            </span>
            <span class="text-[11px] text-[var(--text-card-muted)] font-normal group-open:hidden">View details</span>
            <span class="text-[11px] text-[var(--text-card-muted)] font-normal hidden group-open:inline">Hide details</span>
          </summary>
          <div class="mt-3 space-y-2.5">
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-1.5">
              <h6 class="text-sm font-bold text-[var(--text-card-title)]">Predictive &amp; Technical Skills</h6>
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)]" style="text-indent: 2rem;">Engineered a text classifier by converting raw textual data into numerical tokens and computing mathematical associations across predefined labels. Executed systematic dataset scaling (from 30 to 180 examples) to correct misclassifications of ambiguous and sarcastic inputs. Conducted vulnerability testing against out-of-vocabulary inputs to identify and document edge-case coercion failures.</p>
            </div>
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-1.5">
              <h6 class="text-sm font-bold text-[var(--text-card-title)]">Professional Significance</h6>
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)]" style="text-indent: 2rem;">In enterprise ITSM operations, reliable automated triage is critical for managing large volumes of end-user feedback. Learning how to properly scale dataset volume and diversity directly improves a neural network's predictive accuracy and reduces misclassification risks, ensuring that dynamic AI systems remain functional and robust in unpredictable real-world scenarios.</p>
            </div>
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-1.5">
              <h6 class="text-sm font-bold text-[var(--text-card-title)]">Learning Reflection</h6>
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)] italic font-medium" style="text-indent: 2rem;">&ldquo;This exercise provided hands-on exposure to both the strengths and vulnerabilities of neural networks. While I observed how scaling the training dataset significantly improved the model's ability to handle sarcasm, the most striking finding was how the model forcefully mapped completely unrepresented edge cases into existing categories with abnormally high confidence. This realization emphasized that deploying AI isn't just about training—it's about explicitly programming safeguards for when the model inevitably encounters unknown data.&rdquo;</p>
            </div>
          </div>
        </details>
      </article>
      </div>
"""

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

search_str = '''<div class="flex items-center justify-center p-12 text-[var(--text-card-muted)] text-sm font-mono">
          > Prelim content will be documented here soon...
        </div>'''
text = text.replace(search_str, html, 1)

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

