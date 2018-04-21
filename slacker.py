import sublime
import sublime_plugin
from reddit import generate_page
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class coolmathsgames(sublime_plugin.TextCommand):
	def run(self, edit):
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		file = open("contents.txt","w") 
		file.write(contents) 

		page = generate_page()

		self.view.insert(edit, 0, page)

class uncoolmathsgames(sublime_plugin.TextCommand):
	"""docstring for ClassName"""
	def run(self, edit):
		file = open("contents.txt", "r") 
		contents = file.read() 
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(edit, 0, contents)

		





