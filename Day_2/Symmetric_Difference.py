"""
================================================================
Questions
Given sets of integers, and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either or

but do not exist in both.

Input Format

The first line of input contains an integer,
.
The second line contains space-separated integers.
The third line contains an integer, .
The fourth line contains

space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output

5
9
11
12
==============================================================
""""


elements_M = int(input())
#M = input()
#M = M.split()

""" The set function converts the list into set and the map funciton 
converts the string input into integer when input is splitted by split function
Ex. using map and split "1 2 3" ==>[1,2,3]""" 

set_M = set(map(int,input().split()))
#set_M = set(M)
elements_N = int(input())
set_N = set(map(int,input().split()))
Sym_diff = sorted((set_M.difference(set_N)).union(set_N.difference(set_M)))
for i in range(0,len(Sym_diff)):
    print(Sym_diff[i])