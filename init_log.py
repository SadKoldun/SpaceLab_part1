import logging


def init_log():
    logging.basicConfig(
        format='%(asctime)s  %(message)s', level=logging.INFO, datefmt='%H:%M:%S'
    )