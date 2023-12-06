def sums(items):
    # trying to define different sums to list so using memoization
    #single_sums list contains all sums that occur only ones, so there is no duplicates
    single_sums = [0] * (sum(items) + 1)
    single_sums[0] = 1

    for item in items:
        for j in range (len(single_sums) - 1, -1, -1):
            if single_sums[j] > 0:
                single_sums[j + item] += single_sums[j]

    # I have no clue why this works with counter -1, or why counter = 0 gives wrong answers
    # that differ with one. 
    counter = -1
    for i in single_sums:
        if i > 0:
            counter += 1

    
    return counter



    


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121