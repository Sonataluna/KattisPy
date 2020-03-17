coordA = int(input())
coordB = int(input())

def checkup():
  if coordA > 0 and coordB > 0:
    return 1
  elif coordA > 0 and coordB < 0:
    return 4
  elif coordA < 0 and coordB > 0:
    return 2
  else:
    return 3

print(checkup())