'''Odd Occurring Balloon Color: o Problem: Given an array representing colors
of balloons, find the first color that appears an odd number of times. If all
colors appear an even number of times,
output "All are even".
Example: ▪ Input: N = 7, B = ['r', 'g', 'b', 'b', 'g', 'y', 'y']
Output: 'r' 
'''

# Simple Approach
from collections import Counter
N = 7
B = ['r', 'g', 'b', 'b', 'g', 'y', 'y']
ColorName = {'r':"Red", 'g':"Green", 'b':"Blue", 'y':"Yellow"}
B_cout = dict(Counter(B))
print(B_cout)

all_even = True
for key, value in B_cout.items():
    if value %2 != 0:
        print(f"Color occured odd time: {key} -> {ColorName[key]}")

        all_even = False
        break
    
        
if all_even:
    print("All ballooon are even")







# # approch 2 just for counting color occurance without using 
# N = 7
# B = ['r', 'g', 'b', 'b', 'g', 'y', 'y']
# B_count = {}
# for color in B:
#     if color in B_count:
#         B_count[color] += 1
#     else:
#         B_count[color] = 1






    