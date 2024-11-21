class Solution:
    def __init__(self):
        self.map = {}
    def isHappy(self, n: int) -> bool:
        # stopping condition is that its a multiple of 10 
        digits =[int(d)**2 for d in str(n)]
        if sum(digits)==1:
            return True
        if sum(digits) not in self.map.keys():
            self.map[sum(digits)] = digits
            return self.isHappy(sum(digits))
        else:
            return False
            

