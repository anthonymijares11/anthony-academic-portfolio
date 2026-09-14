import re

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_ref = '&ldquo;The best part of this exercise was actually watching the training and validation loss change epoch by epoch. Seeing how a small tweak, like dropping the learning rate to 0.001, caused the model to underfit, while raising it to 0.01 made the validation loss spike out of control, really helped me understand how weight updates work in practice. Running these 11 separate experiments showed me that building a good neural network isn\'t just about having more computing power, but about finding the right balance between the model\'s size, the data it learns from, and how well it is regularized.&rdquo;'

new_ref = '&ldquo;The best part of this exercise was actually watching the training and validation loss change epoch by epoch. Seeing how a small tweak, like dropping the learning rate to 0.001, caused the model to underfit, while raising it to 0.01 made the validation loss spike out of control, really helped me understand how weight updates work in practice. Running these 11 separate experiments showed me that building a good neural network isn\'t just about having more computing power, but about finding the right balance between the model\'s size, the data it learns from, and how well it is regularized. Although I was limited with my dataset, I didn\'t expect that just by using early stopping at 15 epochs I would already find the optimal value. Because it converged so quickly, adding more data to the dataset would be the next logical step to challenge the model and improve it even further.&rdquo;'

text = text.replace(old_ref, new_ref)

with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated successfully")

