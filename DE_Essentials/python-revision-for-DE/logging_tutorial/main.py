import atexit
import json
import logging
import logging.config
import pathlib

logger = logging.getLogger(__name__)

def setup_logging():
    config_file = pathlib.Path("logging_configs/1-stderr-file.json")
    with open(config_file) as fp:
        config = json.load(fp)
    
    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


def main():
    logging_config = setup_logging()
    logging.basicConfig(level="INFO")
    # logging.config.dictConfig(config=logging_config)
    # logger.addHandler(logging.StreamHandler(...))
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")

if __name__ == "__main__":
    main()