# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott Watters

127 Broken Head Rd, Suffolk Park / Byron Bay 2481

October 1st, 2023
"""
def prime_factorise(n):
    L = []
    for x in range(1, n + 1):
        if n % x == 0:
            L.append(x)
#    print("L: {}".format(L))
    t = 1
    TL = []
    winner = 1
    llx = 1
    print(L)
    for x in range(0, len(L) - 1, 1):
        TL2 = TL
        t *= L[x]
        TL.append(L[x])
        if t == n:
            winner = t
            print(TL, t)
            return (TL, t)
        elif (t * t) == n:
            winner = t * t
            TL.append(t)
            return (TL, winner)
        elif (t * t * t) == n:
            winner = t * t * t
            TL.append(t)
            TL.append(t)
            return (TL, winner)
        elif (t * t * t * t) == n:
            winner = t * t * t * t
            TL.append(t)
            TL.append(t)
            TL.append(t)
            return (TL, winner)
        else:
            continue
        # if t != n:
        #     TL3 = TL2
        #     ttt = tt
        #     ttt *= L[x - 1]
        #     TL3.append(L[x - 1])
        #     print("TL3: {}".format(TL3))
        #     if ttt == n:
        #         winner = ttt
        #         return (TL3, winner)
            
            
def main():
    print("After coding at an undergraduate level and in some areas postgraduade level, because I sat MIT and Harvard OCW and MITx and edX, here\'s a small example of my own code for the fundamental theorem of arithmetic and prime-factorisation\n")
    print("Charles Truscott Watters.\n")
    print("Enter a number to find all prime factors for all numbers below: ")
    n = int(input())
    for x in range(1, n, 1):
        ans = prime_factorise(x)
        if ans == None:
            print("{} is prime".format(x))
        else:
            print("{} is the product of {} hence {} is equal to {}".format(x, ans[0], ans[1], x))
    
if __name__ == """__main__""": main()