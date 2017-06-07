import re
input = "betty bought a bit of butter but the butter was bitter"
lists = input.split(' ')
result = []
for item in lists:
    result.append({item: re.findall(input)})
print(result)