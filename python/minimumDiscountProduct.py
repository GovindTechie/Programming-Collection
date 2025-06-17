'''
Minimum Discount Product
'''



def minimumDiscountProduct(products):
    min_discount = float('inf')
    result = ""

    for product in products:
        name, price, discount = product.split(",")
        discount = int(discount)
        
        if discount < min_discount:
            min_discount = discount
            result = name

    return result

n = 4
products = [
    "mobile,10000,20",
    "shoe,5000,10",
    "watch,6000,15",
    "laptop,35000,5"
]

print(minimumDiscountProduct(products))

