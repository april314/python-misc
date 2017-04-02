#DNA encoding
dna = input()
sym = dna[0]
cnt = 0
for i in dna:
  if sym == i:
    cnt += 1
  else:
    print(sym,cnt,sep="",end="")
    cnt = 1
  sym = i
print(sym,cnt,sep="",end="")
