n,T = input().split()
num = input().split()
done = 0

for time in num:
  T = int(T)-int(time)
  if T < 0:
    break
  else:
    done += 1

print(done)