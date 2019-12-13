#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The complexity of this function is O(n). The first variable assignment is 0(1) and the while loop results in O(n) because, while n is increasing the loops of the while loop at a rate of n^3, n^2 is also added to var a to account for the loop conditional. 


b) The complexity of this function is O(n log n). The first variable assignment is 0(1) and the for loop has an O(n). The while loop is O(log n) because j is doubled at each pass. As n increased, j continues to double to close the loop.


c) The complexity of this function is O(n). This recursive function has an 0(1) body and returns a recursive call to itself to produce O(n). 

## Exercise II

For this problem, instead of starting at the first floor, dropping an egg to see if it breaks, and continuing this until we get an egg that breaks; I would split the building in two halves- upper and lower. I would first first the middle of the building and check to see if dropping an egg there breaks. Because we are looking for the first floor where an egg breaks, if egg does break at middle: check the floor below. If it also breaks there, we can disregard the upper portion completely and redo the process with the lower half. If the egg did not break, the same would follow for the upper half, etc, until we find a position where an egg[i] does not break and egg[i + 1] does break.

def find_f(floors):
    BASE CASE
    if len(floors) == 1:
        return floors[0]

    def drop_egg(floor):
        if egg == broken:
            return 1
        if egg != broken:
            return 0

    mid == floors // 2
    if drop_egg(mid) == 1:
        if drop_egg(mid - 1) == 0:
            f = floors[mid]
            return f
        else:
            f = floors[: mid+1]
            return f
    else:
        if drop_egg(mid + 1) == 1:
            f = floors[mid + 1]
            return f
        else:
            f = floors[mid+1 :]