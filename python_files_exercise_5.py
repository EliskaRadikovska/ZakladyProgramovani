list_of_things = ["violin", "piano", "book", "coffee", "cat"]
number = 1
with open('things_to_island.txt', 'w', encoding='utf-8') as f:
    for item in list_of_things:
        f.write("{0}\t{1}\n".format(number, item))
        number += 1