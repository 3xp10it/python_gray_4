from pydbg import *
from pydbg.defines import *
import threading
import sys
import time
class snapshotter(object):
	def __init__(self,exe_path):
		self.pid=None
		self.dbg=None
		self.exe_path=exe_path
		self.running=True
		pydbg_thread=threading.Thread(target=self.start_debugger)
		pydbg_thread.setDaemon(0)
		pydbg_thread.start()
		while self.pid==None:
			time.sleep(1)
		monitor_thread=threading.Thread(target=self.monitor_debugger)
		monitor_thread.setDaemon(0)
		monitor_thread.start()

	def monitor_debugger(self):
		while self.running==True:
			input=raw_input("enter:'snap','restore',or 'quit' ")
			input=input.lower().strip()
			if input=="quit":
				print "exiting the snapshotter."
				self.running=False
				self.dbg.terminate_process()
			elif input=="snap":
				print "suspending all threads."
				self.dbg.suspend_all_threads()
				print "obtain snapshot."
				self.dbg.process_snapshot()
				print "resuming operation."
				self.dbg.resume_all_threads()
			elif input=="restore":
				print "suspending all threads"
				self.dbg.suspend_all_threads()
				print "restoreing snapshot"
				self.dbg.process_restore()
				print "resuming operation"
				self.dbg.resume_all_threads()
	def start_debugger(self):
		self.dbg=pydbg()
		pid=self.dbg.load(exe_path)
		self.pid=self.dbg.pid
		self.dbg.run()

exe_path="c:\\windows\\system32\\notepad.exe"
snapshotter(exe_path)

