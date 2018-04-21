import praw, prawcore, re, time

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def connect_to_reddit():
    """
    Sign in to Reddit
    @return
    reddit: le reddoot
    """
    reddit = praw.Reddit(client_id = 'Ngjy2b_Gjedvew',
                         client_secret = 'kUbMmIc3KQ92CvcjVpHZbR647Nc',
                         username = 'teamBhackathon',
                         password = 'memes2017',
                         user_agent = 'happysubs app')
    
    
    return reddit
