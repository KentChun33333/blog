import logging 

class DebugLog(object):
	def __init__(self, name):
		#super(DebugLog, self)__init__()
		self.log = logging.getLogger(name)
		self.format = logging.Formatter('%(asctime)s, %(name)s'
			                            ',%(levelname)s, %(message)s')
		self.add_stream_log()
		#self.add_file_log()

	def add_stream_log(self):
		# if not hasattr('ch'):
		self.ch = logging.StreamHandler()
		# [Note] setLevel = ignore level
		self.ch.setLevel(logging.DEBUG)
		self.ch.setFormatter(self.format)
		self.log.addHandler(self.ch)

	def add_file_log(self, name):
		self.fh = logging.FileHandler(name)
		self.fh.setLevel(logging.DEBUG)
		self.fh.setFormatter(self.format)
		self.log.addHandler(self.fh)

	def warn(self,txt):
		return self.log.warn(txt)

	def info(self, txt):
		return self.log.info(txt)

	def critic(self, txt):
		return self.log.critic(txt)

if __name__ =='__main__':
	test = DebugLog('s')
	test.warn('OK')

# =============================================================== #
# [Note]                                                          #
# the default is anything or any kind of message would be logged  #
# but we could use setLevel as                                    #
# =============================================================== #
# [init]
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
# --------------------------------------------------------------- #
# [create file handler which logs even debug messages]
# fh = logging.FileHandler('spam.log')
# fh.setLevel(logging.DEBUG)
# --------------------------------------------------------------- #
# [create console handler with a higher log level]
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# --------------------------------------------------------------- #
# [create formatter and add it to the handlers]
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
# --------------------------------------------------------------- #
# [add the handlers to logger]
# logger.addHandler(ch)
# logger.addHandler(fh)
# --------------------------------------------------------------- #
# [Logger Level] 
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')
# --------------------------------------------------------------- #
