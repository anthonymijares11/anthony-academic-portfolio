# Anthony Mijares: Academic E-Portfolio

A high-performance, responsive academic e-portfolio built for **Jose Rizal University (JRU)**, College of Information Technology.

* **Author:** Anthony Mijares (4th Year BSIT Senior Student & Returnee &amp; Tier 2 IT Helpdesk Support Analyst)
* **Active Course:** ITC-C508: IT Elective 4 (Advanced Machine Learning &amp; Deep Learning)
* **Archived Coursework:** ITC-C506: IT Elective 3 (Predictive Analytics)
* **External Design Portfolio:** EMC C102: Human-Computer Interaction (Wix Redirect)

---

## Architecture and Structure

```
anthony-academic-portfolio/
├── index.html              # Main single-page academic e-portfolio
├── 404.html                # Custom error page
├── _redirects              # Cloudflare Pages redirect engine (/emc -> Wix)
├── _headers                # Security and caching headers
├── robots.txt              # Search engine directives
├── .gitignore              # Standard git ignore file
├── README.md               # Project documentation and setup guide
└── assets/
    ├── anthony_photo.jpg   # Profile photograph
    ├── docs/               # 10 Academic PDFs (Research Papers, Quizzes, Exams)
    │   ├── prelim_ex1_knn_paper.pdf
    │   ├── prelim_ex2_cleaning_paper.pdf
    │   ├── prelim_ex3_regression_paper.pdf
    │   ├── prelim_long_quiz.pdf
    │   ├── prelim_exam.pdf
    │   ├── midterm_ex1_logistic_paper.pdf
    │   ├── midterm_long_quiz.pdf
    │   ├── midterm_exam.pdf
    │   ├── final_ex1_fine_tuning_paper.pdf
    │   └── final_project_euphoria_paper.pdf
    └── notebooks/          # 6 Executable HTML Notebooks (Python / Google Colab)
        ├── prelim_ex1_knn_code.html
        ├── prelim_ex2_cleaning_code.html
        ├── prelim_ex3_regression_code.html
        ├── midterm_ex1_logistic_code.html
        ├── final_ex1_finetuning_code.html
        └── final_project_euphoria_code.html
```

---

## Features

1. **Coursework Organization:**
   * **ITC-C508 (Active Workspace):** Complete responses and deep learning architecture designs for Exercise #WW-P1 (Predictive failure modeling, Explainable AI / SHAP, and real-time NLP systems).
   * **ITC-C506 (Archived Course):** Chronological coursework featuring Course Introduction and Expectations, Prelim Period (5 submissions), Midterm Period (3 submissions), and Final Period (3 submissions).
   * **EMC C102 (HCI Archive):** Integrated overview with native edge redirect to the live external Wix portfolio.
2. **Embedded Academic Artifacts:**
   * Embedded PDF document viewers with fullscreen viewing and direct download capabilities.
   * Embedded executable Google Colab / Jupyter notebook outputs.
3. **Editorial Design:**
   * Clean typography pairing Newsreader (editorial serif) and Inter (sans-serif).
   * Dark and Light theme toggle with preference persistence in localStorage.
   * 100% self-contained: works offline and does not require a database or backend server.

---

## Local Development

You can run this project locally without any dependencies:

### Option 1: Direct File
Simply double-click `index.html` to view it in any modern browser.

### Option 2: Python Local Server
```bash
# In the repository root directory:
python -m http.server 8000
```
Then visit `http://localhost:8000` in your web browser.

---

## Uploading to GitHub

To publish this project to your GitHub account:

1. Create a new empty repository on [GitHub](https://github.com/new) (e.g., named `academic-eportfolio`).
2. Open your terminal in this repository folder:
```bash
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME>.git
git branch -M main
git push -u origin main
```

---

## Free Deployment to Cloudflare Pages (via Git)

Once pushed to GitHub, you can connect your repository to Cloudflare Pages for automatic deployments:

1. Log in to the [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Navigate to **Workers &amp; Pages** &rarr; **Create application** &rarr; **Pages** &rarr; **Connect to Git**.
3. Select your GitHub repository (`academic-eportfolio`).
4. Set **Build configuration**:
   * **Framework preset:** `None`
   * **Build command:** *(leave empty)*
   * **Build output directory:** `.` (or root directory)
5. Click **Save and Deploy**.
6. Cloudflare will automatically build and deploy your site to a free global HTTPS subdomain (e.g., `https://academic-eportfolio.pages.dev`). Every future `git push` will deploy automatically!

---

## License

Academic coursework and intellectual property of Anthony Mijares, Jose Rizal University.
