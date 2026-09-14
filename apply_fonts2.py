import re
def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    google_fonts = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
"""
    if 'fonts.googleapis.com' not in text:
        text = text.replace('<title>', google_fonts + '  <title>')

    text = text.replace('font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;', "font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;")
    text = text.replace('font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;', "font-family: 'Newsreader', Georgia, serif;")
    text = text.replace('.font-mono {', '.font-serif {')
    text = text.replace('font-mono', 'font-serif')

    tw_old = """fontFamily: {
            sans: ['system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
            mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', '"Liberation Mono"', '"Courier New"', 'monospace'],
          }"""
    tw_new = """fontFamily: {
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
            serif: ['Newsreader', 'Georgia', 'serif'],
          }"""
    text = text.replace(tw_old, tw_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

update_file(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html')
update_file(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\consoles.html')
print('Updated to Inter and Newsreader')
