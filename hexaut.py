
import csv

# ------- Authenticator 

data = [] # Placeholder for current hex codes

entry = False # Main operation for entry

user_input = []

user_input.append(input("Code: "))

print("")

# --- Dataset Pull

with open('hex.csv','r') as codefile:

    reader = csv.reader(codefile, delimiter=',')
    for i in reader:
        if i != []: 
            data.append(i[1])

# --- Comparing

for n in data:

    if n == user_input[0]:
        print("{} {}".format(n,"Approved"))
        entry = True
    else:
        print(n)

print("\nEntry:",entry)
    