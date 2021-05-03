import logging

LOG_FORMAT = '[%(asctime)s] [%(levelname)s] %(message)s'

def init(logfile="common.log", level=logging.DEBUG):
    logging.basicConfig(filename=logfile, format=LOG_FORMAT, filemode='a', level=level)
