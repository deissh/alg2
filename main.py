def kr(n: str) -> int:
    ng = 1
    lg = 1
    ans = 0
    ps = n[0: 1]
    n = n[1:]
    while n != '':
        ts = n[0: 1]
        if n != '':
            n = n[1:]
        if ts == ps:
            lg += 1
        else:
            psInt = int(ps)
            ans += psInt * (ng ** lg)
            ng += 1
            lg = 1
            ps = ts
    psInt = int(ps)
    ans += psInt * (ng ** lg)
    return ans


d, n = map(int, input().split())
minst = input()
minkr = kr(minst)
for i in range(0, n - 1):
    tst = input()
    tkr = kr(tst)
    if tkr < minkr:
        minkr = tkr
        minst = tst
print(minkr)
print(minst)
