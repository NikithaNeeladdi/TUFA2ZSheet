    """_summary_
    Star Diamond
Easy
40/40
Contributed by
80 upvotes
Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.

Example:
Input: ‘N’ = 3

Output: 

  *
 ***
*****
*****
 ***
  *
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1  <= N <= 20
Time Limit: 1 sec
Sample Input 1:
3
Sample Output 1:
  *
 ***
*****
*****
 ***
  *    
Sample Input 2 :
1
Sample Output 2 :
*
*
Python (3.10)
1234567891011
    pass
Last saved at 10:14 AM

    """
def nStarDiamond(n: int) -> None:
    # Write your code here.
    s_u = n-1
    s_d = 0
    for i in range(1,n+1):
        print(((s_u)*' ')+('*'*((2*i)-1)))
        s_u -= 1
    for i in range(n,0,-1):
        print(((s_d)*" ") + ("*"*((2*i)-1)))
        s_d += 1
    pass