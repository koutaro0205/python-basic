import sys

args = sys.argv

sum = 0
for numStr in args[1:len(args)]:
  num = int(numStr)
  sum += num

print(sum)
