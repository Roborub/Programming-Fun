from reddit_bot_core import Bot
import re

subreddit_list = [
    "bennettisascrub"
]

test_bot = Bot('TEST', subreddit_list)

submissions = test_bot.get_submissions(subreddit_list[0], test_bot.FILTER.HOT)

for submission in submissions:
    for comment in test_bot.get_comments(submission):
        if (re.match(r".*test_bot.*", comment.body, re.IGNORECASE | re.MULTILINE)):
            comment.reply("Hey, " + comment.author.name + " how are you?")