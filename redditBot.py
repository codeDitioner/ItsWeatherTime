# Reddit Bot that posts weather forecast for Seattle area in SeattleWeatherTime subreddit.
import praw
from itsWeatherTime import weather_today

def reddit_post(arg=None): # Cloud will not run without a default argument
    """
    Function posts to threads with today's weather information for Seattle.
    """
    # Initiate instance with "bot" profile from praw.ini file.
    reddit = praw.Reddit("bot")
    # Assign subreddit location
    submission = reddit.submission(url='https://www.reddit.com/r/SeattleWeatherTime/comments/wqbz04/daily_weather_updates/')
    submission.reply(body=weather_today('Seattle'))
