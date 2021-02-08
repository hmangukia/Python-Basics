# Author: zachRudz
# Source: https://docs.python.org/3/tutorial/stdlib2.html#logging

# Logging is important for debugging your code.
# While you COULD just put print() statements all over your program,
#	logging is the graceful way of printing errors, or debug information 
#	to the user or developer.
# Logs produced this way will either go to stderr (Standard error, not unlike standard output, to which you would print to via print()), or to a file.

# The first step is to import the logging module(part of the standard library)
# This way, we can access the functions and variables provided by the module
import logging

def main():
	# Logging has different levels of severity and verbosity (debug, info, warning, error, critical).
	# Think of it like DEFCON levels. 
	#	DEFCON 5 is low severity but happens more often (info)
	#	DEFCON 1 is high severity, but happens very infrequently (critical)
	
	# Logging works in such a way that the logger only prints messages
	#	that are above a specified severity.
	# So for example, if we were to set our logger's level to the warning level,
	#	then only messages of level warning and above (warnng, error, critical) will be printed.

	# We can setup the logger with the below command. Our output file is "./example.log".
	logging.basicConfig(filename="example.log", level=logging.WARNING)

	# Below are some examples of logging in action. Because our log level is warning, only the last 3 messages will be written to the log file.
	logging.debug('Debugging information')
	logging.info('Informational message')
	logging.warning('Warning:config file %s not found', 'server.conf')
	logging.error('Error occurred')
	logging.critical('Critical error -- shutting down')




# Call your main method like this
# The reason we do this is so that if you were to import this file from another python script (eg: $ import logging.py),
#	then it doesn't run all of the code in the script! If we just wrote all of our main method at the bottom of the script,
#	then our main method would run when you import the script to another file. Not ideal!
if __name__ == "__main__":
	main()
