'''
Find the first position from which a car can complete a circular tour
given N fuel stations
and required distances.
Input:
Fuel = [6, 3, 7, 4]
Dist = [5, 6, 2, 5]
Output: 
'''

def start_index_finder(fuel, dist):
    n = len(fuel)

    total_fuel = 0
    total_dist = 0
    curr_fuel = 0
    start_index = 0

    for i in range(n):
        total_fuel += fuel[i]
        total_dist += dist[i]
        curr_fuel += fuel[i]-dist[i]

        if curr_fuel < 0:
            start_index = i+1
            curr_fuel = 0

    if total_fuel < total_dist:
        return -1
    
    return start_index

Fuel = [6, 3, 7, 4]
Dist = [5, 6, 2, 5]
print(f"Original Fuel {Fuel}\nOriginal Distance {Dist}")
print(f"Starting Station that complete circular tour : {start_index_finder(Fuel, Dist)}")