import re
def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    new_google_fonts = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Roboto+Mono:wght@400;500;600&display=swap" rel="stylesheet">
"""
    # Replace old google fonts link block
    old_google_fonts = """  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n"""
    
    text = text.replace(old_google_fonts, new_google_fonts)

    text = text.replace("font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;", "font-family: 'Roboto', sans-serif;")
    text = text.replace("font-family: 'Newsreader', Georgia, serif;", "font-family: 'Roboto Mono', monospace;")
    text = text.replace('.font-serif {', '.font-mono {')
    text = text.replace('font-serif', 'font-mono')

    tw_old = """fontFamily: {
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
            serif: ['Newsreader', 'Georgia', 'serif'],
          }"""
    tw_new = """fontFamily: {
            sans: ['Roboto', 'sans-serif'],
            mono: ['Roboto Mono', 'monospace'],
          }"""
    text = text.replace(tw_old, tw_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

update_file(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html')
update_file(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\consoles.html')
print('Updated to Roboto')

