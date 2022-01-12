import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5049477338:AAF8ueuyjjF9twKNzorS-I0O0HJpmWP_EzU")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","796381e7-c2b2-472a-b62f-2b0aa51a8c16")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split("1191266989")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","herokumanager")
