import logging
import logging.config
import os

import yaml
from arg_parser import ParseArguments as arg_parser
from config.AppConfiguration import LOG_CONFIG_FILE, LOG_DIR
from inputoutput.FileWriter import FileWriter
from lisibilite.Lisibilite import Lisibilite
from models.CoreMetrics import CoreMetrics
from models.OutputDataModel import OutputDataModel
from models.ReadabilityMetrics import ReadabilityMetrics


def init():
    """
    Method to init the application
    :return: None
    """
    configureLogging()
    logging.debug(f'{__name__} init')
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
        logging.config.dictConfig(
            yaml.load(
                open(LOG_CONFIG_FILE),
                Loader=yaml.FullLoader))
        logging.debug('Loggers initialized')
    except Exception as e:
        logging.error(f"Error in the Log Configuration. Error = {e}")
        exit(1)


if __name__ == "__main__":
    init()
    arg_parser.process_args()
    readabilityWithFile = Lisibilite("./resources/sample_text.txt")
    output = readabilityWithFile.getReadabilityMetrics()
    fw = FileWriter()
    fw.writeCsv(output, "./resources/sample_op.csv")
