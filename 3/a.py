coords = dict()

with open("inp.txt", 'r') as f:
  A, B = [l.strip().split(',') for l in f.readlines()]

x,y = 0,0

k = 0
for command in A:
  c, d = command[0], int(command[1:])

  dx, dy = 0,0
  if c == 'R':
    dx = 1
  elif c=='L':
    dx = -1
  elif c=='U':
    dy = 1
  else:
    assert c == 'D'
    dy = -1

  for i in range(d):
    x += dx
    y += dy
    coords[(x,y)] = k
    k += 1


best = 1e10
x,y=0,0

k = 0
for command in B:
  c, d = command[0], int(command[1:])

  dx, dy = 0,0
  if c == 'R':
    dx = 1
  elif c=='L':
    dx = -1
  elif c=='U':
    dy = 1
  else:
    assert c == 'D'
    dy = -1

  for i in range(d):
    x += dx
    y += dy
    if ((x,y) in coords) and k + coords[(x,y)] < best:
      best = k + coords[(x,y)]
    k += 1



print(best + 2)


