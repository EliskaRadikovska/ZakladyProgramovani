#Exercise_4
import re
def only_digits(string):
    return re.sub(r'[^0-9]+', '', string)

numbers = only_digits('2004-959-559 # This is Phone Number')
print(numbers)
numbers = only_digits("I don't have any numbers.")
print(len(numbers))

