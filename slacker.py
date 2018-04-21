import sublime
import sublime_plugin
import time
from reddit import generate_page
    
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

		





