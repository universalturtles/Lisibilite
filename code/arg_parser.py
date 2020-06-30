import argparse
import logging
from customexceptions.ReadabilityErrors import ArgumentParsingError
from config.AppConfiguration import DEFAULT_OUTPUT_FILE_NAME
from pathlib import Path,PurePath
    
class ParseArguments:    
    def processArgs() -> dict:
        """
        Method to receive system arguments, parse them and pass on to Lisiblite processor
        Either an input file or text content is necessary along with output format and output file name
        :return: The argument values in a dictonary
        """
        parser = argparse.ArgumentParser(description = 'Calculate readability of a text, either input text or file is required along with output filename and format. Input file will have precedence over text.')
        parser.add_argument('-t', '--text', help='The text on which processing would be done needs to be withing double quotes')
        parser.add_argument('-o', '--output-file', help='The name of the output file containing readability metrics', required=True)
        parser.add_argument('-i', '--input-file', help='The name of the input file on which processing would be done' , type=argparse.FileType('r'))
        parser.add_argument('-f', '--format', help='The format of the output file, default is CSV',choices =['pdf','csv'], default = 'csv')
        args = parser.parse_args()
        inputText = args.text
        inputFile = args.input_file
        outputFile = args.output_file
        outputFormat = '.' + args.format
        outputFile = ParseArguments.validateArgs(inputFile,inputText,outputFile,outputFormat)
        print(outputFile)
        return dict(text = inputText, file = inputFile, output = outputFile, format = outputFormat)
    
        """
        Method to validate all system arguments
        :return: The output file name
        """
    def validateArgs(inputFile,inputText,outputFile,outputFormat):
        if not inputFile:
            if not inputText:
                raise ArgumentParsingError(f'Either input file or text is necessary for computing readability')
            elif not len(inputText) > 500:
                logging.debug(inputText)
                raise ArgumentParsingError(f'Input text length has to be minimum 500 for computing readability')
            else:
                logging.debug(inputText)
                logging.info(f'Using input text')
        else:
            logging.info(f'Using input file {inputFile}')
        try:
            if not Path(outputFile).suffix:
                Path(outputFile).mkdir(parents=True, exist_ok=True)
                outputFile = Path(outputFile,DEFAULT_OUTPUT_FILE_NAME).with_suffix(outputFormat)
            else:
                outPath = PurePath(outputFile)
                Path(outPath.parent).mkdir(parents=True, exist_ok=True)
                outputFile = Path(outPath.parent,DEFAULT_OUTPUT_FILE_NAME).with_suffix(outputFormat)
            with open(outputFile, 'w'): pass 
        except OSError:
            raise ArgumentParsingError(f'Output file cannot be written to due to permission issue')
        logging.info(f'Using output file {outputFile}')
        return outputFile
            
        
        
if __name__ == '__main__':
    logging.info('calling')
    ParseArguments.processArgs()