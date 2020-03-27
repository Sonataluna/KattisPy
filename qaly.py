time = int(input())
acc = 0

while time > 0:
  a,g = input().split()
  acc = acc + (float(a)*float(g))
  time -= 1

print(acc)