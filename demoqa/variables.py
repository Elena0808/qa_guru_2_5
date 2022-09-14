import os

web = 'https://demoqa.com/'
month = '.react-datepicker__month-select'
day = '.react-datepicker__day--008'
year = '.react-datepicker__year-select'


def abs_path(relative_path):
    path = os.path.abspath(relative_path)
    return path
