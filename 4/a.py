

def hasDouble(n):
  s = "a" + str(n) + "a"
  for (a,b,c,d) in zip(s[0:-3], s[1:-2], s[2:-1], s[3:]):
    if b == c and a != b and c != d:
      return True
  return False

def nonDecreasing(n):
  ints = list(map(int, str(n)))
  for i, j in zip(ints[1:], ints[:-1]):
    if i < j:
      return False
  return True

def valid(n):
  return nonDecreasing(n) and hasDouble(n)
  
count = 0
A,B = 382345,843167
for i in range(A,B):
  if valid(i):
    count += 1

print(count)

