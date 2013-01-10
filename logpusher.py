
import wx

from ConfigParser import SafeConfigParser
from ftplib import FTP

def loadconfig():
	parser = SafeConfigParser()
	filename = parser.read('logpusher.ini')
	
	if filename == []:
		# file could not be loaded
		print "Config file not found"
	
	for section_name in parser.sections():
		print 'Section: ', section_name
		print '   Options: ', parser.options(section_name)
		for name, value in parser.items(section_name):
			print '    %s = %s' % (name, value)
		print

def rot13(s):
	t = ''
	for ch in s:
		if not ch.isalpha():
			t = t + ch
		else:
			ch_low = ch.lower()
			if ch_low <= 'm':
				d = 13
			else:
				d = -13
			t = t + chr(ord(ch) + d)
	return t

	
class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(200,200))
		
		# Stuff that will be pulled in from the ini file.
		self.server = ''
		self.user   = ''
		self.passwd = ''
		self.script = ''
		
		
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.CreateStatusBar()
		
		filemenu = wx.Menu()
		
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
		menuLoadConfig = filemenu.Append(wx.ID_ANY, "&Load Config", " Reload config ini file")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate this program")
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)
		
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnLoadConfig, menuLoadConfig)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Show(True)
	
	def OnLoadConfig(self, e):
		print "Loading conifg."
	
	def OnAbout(self, e):
		dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor")
		dlg.ShowModal()
		dlg.Destroy()
	
	def OnExit(self, e):
		self.Close(True)

		
		
if __name__ == '__main__':
	app = wx.App(False)
	frame = MainWindow(None, "Sample Editor")
	app.MainLoop()

	print "logpusher\n"
	loadconfig()
	print rot13('b@alk#$%^')
	print rot13('onyx')