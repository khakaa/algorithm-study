croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()

for cr in croa:
    word = word.replace(cr, '*')

print(len(word))