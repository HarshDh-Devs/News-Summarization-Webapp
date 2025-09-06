import streamlit as st
from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import urlopen
from newspaper import Article
import io

def fetch_news(url):
    op = urlopen(url)
    rd = op.read()
    op.close()
    soup_page = BeautifulSoup(rd, 'xml')
    return soup_page.find_all('item')

def fetch_news_poster(poster_link):
    try:
        response = urlopen(poster_link)
        image = Image.open(io.BytesIO(response.read()))
        st.image(image, use_column_width=True)
    except:
        print("No image found!")

def display_news(news_list, news_quantity):
    for news in news_list[:news_quantity]:
        st.write(f"**{news.title.text}**")
        news_data = Article(news.link.text)
        try:
            news_data.download()
            news_data.parse()
            news_data.nlp()
        except Exception as e:
            st.error(e)
        fetch_news_poster(news_data.top_image)
        st.markdown(news_data.summary)

def run():
    st.title("News Summarizer")

    category = ['Trending', 'Favourite']
    cat_op = st.selectbox('Select your Category', category)

    if cat_op == category[0]:
        st.subheader("✅ Here is the Trending news for you")
        news_list = fetch_news('https://news.google.com/news/rss')
        display_news(news_list, 2)  # Default 25 news

    elif cat_op == category[1]:
        topics = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'SPORTS', 'SCIENCE', 'HEALTH']
        chosen_topic = st.selectbox("Choose your favourite Topic", topics)
        if chosen_topic:
            news_list = fetch_news(f'https://news.google.com/news/rss/headlines/section/topic/{chosen_topic}')
            if news_list:
                st.subheader(f"✅ Here are the some {chosen_topic} News for you")
                display_news(news_list, 2)  # Default 25 news
            else:
                print("No news found")

run()