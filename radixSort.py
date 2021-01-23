# Eduardo F.F. Cruz @2020
import random


def countingSort(arr, n, div):
    # arr is the integer list
    # n is the max number supported by the counting sort (supports numbers from 0 to n)
    if (len(arr) > 0):
        countList = [0] * n  # counting list init:filled w/zeros
        sortedList = [0]*len(arr)  # initialize sortedList
        for num in arr:
            countList[(num//div) % 10] += 1  # increment digit occurence
        for i in range(1, n):
            countList[i] += countList[i - 1]  # accumulate
        for i in range(len(arr) - 1, -1, -1):
            # loop from right to left
            sortedList[countList[(arr[i] // div) % 10] -
                       1] = arr[i]  # crescent order
            countList[(arr[i] // div) % 10] -= 1  # decrement
        return sortedList

    return arr


def radixSort(arr):
    div, maxNum = 1, max(arr)
    while (maxNum//div > 0):
        # div is used to determine which digit position will counting sort be applied to
        arr = countingSort(arr, 10, div)
        div *= 10
    return arr


def generateRandomList(min, max, qnt):
    # for testing purposes
    return random.sample(range(min, max + 1), qnt)


def main():
    lista = generateRandomList(1, 1000000, 1000)
    # unsorted
    print("unsorted: ", end='')
    print(lista)
    lista = radixSort(lista)
    print("\nsorted: ", end='')
    print(lista)

if __name__ == '__main__':
    main()
