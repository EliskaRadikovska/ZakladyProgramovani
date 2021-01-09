import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("word", help="word")
parser.add_argument("letter", help="letter")
args = parser.parse_args()

match = re.match(r'^[a-zA-Z]$', args.letter)
if not match:
    print("Letter is not letter")
    exit()

print(re.sub(args.letter, '', args.word))