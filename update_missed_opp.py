import re

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_str = "Because it converged so quickly, adding more data to the dataset would be the next logical step to challenge the model and improve it even further.&rdquo;"
new_str = "Looking back, because the model converged so quickly, I realize that not adding more data was a missed opportunity. Without a larger dataset to truly challenge the model, the scope of my experimentation ended up being fairly basic, which is a valuable lesson I'll definitely carry forward into my next projects.&rdquo;"

text = text.replace(old_str, new_str)

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated successfully")

