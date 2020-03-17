import sys

CORRECT = [1, 1, 2, 2, 2, 8]
tocheck = input()
count = 0
result = ''

for value in tocheck.split():
  result+=str((CORRECT[count]-int(value)))+' '
  count += 1
print(result)