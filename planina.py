number = int(input())
start = 2

while number > 0:
  start += start-1
  number -=1

start=start*start

print (start)