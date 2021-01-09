#Exercise_1
def divide(x, y):
    z = x / y
    return z
print(divide(6,2))

numbers = [int(item) for item in input("Napiste cisla:").split()]
print(numbers)
def sum(list_of_numbers):
    x = 0
    for item in list_of_numbers:
        x += item
    return x
print(sum(numbers))

#Exercise_2
numbers_list = [int(item) for item in input("Napiste cisla:").split()]
compare_list = (lambda list_of_numbers: print('big list') if len(list_of_numbers) > 5 else print('small list'))
compare_list(numbers_list)

#Exercise_3
def string_upper_lower(x):
    uppercase_letters = 0
    lowercase_letters = 0
    for item in x:
        if item.isupper():
            uppercase_letters += 1
        else:
            lowercase_letters += 1
    return uppercase_letters, lowercase_letters
print(string_upper_lower("AhOj"))

#Exercise_4
def meal_vouchers(lunch_cost, voucher_value):
    pay_in_cash = lunch_cost % voucher_value
    amount_of_vouchers = (lunch_cost - pay_in_cash) / voucher_value
    return ("Lunch cost: {0} CZK, Pay in cash: {1}, Pay in meal vouchers: {2} pcs, {3} CZK each".format(lunch_cost, pay_in_cash, amount_of_vouchers, voucher_value))
print(meal_vouchers(500, 74))

#Exercise_5
def factorial(x):
    if x==1:
        return x
    else:
        return x * factorial(x - 1)
print(factorial(5))




