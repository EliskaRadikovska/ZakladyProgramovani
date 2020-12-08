#Exercise_3
import re
while True:
    name = str(input("Your name: "))
    match = re.match(r'^[A-Z][a-zA-Z]*$', name)
    if match:
        break
    print("Takhle to nepujde")
print("OK")