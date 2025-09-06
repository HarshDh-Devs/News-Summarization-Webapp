# 📰 Google News Streamlit App

A simple Streamlit app that fetches Google News RSS feeds by trending, category, or search query, and generates short summaries and top images using Newspaper3k.  
Includes variants of the UI (tabs/sidebar) across multiple scripts for experimentation.

---

## ✨ Features
- **Fetch by mode**: Trending, Categories (WORLD, BUSINESS, TECHNOLOGY, etc.), and free-text Search via Google News RSS.  
- **Auto-summary**: Pulls article content with Newspaper3k and produces concise summaries after parsing and NLP.  
- **Top image preview**: Attempts to render the article’s top image; falls back to a local placeholder if not present (first script).  
- **Streamlit UI**: Multiple layout variants (centered columns, minimal, and sidebar) implemented in separate files.  

---

## 🛠️ Tech stack
- [Streamlit](https://streamlit.io) for the UI  
- [Newspaper3k](https://github.com/codelucas/newspaper) for article parsing, metadata extraction, and summaries (uses NLTK’s punkt tokenizer)  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for RSS parsing of Google News feeds  
- [Pillow (PIL)](https://python-pillow.org/) for image handling  

---

## 📂 Project structure

*(Adjust file names to match your repository files.)*

---

## 🚀 Getting started

### ✅ Prerequisites
- Python **3.9+** recommended  
- Install system build tools if required by Newspaper3k (`lxml`, `libxml2`, `libxslt` on some OSes)  
- Some sites may require a custom user agent and timeouts for Newspaper3k to download reliably  

### ⚙️ Installation
bash
git clone <your-repo-url>
cd <your-repo-folder>

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -U pip
pip install streamlit newspaper3k beautifulsoup4 pillow lxml

python -c "import nltk; nltk.download('punkt')"

# ▶️ Run

Run any of the app variants:

streamlit run main_app.py
# or
streamlit run simple_app.py
# or
streamlit run minimal_category_app.py
# or
streamlit run sidebar_app.py

# 💡 Usage

Trending: Loads top stories from Google News RSS
 and lists items with summaries and images when available.

Categories: Select from WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH; the app fetches the corresponding topic feed and summarizes articles.

Search: Enter a query; the app requests Google News search RSS and summarizes results.

Expander & styles:

Main app shows each item with an expander revealing the summary and “Read more” link.

Some variants use styled headings via st.markdown.

# ⚙️ Configuration

User agent/timeouts: If some domains block Newspaper3k, configure Article with a custom Config user agent and request_timeout.

Image fallback: Ensure Meta/no_image.jpg exists if using the first script’s fallback path; update the path if needed.

Limits: Sliders in the main script control how many items to display per mode.
