    """_summary_
    Pattern 6
Difficulty: BasicAccuracy: 65.67%Submissions: 43K+Points: 1
Geek is very fond of patterns. Once, his teacher gave him a  pattern to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a pattern.

 

Example 1:

Input: 5

Output:
1 2 3 4 5
1 2 3 4
1 2 3 
1 2  
1 

 

Your Task:

You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.

Constraints:

1<= N <= 20
    """
class Solution:
    def printTriangle(self, N):
        # temp = [ ]
        # Code here
        # for i in range(1,N+1):
        #     temp.append(str(i))
        
        # for i in range(N,0,-1):
        #     print(" ".join(temp))
        #     temp.pop()
        temp = ""
        for i in range(N,0,-1):
            for i in range(1,i+1):
                temp += str(i)+ " "
            print(temp)
            temp = ""
