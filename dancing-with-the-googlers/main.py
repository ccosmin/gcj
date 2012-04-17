test_cases = int(raw_input())
for test_case in range(0, test_cases):
  l = raw_input().split()
  n = int(l[0])
  s = int(l[1])
  p = int(l[2])
  g = [int(x) for x in l[3:]]
  r = 0

  for i in g:
    rest = i - p
    if rest < 0:
      continue
    comp = [0, 0]
    if rest % 2 == 0:
      comp[0] = comp[1] = rest / 2
    else:
      comp[1] = rest / 2
      comp[0] = comp[1] + 1
    if comp[0] < p - 2 or comp[1] < p - 2:
      continue
    if p - 2 == comp[0]  or p - 2 == comp[1]:
      if s > 0:
        r = r + 1
        s = s - 1
    else:
      r = r + 1
  print 'Case #%d: %d' % (test_case + 1, r)

