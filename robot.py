#talking robot
n = int(input())
res100 = n%100
res10 = n%10
if (res100 >= 11) and (res100 <= 14) or (res10 == 0) or (res10 >= 5 and res10 <= 9):
  print(str(n)+' программистов')
elif res10 == 1:
  print(str(n)+" программист")
elif (res10 >= 2 and res10 <= 4):
  print(str(n)+" программиста")
