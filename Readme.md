# 📰 Google News Streamlit App

A Streamlit app that fetches Google News articles via RSS, parses and summarizes them with NLP, and displays them with images in multiple UI variants.

---

## ✨ Features
- **Fetch by mode**: Trending, Categories (WORLD, BUSINESS, TECHNOLOGY, etc.), and free-text Search via Google News RSS.  
- **Auto-summary**: Pulls article content with [Newspaper3k](https://github.com/codelucas/newspaper) and produces concise summaries after parsing and NLP.  
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
