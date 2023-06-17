def longest_palindrome(s):
    
    longest=''
    
    for i in range(len(s)):
        
        pal = centre(s,i,i)
        
        if len(pal) > len(longest):
            longest = pal
            
        pal = centre(s,i,i+1)
        
        if len(pal) > len(longest):
            longest = pal
            
    return longest

def centre(s,left,right):
    
    while left >=0 and right <len(s) and s[left] == s[right]:
        left -=1
        right +=1
        
    return s[left+1:right]

s=str(input())
print(longest_palindrome(s))