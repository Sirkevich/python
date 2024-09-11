from dateutil import parser


def parse_date(self, date_str):
    try:
        return parser.parse(date_str, dayfirst=True)
    except ValueError:
        raise ValueError("Incorrect date format")