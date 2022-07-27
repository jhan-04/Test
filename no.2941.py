import sys
alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=sys.stdin.readline().strip()
cnt=0
for w in alpha:
    while w in word:
        cnt+=1
        word=word.replace(w,',')
print(len(word))