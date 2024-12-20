#-------------------------------------------VERSION 1------------------------------------------------------------
import logging

logging.debug("This is a simple message.")
logging.info("This is info.")
logging.warning("This is a warning.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

#------------------------------------------VERSION 2--------------------------------------------------------------
l = logging.getLogger("My Logger.")

l.debug("This is a simple message.")
l.info("This is info.")
l.warning("This is a warning.")
l.error("This is an error message.")
l.critical("This is a critical message.")

