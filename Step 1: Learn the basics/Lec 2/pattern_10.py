    """_summary_
    Rotated Triangle
Easy
0/40
Contributed by
74 upvotes
Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Rotated Triangle.

Example:
Input: ‘N’ = 3

Output: 

*
**
***
**
*
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1  <= N <= 20
Time Limit: 1 sec
Sample Input 1:
3
Sample Output 1:
*
**
***
**
*
Sample Input 2 :
1
Sample Output 2 :
*
    """
def nStarTriangle(n: int) -> None:
    # Write your code here.
    i =1
    up = 1
    down = 0
    if n ==1:
        print('*')
        return
    while i > 0:
        if up == 1:
            print('*'*i)
            i += 1
            if i == n:
                print('*'*i)
                up = 0
                down =1
                i = i-1
        if down == 1:
            print('*'*i)
            i =i-1
    pass