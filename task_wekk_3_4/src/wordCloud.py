from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    wordcloud = WordCloud(
        width=1000,
        height=500,
        background_color='white',
        max_words=200
    ).generate(text)
    return wordcloud
