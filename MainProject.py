import streamlit as st
from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import urlopen
from newspaper import Article
import io

def GetNews(url):
    op = urlopen(url)
    rd = op.read()
    op.close()
    soup_page = BeautifulSoup(rd, 'xml')
    return soup_page.find_all('item')

def GetNewsImage(poster_link):
    try:
        response = urlopen(poster_link)
        image = Image.open(io.BytesIO(response.read()))
        st.image(image, use_column_width=True)
    except:
        print("No image found!")

def GetSearchNews(topic):
    site = 'https://news.google.com/rss/search?q={}'.format(topic)
    op = urlopen(site)
    rd = op.read()
    op.close()
    sp_page = BeautifulSoup(rd, 'xml')
    news_list = sp_page.find_all('item')
    return news_list

def NewsDisplay(news_list, news_quantity):
    for news in news_list[:news_quantity]:
        st.markdown(f"<h2 style='font-size:26px'>{news.title.text}</h2>", unsafe_allow_html=True)
        news_data = Article(news.link.text)
        try:
            news_data.download()
            news_data.parse()
            news_data.nlp()
        except Exception as e:
            st.error(e)
        GetNewsImage(news_data.top_image)
        st.markdown(news_data.summary)

def run():
    st.title("News Summarizer")

    st.sidebar.header("Choose Category")
    topics = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'SPORTS', 'SCIENCE', 'HEALTH']
    chosen_topic = st.sidebar.selectbox("Select Category:", topics)

    st.sidebar.header("Search News")
    user_topic = st.sidebar.text_input("Enter Topic:")
    if st.sidebar.button("Search") and user_topic.strip() != '':
        news_list = GetSearchNews(topic=user_topic)
        if news_list:
            NewsDisplay(news_list, 25)
        else:
            st.error("No News found for {}".format(user_topic))

    if chosen_topic:
        news_list = GetNews(f'https://news.google.com/news/rss/headlines/section/topic/{chosen_topic}')
        if news_list:
            NewsDisplay(news_list, 25)
        else:
            st.warning("No news found")

run()