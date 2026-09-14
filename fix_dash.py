def fix():
    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.replace("training—it's", "training, it's")
    text = text.replace("training—", "training, ")

    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(text)

fix()

