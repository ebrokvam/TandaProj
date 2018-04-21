import praw, prawcore
from ascii_image import handle_image_conversion

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def connect_to_reddit():
    """
    Sign in to Reddit
    @return
    reddit: le reddoot
    """
    print('Connecting...')
    reddit = praw.Reddit(client_id = 'Ngjy2b_Gjedvew',
                         client_secret = 'kUbMmIc3KQ92CvcjVpHZbR647Nc',
                         username = 'teamBhackathon',
                         password = 'memes2017',
                         user_agent = 'happysubs app')
    
    print('All good mates')
    return reddit


def get_posts_names(reddit, sub):
    """
    Get the names of the posts in the specified subreddit
    reddit: reddit object
    sub: subreddit name
    """
    titles = []
    source = reddit.subreddit(sub)
    for submission in source.hot(limit=10):
        titles.append(submission.title)
    
    return titles

def get_posts_urls(reddit, sub):
    """
    Get the names of the posts in the specified subreddit
    reddit: reddit object
    sub: subreddit name
    """
    urls = []
    source = reddit.subreddit(sub)
    for submission in source.hot(limit=10):
        urls.append(submission.url)
    
    return urls

def generate_page(titles, urls):
    reddit = connect_to_reddit()
    sub = 'memes'
    titles = get_posts_names(reddit, sub)
    urls = get_posts_urls(reddit, sub)
    
    page = '';
    
    for i in range(0, 10):
        ascii_image = handle_image_conversion(urls[i])
        if ascii_image == None:
            ascii_image = "NO IMAGE"
        page += (titles[i] + '\n\n' + ascii_image + '\n\n') 
        
    return page


    
