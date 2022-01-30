#!/usr/bin/python

import argparse
import logging


def arg_parse():
    """
    Parsing arguments. Returns file name and date given from cli.
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("-d", "--date")
    args = parser.parse_args()
    return args

def make_dictionary(file):
    """
    Takes an input of cookie_log csv file and returns a nested
    dictionary mapping a date to a dictionary mapping a cookie
    to the frequency of cookie in a given day.

    Raises:
        IOError: Unable to read file
    """
    
    nested_dic = {}
    
    try:
        with open(file) as f:
            cookie_logs = f.readlines()
            
    except IOError:
        logging.critical("No matching csv file exists for \"%s\"", file)
        raise

    for log in cookie_logs:
        cookie_time = log.rstrip().split(",")
        cookie, timestamp = cookie_time[0], cookie_time[1][:10]

        if timestamp in nested_dic:
            if cookie in nested_dic[timestamp]:
                nested_dic[timestamp][cookie] += 1
            else:
                nested_dic[timestamp][cookie] = 1
                            
        else:
            nested_dic[timestamp] = {cookie: 1}
            
    return nested_dic

def get_most_active_cookies(file, date):
    """
    Takes an input of cookie log csv file and date given from cli
    and returns a list of most active cookies.

    Raises:
        KeyError: Accessing key that is not in dictionary. 
        TypeError: Dictionary has a 'NoneType'
    """

    cookie_time_dic = make_dictionary(file)

    try:
        cookie_given_day = cookie_time_dic[date]
        most_active_freq = max(cookie_given_day.values())
        most_active_cookies = [cookie for cookie, freq in \
            cookie_given_day.items() if freq == most_active_freq]
                
        return most_active_cookies

    except KeyError as e:
        logging.warning("No cookies active for the given date: %s", date)
        return None
        
def main():
    args = arg_parse()
    logging.basicConfig(level=logging.DEBUG)    
    most_active_cookies = get_most_active_cookies(args.file, args.date)

    if most_active_cookies:
        for cookies in most_active_cookies:
            print(cookies)

if __name__ == "__main__":
    main()


"""
Notes: I would like to make some clarifications for the code written above.
First of all, I used string slicing to obtain the dates (since we technically
don't need to consider the time). Obviously, there are many other ways to do
it, but I thought this is the most simplistic way to do it, since we know
that a given input length and format doesn't change. I also assumed that the
given inputs will be valid. In other words, I assumed that the tester will
correctly input the dates and the csv file names. Another thing I would like
to note is that I could have been logging to a file (by creating a new log)
rather than a console, but for the sake of simplicity, I decided to be
doing the latter by directly outputting logging messages on console. Lastly,
I have used my "test log" as the given cookie_log.csv input to perform
unit-testing. 
"""



# WHAT TO DO: write unit test cases
# Revise comments


            
   
    
    
    


