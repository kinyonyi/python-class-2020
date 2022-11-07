import logging
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
logging.basicConfig(filename="mylog.txt", filemode="a", level=0)
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.info("This is an information log")
logging.error("This is an error message")
logging.debug("This is a debug")
logging.critical("There is a likelyhood of fire outbreak")
logging.warning("this is a warning")