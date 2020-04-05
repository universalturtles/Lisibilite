import os
import yaml
import logging
import logging.config

from config.AppConfiguration import LOG_DIR, LOG_CONFIG_FILE
from lisibilite.Lisibilite import Lisibilite


def init():
    """
    Method to init the application
    :return: None
    """
    configureLogging()
    logging.debug('Log configuration completed')


def configureLogging():
    """
    Method to configure the logging
    :return: None
    """
    try:
        logging.info('Setting up loggers')
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        logging.config.dictConfig(yaml.load(open(LOG_CONFIG_FILE), Loader=yaml.FullLoader))
        logging.debug('Loggers initialized')
    except Exception as e:
        logging.error(f"Error in the Log Configuration. Error = {e}")
        exit(1)


if __name__ == "__main__":
    init()
    readability = Lisibilite(filename="./resources/sample_text.txt")
    print(readability.computed)

