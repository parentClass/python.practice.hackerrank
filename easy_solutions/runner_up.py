if __name__ == '__main__':
    # accepts the scores array size input
    n = int(input())
    # accepts the scores input
    arr = map(int, input().split())
    # converting and removing duplicate value then store it in a variable.
    scores = list(set(arr))
    # in line sorts the scores
    scores.sort()
    # prints the second to the last value of the list
    print(scores[-2])
