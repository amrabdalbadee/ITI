#lab 4_karatsuba
def karatsuba(m,n):
    if(m<10 or n<10):
        return m*n
    else:
        mstring = str(m)
        nstring = str(n)

        k = max(len(mstring), len(nstring))
        mid=int(k//2)
        a = int(mstring[:-mid])
        c = int(nstring[:-mid])
        b = int(mstring[-mid:])
        d = int(nstring[-mid:])
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        return ac*10**(2 * mid) + ad_plus_bc*10**(mid) + bd

print("Answer is:")
print(karatsuba(3425,2486))