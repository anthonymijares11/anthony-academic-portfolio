# Anthony Mijares: Academic E-Portfolio

A responsive academic e-portfolio built for **Jose Rizal University (JRU)**, College of Information Technology.

* **Live Site:** https://anthonymijares11.github.io/anthony-academic-portfolio
* **Author:** Anthony Mijares (4th Year BSIT Senior Student & Returnee & Tier 2 IT Helpdesk Support Analyst)
* **Active Course:** ITC-C508: IT Elective 4 (Advanced Machine Learning & Deep Learning)
* **Archived Coursework:** ITC-C506: IT Elective 3 (Predictive Analytics)
* **External Design Portfolio:** EMC C102: Human-Computer Interaction (Wix Portfolio)

---

## Architecture and Structure

```text
anthony-academic-portfolio/
├── index.html              # Main single-page academic e-portfolio
├── 404.html                # Custom error page
├── _redirects              # Cloudflare Pages redirect rules (/emc -> Wix)
├── _headers                # Security and caching headers
├── .nojekyll               # GitHub Pages static asset directive
├── .gitattributes          # Repository language classification rules
├── .gitignore              # Git ignore rules
├── robots.txt              # Search engine directives
├── README.md               # Project documentation
└── assets/
    ├── anthony_photo.jpg   # Profile photograph
    ├── favicon.svg         # Site icon
    ├── docs/               # Academic PDFs, workbooks, and datasets (ITC-C506 & ITC-C508)
    ├── notebooks/          # Executable HTML & Jupyter notebooks (ITC-C506 & ITC-C508)
    └── thumbs/             # Document and project preview thumbnails
```

---

## Features

1. **Coursework Organization:**
   * **ITC-C508 (Active Course):** Course Introduction, Prelim Period, Midterm Period, and Final Period (including the BenepiKnow multilingual RAG chatbot capstone project, chunking & hyperparameter experiments, neural network training logs, and IEEE reports).
   * **ITC-C506 (Archived Course):** Course Introduction, Prelim Period, Midterm Period, and Final Period submissions, research papers, exams, and Project EUPHORIA.
   * **EMC C102 (HCI Archive):** Overview and direct link to the external Wix portfolio.
2. **Embedded Academic Artifacts:**
   * Built-in modal viewer for PDF documents and HTML notebooks with full-tab preview and direct file downloads.
3. **Theme & Interface:**
   * Light and Dark mode toggle with `localStorage` persistence and ambient background toggle.
   * Self-contained static architecture compatible with GitHub Pages and Cloudflare Pages.

---

## Local Development

### Option 1: Direct File
Open `index.html` directly in any modern browser.

### Option 2: Python Local Server
```bash
python -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

---

## License

Academic coursework and intellectual property of Anthony Mijares, Jose Rizal University.
