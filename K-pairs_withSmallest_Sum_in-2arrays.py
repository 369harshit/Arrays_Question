# Python3 program to print the k the smallest
# pairs | Set 2

# Function to print the K the smallest pairs
def printKPairs(a1, a, size1, size2, k):
    # if k is greater than total pairs
    if k > (size2 * size1):
        print("k pairs don't exist\n")
        return

    # _pair _one keeps track of
    # 'first' in a1 and 'second' in a2
    # in _two, _two[0] keeps track of
    # element in the a2and _two[1] in a1[]
    _one, _two = [0, 0], [0, 0]
    cnt = 0

    # Repeat the above process till
    # all K pairs are printed
    while cnt < k:

        # when both the pointers are pointing
        # to the same elements (po3)
        if (_one[0] == _two[1] and _two[0] == _one[1]):
            if a1[_one[0]] < a2[_one[1]]:
                print("[", a1[_one[0]], ", ", a2[_one[1]], "] ", end=" ")

                # updates according to step 1
                _one[1] = (_one[1] + 1) % size2
                if _one[1] == 0:  # see po2
                    _one[0] = (_one[0] + 1) % size1

                # updates opposite to step 1
                _two[1] = (_two[1] + 1) % size2
                if _two[1] == 0:
                    _two[0] = (_two[0] + 1) % size2

            else:
                print("[", a2[_one[1]], ", ", a1[_one[0]], "] ", end=" ")

                # updates according to rule 1
                _one[0] = (_one[0] + 1) % size1
                if _one[0] == 0:  # see po2
                    _one[1] = (_one[1] + 1) % size2

                # updates opposite to rule 1
                _two[0] = (_two[0] + 1) % size2
                if _two[0] == 0:  # see po2
                    _two[1] = (_two[1] + 1) % size1

        # else update as necessary (po1)
        elif a1[_one[0]] + a2[_one[1]] <= a2[_two[0]] + a1[_two[1]]:
            if a1[_one[0]] < a2[_one[1]]:
                print("[", a1[_one[0]], ", ", a2[_one[1]], "] ", end=" ")

                # updating according to rule 1
                _one[1] = ((_one[1] + 1) % size2)
                if _one[1] == 0:  # see po2
                    _one[0] = (_one[0] + 1) % size1
            else:
                print("[", a2[_one[1]], ", ", a1[_one[0]], "] ", end=" ")

                # updating according to rule 1
                _one[0] = ((_one[0] + 1) % size1)
                if _one[0] == 0:  # see po2
                    _one[1] = (_one[1] + 1) % size2

        elif a1[_one[0]] + a2[_one[1]] > a2[_two[0]] + a1[_two[1]]:
            if a2[_two[0]] < a1[_two[1]]:
                print("[", a2[_two[0]], ", ", a1[_two[1]], "] ", end=" ")

                # updating according to rule 1
                _two[0] = ((_two[0] + 1) % size2)
                if _two[0] == 0:  # see po2
                    _two[1] = (_two[1] + 1) % size1

            else:
                print("[", a1[_two[1]], ", ", a2[_two[0]], "] ", end=" ")

                # updating according to rule 1
                _two[1] = ((_two[1] + 1) % size1)
                if _two[1] == 0:  # see po2
                    _two[0] = (_two[0] + 1) % size1
        cnt += 1


# Driver Code
if __name__ == '__main__':
    a1 = [2, 3, 4]
    a2 = [1, 6, 5, 8]
    size1 = len(a1)
    size2 = len(a2)
    k = 4
    printKPairs(a1, a2, size1, size2, k)
