import telebot
import feedparser

bot_token = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
channel_id = '@YOUR_TELEGRAM_CHANNEL_NAME_HERE'
search_word = 'peace'

bot = telebot.TeleBot(token=bot_token)

def send_matching_news():
    feed = feedparser.parse("YOUR_RSS_FEED_URL_HERE")

    for entry in feed.entries:
        if search_word in entry.title.lower() or search_word in entry.summary.lower():
            # If the search word is found in the title or summary, forward the news article to the designated channel
            title = entry.title
            summary = entry.summary
            link = entry.link
            message = f"{title}\n{summary}\n{link}"
            bot.send_message(channel_id, message)

