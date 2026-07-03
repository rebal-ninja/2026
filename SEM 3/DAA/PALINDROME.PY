class solution:
    def is_palindrome(self,x:int):
        
        while x<0:
            return False
        orginal = x 
        reverse = 0 

        while x>0:
            digit = x%10
            reverse = reverse*10+digit
            x=x//10

        if orginal== reverse:
            return True
        return False
        
sol = solution()
x= 124
print(sol.is_palindrome(x))