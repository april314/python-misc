a = int(input()) #lines
b = int(input())
c = int(input()) #columns
d = int(input())
for i in range(c,d+1):
  print('\t',i,end='')
for j in range(a,b+1):
  print()
  print(j,'\t',end='')
  for i in range(c, d+1):
    print(i*j,'\t',end='')
