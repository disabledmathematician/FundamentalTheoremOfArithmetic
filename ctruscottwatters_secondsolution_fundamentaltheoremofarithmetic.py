#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott

127 Broken Head Rd, Suffolk Park / Byron Bay NSW 2481

1st October 2023, Second Try at Infinite Solution to Fundamental Theorem of Arithmetic.
"""

def check_if_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False

    return True
def prime_factorise(n):
    if check_if_prime(n) == True:
        return [1, n]
    factors = []
    for x in range(1, n - 1):
        if n % x == 0:
            factors.append(x)
#    print(factors)
    factor_matrices = []
    for x in range(n):
        factor_matrices.append(factors)
    length_matrices = len(factor_matrices) - 1
    count = 1
    all_matrice_units_in_sequence = []
    new_n = 1

    while length_matrices > 0:
        for x in range(len(factor_matrices)):
            if count < len(factors):
                new_n *= factor_matrices[x][count]
                print("new_n: {}, factor_matrices[x][count]: {}".format(new_n, factor_matrices[x][count]))
                all_matrice_units_in_sequence.append(factor_matrices[x][count])
                print(all_matrice_units_in_sequence)
#                print(factor_matrices[x][count])
                if new_n == n:
                    return all_matrice_units_in_sequence
                elif new_n > n:
                    new_n = 1
                    all_matrice_units_in_sequence = []
                count += 1
            else:
                count = 1
#        count = len(factors) - 1
        length_matrices -= 1

    

def CharlesTruscott():
#    ans, ans1 = prime_factorise(20)
#    print("ans: {}, ans1: {}".format(ans, ans1))
    print("Second Solution, Reaching to an Infinitely Correct Algorithm for the Fundamental Theorem of Arithmetic. Two afternoons spent on this")
    print("Copyright Charles Truscott 127 Broken Head Rd Suffolk Park / Byron Bay NSW 2481 Australia. Certified by MIT and Harvard in Computer Programming and Numerical / Scientific Computation")
    print("Enter a number to find all factors of the number, or whether the number is prime: ")
    number = int(input())
    all_units = prime_factorise(number)
    if all_units != None:
        print("The factors of {} are {}".format(number, all_units))
    print("May have got this algorithm correct to an infinite integer number set ...")
    print("The fundamental theorem of arithmetic states that all numbers which are not prime are the product of primes, each other the number itself and one")
#    for x in range(1, 30):
#        all_units = prime_factorise(x)
#        if all_units != None:
#            print("The factors of {} are {}".format(x, all_units))

if __name__ == """__main__""": CharlesTruscott()