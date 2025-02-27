from collections import Counter
X = int(input("Enter the number of shoes "))
shoe_size = Counter(map(int, input("Size of each shoe in his shop ").split()))
N = int(input("The number of costumer "))

total_earn = 0
for _ in range(N):
    size, price = map(int, input("Enter size and price ").split())
    if shoe_size[size] > 0:
        total_earn += price
        shoe_size[size] -= 1
    
print(total_earn)








costumers = [tuple(map(int, input("Enter size and Space seperated price").split())) for _ in range(N)]
