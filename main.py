import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler

def get_news(topic):
    url = f"https://news.google.com/search?q={topic}&hl=en-US&gl=US&ceid=US:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("a", class_="DY5T1d")
    return articles

def news(update, context):
    topic = " ".join(context.args)
    if not topic:
        update.message.reply_text("Please provide a topic for the news.")
        return
    articles = get_news(topic)
    for article in articles:
        update.message.reply_text(article.text + "\n" + "Link: " + article["href"])

def main():
    # Your Telegram token
    updater = Updater("YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("news", news))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
