import re
def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace("title.textContent = 'ITC-C506: IT Elective 3 (Archive)';", "title.textContent = 'ITC-C506: IT Elective 3';")
    text = text.replace("title.textContent = 'EMC C102: Human-Computer Interaction (Archive)';", "title.textContent = 'EMC C102: Human-Computer Interaction';")
    
    text = text.replace('<h2 id="activeWorkspaceTitle" class="text-lg sm:text-xl font-bold text-[var(--text-page)]">', '<h2 id="activeWorkspaceTitle" class="text-lg sm:text-xl font-bold text-[var(--text-page)] truncate">')
    text = text.replace('<div class="flex flex-wrap items-center justify-between gap-4 p-5 sm:p-6 rounded-2xl border border-[var(--border-card)] bg-[var(--bg-card)] shadow-[var(--shadow-card)]">\n      <div>', '<div class="flex flex-wrap items-center justify-between gap-4 p-5 sm:p-6 rounded-2xl border border-[var(--border-card)] bg-[var(--bg-card)] shadow-[var(--shadow-card)]">\n      <div class="min-w-0 flex-1">')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

update_file(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html')
print('Fixed!')

