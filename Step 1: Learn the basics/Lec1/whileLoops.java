// While loop- printTable - Java
// Difficulty: EasyAccuracy: 52.74%Submissions: 43K+Points: 2
// While loop is another loop like for loop but unlike for loop it only checks for one condition.

// Here, we will use a while loop and print a number n's table in reverse order.

// Example 1:

// Input:
// 1

// Output:
// 10 9 8 7 6 5 4 3 2 1
// Example 2:

// Input:
// 2

// Output:
// 20 18 16 14 12 10 8 6 4 2
// User Task:
// Your task is to complete the provided function and print the table in reverse order (with space between the values).
// NOTE: As the code is checked against multiple test cases, the new line is necessary after every execution and the template code has taken care of that.

// Constraints:
// 1 <= n<= 1000

class Geeks {
	 static void printTable (int n) 
	 {
            int multiplier=10;
            while(multiplier>0)
            {
                System.out.print(multiplier*n+ " ") ;
                multiplier = multiplier-1 ;
            }
       System.out.println();
	 }
