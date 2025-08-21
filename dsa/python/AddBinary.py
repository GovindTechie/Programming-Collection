class Solution(object):
    def addBinary(self, a, b):
        a_int = 0
        pow = 0
        for i in reversed(range(len(a))):
            if a[i] == '1':
                a_int += 2**pow
            pow += 1

        pow = 0
        b_int = 0
        for i in reversed(range(len(b))):
            if b[i] == '1':
                b_int += 2**pow
            pow += 1

        result_value = a_int + b_int

        if result_value == 0:
            return '0'
        
        binary = ''
        while result_value > 0:
            remainder = result_value % 2
            binary = str(remainder) + binary
            result_value = result_value // 2
        
        return binary 

            
        
s1 = Solution()
a = "11"
b = "1"
print(f"Original Strings {a} & {b}")
print(f"Addition : {s1.addBinary(a, b)}")