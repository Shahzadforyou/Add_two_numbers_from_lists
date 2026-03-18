class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.num1 = 0
        self.num2 = 0
        for i in l1:
            self.num1 = (self.num1*10) + i 
        for j in l2:
            self.num2 = (self.num2*10) + j 
        return l1+l2
    