class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)

        return list(groups.values())

        
        


s1 = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(f"Original strings : {strs}")
print(f"Group of Anagram : {s1.groupAnagrams(strs)}")

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]