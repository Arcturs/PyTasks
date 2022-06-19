import re
import codecs


months_in_russian = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
                     5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
                     9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def to_date(obj, list):
        if len(list) == 3:
            return obj(int(list[0]), list[1], int(list[2]))
        else:
            return obj(int(list[0]), list[1], 0)

    def month_validation(self):
        if self.month.lower() not in months_in_russian.values():
            return False
        self.month = list(months_in_russian.keys())[list(months_in_russian.values()).index(self.month.lower())]
        return True


def regex_match(date):
    if bool(re.fullmatch(r'(0[1-9]|[1-2]\d|3[0-1]).(0[1-9]|1[0-2]).(\d{4})', date)):
        input_date = Date.to_date(list(map(int, date.split('.'))))
        if date_validation(input_date):
            return True

    if bool(re.fullmatch(r'([1-9]|[0-2]\d|3[0-1]) ([А-Яа-я]{0,8})( (\d{4}))?', date)):
        input_date = Date.to_date(date.split(' '))
        if not input_date.month_validation():
            return False
        if date_validation(input_date):
            return True

    return False


def date_validation(date):
    if (date.month == 2 and date.year % 4 != 0 and date.day >= 28) or (date.month == 2 and date.year % 4 == 0 and date.day >= 29):
        return False
    if date.day == 31 and date.month in (4, 6, 9, 11):
        return False
    return True


valid_dates = []
try:
    with codecs.open('test.txt', 'r', 'utf-8') as f:
        for line in f:
            if regex_match(line.strip()):
                valid_dates.append(line.strip())
    for line in valid_dates:
        print(f'{line}')
except Exception:
    print('Failed with exception')
