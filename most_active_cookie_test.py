import unittest
import most_active_cookie as f 
import logging

class TestMethods(unittest.TestCase):
    """
    First three tests will check if the program correctly outputs
    an appropriate value given that there is one, multiple, and zero
    cookies in a given day. The last test checks if the program correctly
    raises an error when an invalid file is inputted.
    """

    def test_one_cookie_day(self):
        cookie = ['4sMM2LxV07bPJzwf']
        file = 'cookie_log.csv'
        date = '2018-12-07'
        self.assertEqual(f.get_most_active_cookies(file ,date), cookie)

    def test_test_multiple_cookie_day(self):
        cookie = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
        file = 'cookie_log.csv'
        date = '2018-12-08'
        self.assertEqual(f.get_most_active_cookies(file ,date), cookie)

    def test_test_no_cookie_day(self):
        cookie = None
        file = 'cookie_log.csv'
        date = '2018-11-11'
        self.assertEqual(f.get_most_active_cookies(file ,date), cookie)


    def test_invalid_file(self):
        file = 'invalid_file.csv'
        date = '2018-12-07'
        self.assertRaises(IOError, f.get_most_active_cookies, file, date)
                        
                         
def main():
    unittest.main()

if __name__ == "__main__":
    main()
    
