days = input()
temp = input().split(" ")
count = 0

for day in temp:
  if day < "0":
    count += 1

print (count)