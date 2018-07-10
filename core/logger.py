import logging
import logging.config


def getlog():
    log_filename = "D:/Jarvis' report.log"
    formatter = '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s'
    logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                        format=formatter,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(formatter))
    logging.getLogger('').addHandler(console)
    return logging
