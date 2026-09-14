import re

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_prof = "Learning how to balance the network's capacity with its stability is key to preventing overfitting and ensuring the model makes accurate predictions in production."
new_prof = "Learning how to properly tune these settings is key to preventing the model from just memorizing the training data (overfitting), ensuring it actually makes accurate predictions when deployed in production."

text = text.replace(old_prof, new_prof)

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated successfully")
