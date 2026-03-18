class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.num1 = 0
        self.num2 = 0
        for i in l1:
            self.num1 = (self.num1*10) + i 
        for j in l2:
            self.num2 = (self.num2*10) + j 
        return self.num1 + self.num2
    
list1 = [1,2,3]
list2 = [4,5,6]
list1.reverse()
list2.reverse()

s1 = Solution()
result = s1.addTwoNumbers(list1,list2)
temp = str(result)
req_list =[]
for i in temp:
    req_list.append(int(i))
print(req_list)