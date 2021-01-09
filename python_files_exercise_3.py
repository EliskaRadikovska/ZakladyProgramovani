import argparse
parser = argparse.ArgumentParser()
parser.add_argument("substring", help="searched substring")
parser.add_argument("string", help="string")
args = parser.parse_args()

index = 0
cnt = 0
while True:
    position = args.string.find(args.substring, index)
    if position == -1:
        break
    index = position + len(args.substring)
    cnt += 1
print("String {0} occurred {1} times in string {2}.".format(args.substring, cnt, args.string))    
