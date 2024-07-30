    """_summary_
    Pattern 7
Difficulty: BasicAccuracy: 62.43%Submissions: 39K+Points: 1
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Ram an integer n and asked him to build a pattern.
Help Ram build a pattern.

Example 1:

Input: 5
Output:
    *
   ***  
  *****
 *******
*********
Example 2:

Input: 3
Output:
  *
 ***  
*****
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes an integer n  as the input parameter and prints the pattern.

Expected Time Complexity: O(n2).
Expected Auxiliary Space: O(1)

Constraints:
1<= n <= 1000
    """
class Solution:
    def printTriangle(self, N):
        # Code here
        spaces =  N-1
        for i in range(1, N+1):
            if spaces >=0:
                print((" "*spaces)+(("*")*((2*i)-1)))
            spaces -= 1
             