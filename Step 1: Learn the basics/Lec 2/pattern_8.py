    """_summary_
    Pattern 8
Difficulty: BasicAccuracy: 63.56%Submissions: 33K+Points: 1
Geek is very fond of patterns. Once, his teacher gave him a  pattern to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a pattern.

 

Example 1:

Input: 5

Output:

*********
 *******
  *****
   ***
    *

Your Task:

You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.

Constraints:

1<= N <= 20
    """
class Solution:
    def printTriangle(self, N):
        # Code here
        spaces = 0
        for i in range(N,0,-1):
            print((spaces*" ")+("*")*((2*i)-1))
            spaces += 1
