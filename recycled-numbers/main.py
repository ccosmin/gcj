import math
from sets import Set
test_cases = int(raw_input())
for test_case in range(0, test_cases):
  a, b = map(int, raw_input().split())
  ret = Set() 
  for p in xrange(a, b + 1):
    d = int(math.log(p, 10)) + 1
    de = math.pow(10, d)
    cont = True
    imp = 1
    for j in range(1, d):
      de = de / 10
      imp = imp * 10
      c = p / imp 
      if c == 0:
        cont = False
        break
      r = p % imp
      to_check = r * de + c
      if p < to_check and a <= to_check <= b:
        ret.add((p, to_check)) 
  print 'Case #%d: %d' % (test_case + 1, len(ret))
