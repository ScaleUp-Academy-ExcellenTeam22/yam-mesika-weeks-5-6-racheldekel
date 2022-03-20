import random
import time
import datetime

INPUT_DATE_MESSAGE = "Please enter date in YYYY-MM-DD format: "
MONDAY_MESSAGE = "אין לי ויניגרט"

#the main function - gets dates and send for each function to get a dae and check if monday
def print_date():
    start_date = get_date(INPUT_DATE_MESSAGE)
    end_date = get_date(INPUT_DATE_MESSAGE)
    rand_date = random_date(start_date, end_date, '%Y-%m-%d', random.random())
    print(rand_date)
    if check_if_monday(rand_date):
        print(MONDAY_MESSAGE)

#return the date
def get_date(string):
    in_date = input(string)
    return in_date

#the random function - return the date in datetime format
def random_date(start, end, time_format, prop):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return datetime.date(time.localtime(ptime).tm_year,
                         time.localtime(ptime).tm_mon,
                         time.localtime(ptime).tm_mday)

#function that check if monday with weekday() function
def check_if_monday(date):
    return date.weekday() == 0

#print the program
if __name__ == '__main__':
    print_date()