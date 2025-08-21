class Solution(object):
    def equalFrequency(self, word):
        dict = {}
        for ch in word:
            if ch not in dict:
                dict[ch] = 1
            else:
                dict[ch] += 1

        list1 = list(dict.values())
        list1.sort()
        diff = 0
        morediff = 0
        zeroDiff = 0
        for count in range(0, len(list1)-1):
            if(list1[count+1] - list1[count] == 1):
                diff += 1
            if(list1[count+1] - list1[count] >= 2):
                morediff += 1
            else :
                zeroDiff += 1


        

        # handling the value such as 3331 , 1111, as can remove 3 and 5
        listCount = {}
        result = False
        for i in range(0, len(list1)):
            if list1[i] not in listCount:
                listCount[list1[i]] = 1
            else :
                listCount[list1[i]] += 1
        set1 = set(list1)
        if (len(set1) == 1 and 1 in set1):
            result = True
        if (len(set1) == 2 and 1 in set1 and listCount[1] == 1):
            result = True
        


            
                
        if morediff == 0 and diff == 1:
            return True
        elif result == True:
            return True
        else :
            return False
                    