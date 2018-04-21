import sublime
import sublime_plugin
import time

class coolmathsgames(sublime_plugin.TextCommand):
	def run(self, edit):
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(edit, 0, contents + " memes")





