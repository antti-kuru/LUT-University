# https://wiki.python.org/moin/BitwiseOperators  
def subsets(n: int) -> list:
  

    def __subsethelp(input_list, n, all_subsets):
        # I haven't used << or >> operators before but know I did.
        # 1 << n returns n (which is the input number) with bits shifted to the left by n places
        # so it is 2^n
        for i in range (1 << n):
            subset =[]
            for j in range(n):
                if (i & (1<<j)) != 0:
                    subset.append(input_list[j])
            if subset:
                all_subsets.append(subset)

    input_list = []
    for i in range(1, n + 1):
        input_list.append(i)
    all_subsets = []
    __subsethelp(input_list, n, all_subsets)
    return all_subsets


if __name__ == "__main__":
    print(subsets(1))   # [[1]]
    print(subsets(2))   # [[1], [2], [1, 2]]
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]
    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]