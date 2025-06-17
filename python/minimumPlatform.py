'''Minimum Platforms Required (JP Morgan, PayPal, Accenture) 
Given the arrival and departure times of trains at a station, find the minimum number of platforms 
required at any point in time. 
'''



def find_min_platforms(n, arrival, departure):
    arrival.sort()
    departure.sort()
    i = j = 0
    platforms_needed = max_platforms = 0

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms


n = 6
arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print(find_min_platforms(n, arrival, departure))
