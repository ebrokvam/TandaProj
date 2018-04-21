import sublime
import sublime_plugin
import time
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
    page = '';
    
    for i in range(0, 10):
        ascii_image = handle_image_conversion(urls[i])
        if ascii_image == None:
            ascii_image = "NO IMAGE"
        page += (titles[i] + '\n\n' + ascii_image + '\n\n') 
        
    return page
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class coolmathsgames(sublime_plugin.TextCommand):
	def run(self, edit):
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		file = open("contents.txt","w") 
		file.write(contents) 

		reddit = connect_to_reddit()

		sub = 'adviceanimals'

		titles = get_posts_names(reddit, sub)
		urls = get_posts_urls(reddit, sub)
		generate_page(titles, urls)

		self.view.insert(edit, 0, "Reddit" + generate_page(titles, urls))

class uncoolmathsgames(sublime_plugin.TextCommand):
	"""docstring for ClassName"""
	def run(self, edit):
		file = open("contents.txt", "r") 
		contents = file.read() 
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(edit, 0, contents)

		





