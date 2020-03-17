values = input().split(" ")

count = int(values[2])
a = int(values[0])
b = int(values[1])
start = 1

while count > 0:
  if (start%a == 0 and start%b != 0):
    print('Fizz')
  elif (start%a != 0 and start%b == 0):
    print('Buzz')
  elif (start%a == 0 and start%b == 0):
    print('FizzBuzz')
  else:
    print(start)
  start+=1
  count-=1