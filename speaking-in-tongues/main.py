d = { ' ' : ' ', 'y' : 'a', 'n' : 'b', 'f' : 'c', 'i' : 'd', 'c' : 'e', 'w' : 'f', 'l' : 'g', 'b' : 'h', 'k' : 'i', 'u' : 'j', 'o' : 'k', 'm' : 'l', 'x' : 'm', 's' : 'n', 'e' : 'o', 'v' : 'p', 'z' : 'q', 'p' : 'r', 'd' : 's', 'r' : 't', 'j' : 'u', 'g' : 'v', 't' : 'w', 'h' : 'x', 'a' : 'y', 'q' : 'z' } 
def translate(c):
  return d[c]
test_cases = int(raw_input())
for test_case in range(0, test_cases):
  s = raw_input()
  ts = map(translate, s)
  print 'Case #%d: %s' % ( test_case + 1, ''.join(ts) ) 

