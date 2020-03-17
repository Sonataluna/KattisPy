value = format(int(input()),'b')
value = str(value)
new_value = ""

for bit in value[::-1]:
  new_value += bit

new_value2=int(new_value,2)
print (new_value2)