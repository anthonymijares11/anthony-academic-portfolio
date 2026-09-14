import re

def update():
    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    old_text = "Stepping into ITC-C508 carries a lot of weight for me. Balancing night shifts at a BPO helpdesk alongside my studies requires a strict focus on practicality. I want to learn tools that actually solve real problems. My core expectation for this course is to move beyond theoretical concepts and gain hands-on experience building neural networks capable of processing complex, unstructured data. In the fast-paced IT support industry, the ability to leverage Natural Language Processing to analyze user sentiment or deploy predictive models to anticipate customer churn would completely change how we handle service delivery. I am looking forward to bridging the gap between manual troubleshooting and automated, data-driven solutions."

    new_text = "Stepping into ITC-C508 carries a lot of weight for me. Having recently stepped away from my night shift role as a Tier 2 IT Helpdesk Analyst to focus entirely on my studies, my core expectation is to build a highly practical and competitive skill set before graduation. Rather than just understanding theoretical concepts, I want to gain strong intuition on how to adjust hyperparameters and fine-tune complex machine learning models. By bridging the gap between manual troubleshooting and automated data-driven solutions, mastering these deep learning frameworks will not only prepare me to advance into a Level 3 System Administrator role but, more importantly, it will build the technical foundation I need to jumpstart my career as an AI or Machine Learning Engineer once I finish my degree."

    text = text.replace(old_text, new_text)

    with open(r'C:\Users\antho\.gemini\antigravity\scratch\anthony-academic-portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(text)

update()
