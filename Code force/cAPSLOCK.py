def isup(s):
    for i in s[1:]:
        if i.islower():
            return False
    return True
def up(s):
    return s[0].upper()+s[1:].lower()
s=input()
if(isup(s)):
    if s[0].islower():
        print(up(s))
    else:
        print(s.lower())
else:
    print(s)
