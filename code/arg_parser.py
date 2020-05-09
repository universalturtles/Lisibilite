import os
import yaml
import logging
import logging.config
import argparse

from lisibilite.Lisibilite import Lisibilite
from config.AppConfiguration import LOG_DIR, LOG_CONFIG_FILE


def init():
    """
    Method to init the application
    :return: None
    """
    configureLogging()
    logging.debug(f'{__name__} init')
    logging.debug('Log configuration completed')
    process()


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
        
def process():
    """
    Method to receive system arguments, parse them and pass on to Lisiblite processor
    Either an input file or text content is necessary along with output format and output file name
    :return: Writes to the output file in the given format
    """
    parser = argparse.ArgumentParser(description = 'Calculate readability of a text, either input text or file is required along with output filename and format. Input file will have precedence over text.')
    parser.add_argument('-in', '--input', help='The text on which processing would be done needs to be withing double quotes')
    parser.add_argument('-out_file', '--output_file', help='The name of the output file containting readability metrics', required=True)
    parser.add_argument('-in_file', '--input_file', help='The name of the input file on which processing would be done')
    parser.add_argument('-out_format', '--output_format', help='The format of the output file, default is CSV', default = 'csv')
    args = parser.parse_args()
    input_text = args.input
    input_file = args.input_file
    if input_file:
        if os.path.exists(input_file):
            logging.info(os.path.dirname(os.path.abspath(input_file)))
            readability = Lisibilite(input_file)
        else:
            raise Exception(f'Not a valid file path')
    elif input_text:
        readability = Lisibilite(contents = input_text)
    else:
        raise Exception(f'Either input file or text is necessary for computing readability')
    logging.info(readability.computed)

if __name__ == "__main__":
    init()

