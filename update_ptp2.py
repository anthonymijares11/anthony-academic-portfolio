import urllib.parse
html = """
      <!-- Activity 3: PT-P2 -->
      <article class="p-6 sm:p-7 rounded-2xl border border-[var(--border-card)] bg-[var(--bg-card)] space-y-4 shadow-[var(--shadow-card)] transition-all duration-200">
        <h4 class="text-lg sm:text-xl font-bold text-[var(--text-card-title)] tracking-tight">
          Performance Task 2: Systematic Hyperparameter Optimization
        </h4>

        <!-- Main PDF -->
        <div class="my-3 p-3.5 sm:p-4 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex flex-wrap items-center justify-between gap-3 transition-colors duration-150">
          <div class="flex items-center gap-2.5 min-w-0 max-w-xl">
            <span class="p-2 rounded-lg bg-[var(--bg-card)] border border-[var(--border-well)] flex items-center justify-center shrink-0">
              <svg class="w-4 h-4 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            </span>
            <div class="min-w-0">
              <span class="text-xs sm:text-[13px] font-semibold text-[var(--text-card-title)] block leading-snug truncate sm:whitespace-normal">
                Research Paper: Systematic Hyperparameter Optimization of a Sequential Neural Network
              </span>
            </div>
          </div>
          <div class="flex items-center gap-2 shrink-0">
            <button onclick="openAssetModal('assets/docs/itc508/Mijares_Anthony_IEEE_Report (2).pdf', 'PT-P2: Hyperparameter Optimization', 'pdf')" class="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-lg bg-[var(--bg-card)] border border-[var(--border-well)] text-[var(--text-card-title)] hover:opacity-80 transition font-medium cursor-pointer shadow-xs">
              <svg class="w-3.5 h-3.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path><polyline points="10 17 15 12 10 7"></polyline><line x1="15" y1="12" x2="3" y2="12"></line></svg>
              <span>View PDF</span>
            </button>
          </div>
        </div>

        <!-- Notebook & Excel -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div class="p-3 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex items-center justify-between gap-2">
            <div class="flex items-center gap-2 min-w-0">
              <svg class="w-3.5 h-3.5 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span class="text-xs font-semibold text-[var(--text-card-title)] truncate">Jupyter Notebook File</span>
            </div>
            <a href="assets/notebooks/itc508/Mijares_Anthony_Neural_Network_Training_Testing.ipynb" download class="text-[11px] font-medium text-[var(--text-page)] hover:underline whitespace-nowrap">Download .ipynb</a>
          </div>
          <div class="p-3 rounded-xl border border-[var(--border-well)] bg-[var(--bg-well)] flex items-center justify-between gap-2">
            <div class="flex items-center gap-2 min-w-0">
              <svg class="w-3.5 h-3.5 shrink-0 text-[var(--text-card-muted)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span class="text-xs font-semibold text-[var(--text-card-title)] truncate">FFBP Training Log (Excel)</span>
            </div>
            <a href="assets/docs/itc508/Mijares_Anthony_FFBP_Training_Log_Template (1).xlsx" download class="text-[11px] font-medium text-[var(--text-page)] hover:underline whitespace-nowrap">Download</a>
          </div>
        </div>

        <div class="space-y-1.5 pt-1">
          <h5 class="text-sm sm:text-base font-bold text-[var(--text-card-title)]">Description</h5>
          <p class="text-sm leading-relaxed text-[var(--text-card-body)] font-normal" style="text-indent: 2rem;">This study transitions from no-code platforms to an interactive Python-based Keras environment. The objective was to systematically optimize a sequential neural network designed for ITSM ticket classification. Using a One-Factor-At-A-Time strategy, learning rates, architectural capacity constraints, and batch sizes were evaluated across eleven distinct experimental configurations to identify the optimal model architecture and maximize validation accuracy.</p>
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
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)]" style="text-indent: 2rem;">Developed a sequential neural network in Python utilizing TensorFlow and Keras, incorporating embedding layers, global average pooling, and dropout regularization. Executed a systematic hyperparameter tuning process evaluating convergence behavior across 11 experiments by diagnosing model fit via sparse categorical cross-entropy loss curves, discovering that a 128 hidden dimension with a 0.005 learning rate and 0.1 dropout yielded the peak F1-score of 0.8898.</p>
            </div>
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-1.5">
              <h6 class="text-sm font-bold text-[var(--text-card-title)]">Professional Significance</h6>
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)]" style="text-indent: 2rem;">Transitioning from automated heuristics to explicit code-based optimization provides granular control over a network's learning trajectory. In professional AI engineering, knowing how to balance core network capacity with convergence stability prevents rote memorization (overfitting) and ensures high-quality generalization for automated triage architectures.</p>
            </div>
            <div class="p-4 rounded-xl bg-[var(--bg-well)] border border-[var(--border-well)] space-y-1.5">
              <h6 class="text-sm font-bold text-[var(--text-card-title)]">Learning Reflection</h6>
              <p class="text-xs sm:text-[13px] leading-relaxed text-[var(--text-card-body)] italic font-medium" style="text-indent: 2rem;">&ldquo;By far the most rewarding part of this exercise was actively tracking the interaction between training loss and validation loss across the epochs. Seeing how a simple adjustment, like decreasing the learning rate to 0.001, caused immediate underfitting, while increasing it to 0.01 triggered pronounced divergence, really solidified my understanding of gradient updates. It proved that successful neural networks require a delicate equilibrium between architectural capacity and regularization.&rdquo;</p>
            </div>
          </div>
        </details>
      </article>\n      </div>"""

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add to prelim section
start = text.find('id="itc508ContentPrelim"')
end_div = text.find('</div>', text.rfind('</article>', start, text.find('id="itc508ContentMidterm"', start)))
if end_div == -1:
    end_div = text.find('</div>\n\n      <!-- Midterm Period Tab -->', start)

text = text[:end_div] + html + text[end_div+6:]

# Hide Midterm and Final buttons for ITC508
text = text.replace('id="itc508TabMidterm" class="', 'id="itc508TabMidterm" class="hidden ')
text = text.replace('id="itc508TabFinal" class="', 'id="itc508TabFinal" class="hidden ')

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

