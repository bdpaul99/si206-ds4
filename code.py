# function to return the factorial of a number
# Add comments
import unittest

def factorial(num):
    ans = 1
    if num < 0:
        return None
    elif num < 2:
        return ans
    else:
        for i in range(1, num + 1):
            ans = ans * i
        return ans


# function to check if the input year is a leap year or not
def check_leap_year(year):
    isLeap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                isLeap = True
        else:
            isLeap = True
    return isLeap



class TestFactorial(unittest.TestCase):
    def testfactorial_test(self):
        self.assertEqual(factorial(0),1,"testing factorial(0) is equal to 0")
        self.assertEqual(factorial(1),1, "testing factorial(1) is equal to 1")
        self.assertEqual(factorial(5),120,"testing factorial(5) is equal to 120")
        self.assertEqual(factorial(-3), None, "testing factorial(-3) is equal to none")
        self.assertEqual(factorial(6),720,"testing factorial(6) is equal to 720")
        return




print("check_leap_year(2000): {}".format(check_leap_year(2000)))
print("check_leap_year(1990): {}".format(check_leap_year(1990)))
print("check_leap_year(2012): {}".format(check_leap_year(2012)))
print("check_leap_year(2100): {}".format(check_leap_year(2100)))


unittest.main(verbosity=2)
