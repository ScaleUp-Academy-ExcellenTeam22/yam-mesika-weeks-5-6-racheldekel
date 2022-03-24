import random
import time
import datetime

INPUT_DATE_MESSAGE = "Please enter date in YYYY-MM-DD format: "


def print_date():
    """
    the main function - gets dates and send for each function to get a dae and check if monday
    :return:
    """
    start_date = get_date(INPUT_DATE_MESSAGE)
    end_date = get_date(INPUT_DATE_MESSAGE)
    rand_date = random_date(start_date, end_date, '%Y-%m-%d', random.random())
    print(rand_date)
    if check_if_monday(rand_date):
        print("אין לי ויניגרט")


def get_date(string):
    """
    return the date
    :param string: string for the output
    :return: print the date
    """
    in_date = input(string)
    return in_date


def random_date(start, end, time_format, prop):
    """
    the random function - return the date in datetime format
    :param start: the first date - to start in
    :param end: the last date - the end date to random
    :param time_format: how the date looks like
    :param prop: the proper time
    :return:
    """
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return datetime.date(time.localtime(ptime).tm_year,
                         time.localtime(ptime).tm_mon,
                         time.localtime(ptime).tm_mday)


def check_if_monday(date):
    """
    function that check if monday with weekday() function
    :param date: get the date
    :return: return if its monday
    """
    return date.weekday() == 0


if __name__ == '__main__':
    """
    print the program
    """
    print_date()
