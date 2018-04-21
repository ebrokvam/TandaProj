import sublime
import sublime_plugin
import time

class coolmathsgames(sublime_plugin.TextCommand):
	def run(self, edit):
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		file = open("contents.txt","w") 
		file.write(contents) 

		self.view.insert(edit, 0, "i really enjoy memes")

class uncoolmathsgames(sublime_plugin.TextCommand):
	"""docstring for ClassName"""
	def run(self, edit):
		file = open("contents.txt", "r") 
		contents = file.read() 
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(edit, 0, contents)
		



		





