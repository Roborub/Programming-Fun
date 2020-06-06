import praw
from pydash import py_ as _
from enum import Enum

class FILTER(Enum):
    HOT = 1,
    NEW = 2,
    CONTROVERSIAL = 3,
    TOP = 4,
    RISING = 5

class Bot:
    def __init__(self, name, subreddits = dict()):
        self.FILTER = FILTER
        self.bot = praw.Reddit(name)
        self.subreddits = dict()
        self.set_subreddits(subreddits)


    def set_subreddits(self, subreddit_list):
        self.subreddits = { s:self.bot.subreddit(s) for s in subreddit_list }

    def get_subreddit(self, subreddit_name):
        return self.subreddits.get(subreddit_name)

    def get_all_subreddits(self):
        return self.subreddits

    def get_comments(self, submission):
        return [ self.bot.comment(i) for i in submission.comments ] 

    def get_submissions(self, subreddit_str, filter = 1, limit = 25):
        subreddit = self.get_subreddit(subreddit_str)
        

        filters = {
            self.FILTER.HOT: subreddit.hot,
            self.FILTER.NEW: subreddit.new,
            self.FILTER.CONTROVERSIAL: subreddit.controversial,
            self.FILTER.TOP: subreddit.top,
            self.FILTER.RISING: subreddit.rising
        }

        submission_ids = filters.get(filter)(limit = limit)

        return [ self.bot.submission(i) for i in submission_ids ]