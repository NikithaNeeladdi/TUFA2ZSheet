    """_summary_
    Pattern 2
Difficulty: EasyAccuracy: 60.56%Submissions: 53K+Points: 2
Geek is very fond of patterns. Once, his teacher gave him a pattern of triangle to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a triangle pattern using stars(*).

 

Example 1:

Input:
n = 5
Output:
* 
* * 
* * * 
* * * * 
* * * * *
Example 2:

Input: 
n = 6
Output:
* 
* * 
* * * 
* * * * 
* * * * *
* * * * * *
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes an integer n  as the input parameter and prints the pattern accordingly.

Expected Time Complexity : O(n2)
Expected Auxilary Space : O(1)

Constraints:
1<= n <= 1000


    """
class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1,N+1):
            print('* '*i)