#matrix input
matr = []
str = input()
while str != "end":
  matr.append([int(i) for i in str.split()])
  str = input()
#printing new matrix
for i in range(len(matr)):
  for j in range(len(matr[0])):
    print(matr[i-1][j] + matr[(i+1)%len(matr)][j] + matr[i][j-1] + matr[i][(j+1)%len(matr[0])], end = " ")
  print()
