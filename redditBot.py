# Reddit Bot that posts weather forecast for Seattle area.
import praw
from itsWeatherTime import weather_today

reddit = praw.Reddit("bot")
subreddit = reddit.subreddit('SeattleWeatherTime')
for submission in subreddit.new():
    submission.reply(body=weather_today('Seattle'))