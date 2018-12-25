from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser
from rest_pandas.renderers import PandasCSVRenderer
import pandas
import csv
from task import settings


class CSVParser(BaseParser):
    """
    Parses CSV-dataframe data.
    """
    media_type = 'text/csv'
    renderer_class = PandasCSVRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as CSV and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            dia = csv.excel()
            data = stream.read().decode(encoding)
            return pandas.read_csv(data, dialect=dia)
        except ValueError as exc:
            raise ParseError('CSV parse error - %s', parser_context=None)