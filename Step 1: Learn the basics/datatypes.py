"""
Data Type
Difficulty: BasicAccuracy: 51.63%Submissions: 37K+Points: 1
Geek is learning a new programming language. As data type forms the most fundamental part of a language, Geek is learning them with focus and needs your help.
Given a data type, help Geek in finding the size of it in byte.

Data Type - Character, Integer, Long, Float and Double

Example 1:

Input: Character
Output: 1
Explaination: For java it would be 2 bytes.
Example 2:

Input: Integer
Output: 4
 

Your Task:

Complete the function dataTypeSize() which takes a string as input and returns the size of the data type represented by the given string in byte unit.
Return -1 if the input data type is invalid.
"""

class Solution:
    def dataTypeSize(self, str):
        dir_datatypes = { 'Character': 1 , 'Integer' : 4 ,'Long' : 8 , 'Float': 4 , 'Double': 8 , "Short": 2}
        if str and (str in dir_datatypes.keys()):
            return dir_datatypes[str]
        return -1