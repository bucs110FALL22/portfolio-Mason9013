n = 101
count = 0
while n != 1:
  if n % 2 == 0:
    n = n/2
  elif n % 2 != 0:
    n = 3*n+1
  count += 1
  #print(n)
print(count)

upper_limit = 20
iters = {}

countt = 0
start = range(2,upper_limit+1)

for n in start:
  if n % 2 == 0:
    n = n/2
  elif n % 2 != 0:
    n = 3*n+1
  countt += 1
  iters['count'] = 'n'

print(iters)