def invalid_transactions(transactions):
    invalid = set()
    records = []

    for t in transactions:
        name, time, amount, city = t.split(",")
        records.append((name, int(time), int(amount), city, t))

    for i in range(len(records)):
        name1, time1, amount1, city1, orig1 = records[i]

        if amount1 > 1000:
            invalid.add(orig1)

    
        for j in range(len(records)):
            if i == j:
                continue
            name2, time2, amount2, city2, orig2 = records[j]
            if name1 == name2 and abs(time1 - time2) <= 60 and city1 != city2:
                invalid.add(orig1)
                invalid.add(orig2)

    return list(invalid)


transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
result = invalid_transactions(transactions)

print("Invalid transactions:")
for t in result:
    print(t)
