s = input()

for i in range(len(s)):
    if s[i].islower():
        s = s[:i] + s[i:].replace(s[i],s[i].upper(),1)
    elif s[i].isupper():
        s = s[:i] + s[i:].replace(s[i],s[i].lower(),1)

print(s)