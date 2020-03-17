megabyte = int(input())
month = int(input())
totalMB = megabyte*(month+1)
totalused = 0
while month > 0:
  totalused += int(input())
  month -= 1
print(totalMB-totalused)
