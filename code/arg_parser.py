import os
import argparse
import logging
        
def process():
    """
    Method to receive system arguments, parse them and pass on to Lisiblite processor
    Either an input file or text content is necessary along with output format and output file name
    :return: The argument values
    """
    parser = argparse.ArgumentParser(description = 'Calculate readability of a text, either input text or file is required along with output filename and format. Input file will have precedence over text.')
    parser.add_argument('-t', '--text', help='The text on which processing would be done needs to be withing double quotes')
    parser.add_argument('-o', '--output-file', help='The name of the output file containting readability metrics', required=True)
    parser.add_argument('-i', '--input-file', help='The name of the input file on which processing would be done')
    parser.add_argument('-f', '--format', help='The format of the output file, default is CSV', default = 'csv')
    args = parser.parse_args()
    input_text = args.text
    input_file = args.input_file
    output_file = args.output_file
    output_format = args.format
    if input_file:
        if not os.path.exists(input_file):
            logging.error(os.path.abspath(input_file))
            raise Exception(f'Not a valid file path')
        logging.info(os.path.abspath(input_file))
    elif input_text:
        logging.info(input_text)
    else:
        raise Exception(f'Either input file or text is necessary for computing readability')
    return input_text,input_file,output_file,output_format

if __name__ == "__main__":
    process()