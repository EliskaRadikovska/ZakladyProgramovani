numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def linear_search(number, list_of_numbers):
    index = 0
    for item in list_of_numbers:
        if (item == number):
            return index
        else:
            index += 1

def binary_search(number, list_of_numbers, left_index, right_index):
    try:
        middle_index = (round(left_index + (right_index - left_index)/2))
        if number == list_of_numbers[middle_index]:
            return middle_index
        if number > list_of_numbers[middle_index]:
            return binary_search(number, list_of_numbers, middle_index, right_index)
        if number < list_of_numbers[middle_index]:
            return binary_search(number, list_of_numbers, left_index, middle_index)
    except:
        return "Číslo jsem nenašel"
    #moc nevím, jak jinak přidat možnost, že číslo nenašel

print(binary_search(3, numbers, 0, len(numbers) - 1))
