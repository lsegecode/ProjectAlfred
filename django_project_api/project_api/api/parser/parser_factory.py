from api.parser.parser import Parser
from api.parser.parsers import *
from api.parser.custom_exceptions import InvalidParserFactoryOption, MultipleValuesParserFactoryClass
from logger.logger import *

class ParserFactory(object):

    @wrap(entering, exiting)
    def parser(self, *parser_type):
        """Generating parsers"""
        if len(parser_type) > 1:
            raise MultipleValuesParserFactoryClass(parser_type)
        if len(parser_type) < 1:
            raise InvalidParserFactoryOption(parser_type)
        parser = self.get_parser(parser_type[0])
        return parser

    @wrap(entering, exiting)
    def get_parser(self, parser_type):
        """Getting parsers"""
        parsers_classes = Parser.__subclasses__()
        parser = list(
            filter(lambda parser_class: parser_class.__name__.lower() == parser_type.lower().strip(), parsers_classes))
        if len(parser) > 0:
            return parser[0]()
        else:
            raise InvalidParserFactoryOption(parser_type)
