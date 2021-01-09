import argparse
parser = argparse.ArgumentParser()
parser.add_argument("string", help="string supposed to be counted")
parser.add_argument("-v", "--vowels", help="count only vowels", action="store_true")
parser.add_argument("-c", "--consonants", help="count only consonants", action="store_true")
args = parser.parse_args()

letters = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiouy"
all_letters = not args.vowels and not args.consonants

string = args.string.lower()

for letter in letters:
    count = string.count(letter)
    vowel = letter in vowels
    if (vowel and (args.vowels or all_letters)) or (not vowel and (args.consonants or all_letters)):
        print("{0} {1}".format(letter, count))