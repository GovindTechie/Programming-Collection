''''
Sample Input:
7
1 8 4 2 10 3 2
Sample Output
8
Explanaon:
The maximum loss occurs when buying at a price of 10 and selling at a
price of 2,
resulng in a loss of 8.
'''

def maximumLoss(list1):
    max_loss = 0
    max_price = list1[0]

    for price in list1:
        max_price = max(max_price, price)
        loss = max_price - price
        max_loss = max(max_loss, loss)


    return max_loss


n = int(input("Enter a number of days"))
stockPrice = list(map(int, input().split()))
print(f"Number of daya {n}, StockPrices : {stockPrice}")
print(f"Maximum loss possible : {maximumLoss(stockPrice)}")