# Randy Baukovac CIS188 Password checker.
# import re to check strings that match it
import re


# define our main function with a for loop to run through the input str to check for specific criteria.
def passCheck(password):
    counter = 0
    for regex in regex_list:
        if regex.search(password) is None:
            tryAgain = input('Please make your password stronger: \b')
            if tryAgain == "Y" or 'y':
                passCheck(pw)
            else:
                break
        else:
            counter += 1
            continue
    if counter == 4:
        print('You passed the strength test!')


# create variables to hold each set of information we are looking for in the str.  Each meets a certain condition and matches it
length = re.compile('.{8,}')
lower_case = re.compile('[a-z]+')
upper_case = re.compile('[A-Z]+')
digit = re.compile('[\d]+')

regex_list = [length,
              lower_case,
              upper_case,
              digit]
pw = input('Enter desired password:\n')

passCheck(pw)
