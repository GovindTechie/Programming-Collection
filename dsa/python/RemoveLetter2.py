class Solution(object):
    def equalFrequency(self, word):
        # making a dictionary of frequency count of each character
        dict = {}
        for ch in word:
            if ch not in dict:
                dict[ch] = 1
            else:
                dict[ch] += 1

        # dictionary converted to list and sort it
        list1 = list(dict.values())
        list1.sort()

     
        # making dictionary of each same frequency count
        result = False
        listCount = {}
        for i in range(0, len(list1)):
            if list1[i] not in listCount:
                listCount[list1[i]] = 1
            else :
                listCount[list1[i]] += 1

        # main output logic is here

        set1 = set(list1)

        list2 = list(set1)
        list2.sort

        # solving proble of string like "aaaa" or "bac"
        if(len(list2) == 1):
            if(list2[0] == 1 or listCount[list2[0]] == 1):
                result = True
        
        # soving problem of string like "ddda", "aabbccd"
        if (len(list2) == 2):
            if(1 in list2 and listCount[1] == 1):
                result = True
        
        # soving problem like  "dddfffrrrr"
        if(len(list2) == 2 and list2[1] - list2[0] == 1):
            if(listCount[list2[1]] == 1):
                result = True
          
        # return the output 
        if result == True:
            return True
        else :
            return False
                    