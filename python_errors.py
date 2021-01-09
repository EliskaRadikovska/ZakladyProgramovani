#Exercise_1
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ' + seasons[3])

#Exercise_2
message = ""
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)

#Exercise_3
name = str(input('Write your name:'))
contains_digit = False
for letter in name:
    if(letter.isdigit()):
        contains_digit = True
if (contains_digit):
    raise Exception('Cislo ve jmene vetsinou nebyva')
if (name.isspace()):
    raise Exception('Mas tam mezeru')
if (name[0].islower()):
    raise Exception('Nezacina velkym pismenem')
else:
    print('Vsechno ok')

#Exercise_4
def division():
    a = (input("Zadej cislo a:"))
    b = (input("Zadej cislo b:"))
    while(isinstance(a, int) == False or isinstance(b, int) == False):
        a = int(input("Zadej CISLO a:"))
        b = int(input("Zadej CISLO b:"))
    while(b == 0):
        b = int(input("Zadej b, ktere neni 0:"))
    return print(a / b)
division()
    
#Exercise_5
year = int(input("Greetings! What is your year of origin?"))
if (year <= 1900):
    print ('Woah, that\'s the past!')
elif (year > 1900 and year < 2020):
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")