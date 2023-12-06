def primes(N):
    #https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # 0 and 1 are not prime's
    amount = 0
    A = [True for i in range (N+1)]
    A[0] = False
    A[1] = False

    for i in range (2, int(N**0.5) + 1):
        if A[i] == True:
            for j in range(2*i, N+1, i):
                A[j] = False

    for i in range (2, N+1):
        if A[i]:
            #print(i)
            amount +=1

    return amount


if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15