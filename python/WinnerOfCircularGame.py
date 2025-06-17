'''
Leetcode -- 1823. Find the Winner of the Circular Game
Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
'''


class Solution(object):
    def findTheWinner(self, n, k):
        friends = list(range(1, n+1))
        index = 0

        while len(friends) > 1 :
            index = (index + k -1) % len(friends)
            friends.pop(index)

        return friends[0]


s1 = Solution()
print(s1.findTheWinner(5,2))
        