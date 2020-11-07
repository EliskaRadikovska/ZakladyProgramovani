#Exercise_1
names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef','Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav','Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal','Lenka', 'Katerina']
name = str(input("Your name: "))
if (name in names_list):
    print("Jmeno je v listu")
else: 
    print("Jmeno neni v listu")

#Exercise_2
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india',
'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike',
'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec',
'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform',
'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
'z':'zulu'}
user_name = str(input("Your name:"))
for letter in user_name:
    print(d[letter.lower()])
    
#Exercise_3
a = [[1,2,3],[4,5,6],[7,8,9]]
list_a = []
for item in a:
    for number in item:
        list_a.append(number)
b_1 = [x - 2 for x in list_a if x % 3 == 0]
b_2 = [x - 1 for x in list_a if x % 3 == 0]
b_3 = [x  for x in list_a if x % 3 == 0]
b = []
b.append(b_1)
b.append(b_2)
b.append(b_3)
print(b)

#Exercise_4
shopping_list = ["mouka", "maslo", "vejce"]
new_item = str(input("Nova polozka:"))
not_found = False
for item in shopping_list:
    not_found = False
    if (new_item==item):
        print(new_item)
        break
    else:
        not_found = True
if (not_found):
    shopping_list.append(new_item)
print(shopping_list)

#Exercise_5
all_numbers = list(range(1,26))
first_list = [x for x in all_numbers if x % 5 == 0]
print(first_list)
second_list = ['{0} is my favorite number'.format(x) for x in all_numbers if x % 5 == 0]
print(second_list)


#Exercise_6
string_input = str(input("Zadejte text:"))
positions = []
for i, letter in enumerate(string_input):
    if(letter == 'a'):
        positions.append(i)
print(positions)

#Exercise_7
scores = {'John' : 10, 'Emily' : 35, 'Metthew' : 50}
triple_points = {x : 3 * scores[x] for x in scores}
print(triple_points)
