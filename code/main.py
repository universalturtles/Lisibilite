import logging
import logging.config
import os
import nltk

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
    # Natural Language Toolkit: Punkt sentence tokenizer
    # Kiss, Tibor and Strunk, Jan (2006): Unsupervised Multilingual Sentence
    #    Boundary Detection.  Computational Linguistics 32: 485-525.
    # Ref: https://www.nltk.org/_modules/nltk/tokenize/punkt.html
    nltk.download('punkt')


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
    # arg_parser.processArgs()
    readabilityWithFile = Lisibilite("./resources/sample_text.txt")
    output = readabilityWithFile.getReadabilityMetrics()
    fw = FileWriter()
    fw.writeCsv(output, "./resources/sample_op.csv")
