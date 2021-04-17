
import secrets

# --------------------------- Python Secrets ------------------------

n = int(input("Number of codes: "))
print("Names separated by enter:")

new_codes = {}

for z in range(n):

    hex = secrets.token_hex(16)
    name = input()
    new_codes[name] = hex

print(new_codes)

# --- Database

import csv 

with open('hex.csv','a') as codefile:

    writer = csv.writer(codefile, delimiter=',')
    for key, value in new_codes.items():
        writer.writerow([key,value])
