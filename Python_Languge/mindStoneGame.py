'''
Loki’s Mind Stone
Sample Input:
5
3 1 4 2 5
Sample Output:
2
Explanaon:
Brainwashing Avengers with strengths 5 and 4 gives a total strength of 9,
which is greater than the combined strength of the remaining Avengers
(3 + 2 + 1 = 6).
'''

def brainWashedAvengersCount(list1):
    list1.sort(reverse = True)
    total_sum = sum(list1)
    count = 0
    for i in range(0, len(list1)):
        count+=list1[i]
        if(count > total_sum//2):
            return i+1
    return 0

n = int(input("Enter the number of averages"))
strengths = list(map(int, input().split()))
print(f"Original Count : {n}, strengths : {strengths}")
print(f"Brain washed avengers count {brainWashedAvengersCount(strengths)}")


