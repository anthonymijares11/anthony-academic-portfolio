import re
def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove Google Fonts
    text = re.sub(r'  <link rel="preconnect" href="https://fonts\.googleapis\.com">\n', '', text)
    text = re.sub(r'  <link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\n', '', text)
    text = re.sub(r'  <link href="https://fonts\.googleapis\.com.*?rel="stylesheet">\n', '', text)

    # Replace font families
    text = text.replace("font-family: 'Roboto', sans-serif;", 'font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;')
    
    # Tailwind config update
    tw_old = """fontFamily: {
            sans: ['Roboto', 'sans-serif'],
            mono: ['Roboto', 'sans-serif'],
          }"""
    tw_new = """fontFamily: {
            sans: ['system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
            mono: ['system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
          }"""
    text = text.replace(tw_old, tw_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

update_file(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html')
update_file(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\consoles.html')
print('Updated to System UI')

