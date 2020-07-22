def solve(s):
    l = []
    for i in range(len(s)):
        l.append(s[i])
    a = ord(l[0])
    b = a - 32
    w = chr(b) 
    l.remove(l[0])
    l.insert(0, w)
        
    if " " in l:
        m = l.index(" ")
        z = ord(l[m+1])
        x = z - 32
        y = chr(x)
        l.remove(l[m+1])
        l.insert(m+1, y)
        p = ''.join(l)
        return p


n = "aditya gole"
print(solve(n))
