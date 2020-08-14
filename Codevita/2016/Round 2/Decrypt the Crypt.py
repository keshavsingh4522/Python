'''
Statement

Walter uses multiple applications at his workplace. He was assigned a unique password of variable lengths for each application (maximum length being 10). The only common factor among them was that all the passwords were a combination of 10 distinct characters. Walter created an algorithm to encrypt these passwords and wrote the codes on his desk to avoid a situation in which he would not be able to recollect a password.

Given as an input, is an encoded password and a list of 10 unique characters. Write a program that obtains the password by reverting the algorithm used by Walter.

Algorithm used by Walter to encode his password is as follows:

  1.  Walter observes all his passwords and lists down every distinct character. He assigns an index value to each character from 0 to 9. (Note: This list will be provided as an input to the program). This list MUST contain 10 DISTINCT characters.
  2.  He then replaces every character in the password with the corresponding index value to convert the password to a 10 digit numeric value.
  3.  The leftmost digit in this number sequence is noted; let's say 'A'. Now, starting from the leftmost position, every digit in the number is added to the digit on its right. The last digit in the sequence is added to 'A'.
  4.  Step 3 provides new sequences of numbers. He then scans through each of the summations and if any of the summation results in a value greater than 9, it is subtracted by 10, and its position is noted (Say B).
  5.  He then lists every digit from 0 to 9 separated by '|' character and prepends each digit with its position in the sequence as noted in 'B'. The resulting sequence after this step is saved (Say C).
  6.  The encoded password would therefore be
    < value_of_C >||< contents_of_array_B  > < Value_of_A >


Decrypt the encrypted password that has been created by Walter using the above algorithm to compute the actual password! 

Print -1 if there is any error in the inputs. 

Input Format:

  1.  First line contains the encoded password as it should be according to Walter's algorithm
  2.  Second line contains 10 unique characters


Output Format:

Obtained password by reverting the algorithm. Print -1 if there is any error in the inputs.
Constraints: 

  1.  Second line of input MUST contain 10 DISTINCT characters.
  2.  Encoded password should be in format
    < value_of_C >|| < contents_of_array_B >


Sample Input and Output

Input1
0|1|2|43|14|5|6|7|308|29||0149
*Acf$Zd&T@

Output1
@@Z$$

Input2
0|1|2|43|14|5|6|7|308|29||0149
*Acf$Zd&T

Output2
-1



Explanation of Test Case 1:
    
NOTE: - The following are the steps used to encrypt the password. Your task is to reverse the logic and decrypt the encrypted string provided as input, and get back the clear-text password.

  1.  Consider input characters and its position

    Input character list:*Acf$Zd&T@
    Position            :0 1 2 3 4 5 6 7 8 9

    (Note: The character list will not contain more than 10 characters and each character must be unique)
  2.  Now replace the characters in the password with the position value of the respective character as defined in step 1, to convert the password into a numeric value.

    Password        :@@Z$$
    Numeric value   :9 9 5 4 4

    (Note: Remember leftmost value (Say A) = 9)
  3.  Starting from the left most position, add each digit to the digit on its right. Add the last digit with the first digit in the sequence

    Numeric value of password  : 9   9   5   4   4
    Addition                   : 18  14  9   8   13

  4.  For each addition result equal to or greater than 10, subtract it by 10 and note its position.

    Additive step output  : 18   14   9   8   13
    Selective subtraction : 8    4    9   8   3
    Numeric value         : 0    1            4

    (Note: Remember the selective subtraction step positions obtained (Say B) = 014)
  5.  The password will follow the following format

    Format: 0|1|2|3|4|5|6|7|8|9
  6.  Now, each number in this format is pre-appended with the positions of the occurrence of the respective number in the output obtained in selective subtraction step of Step 4.

    Encrypted password:  0|1|2|43|14|5|6|7|038|29

    (Note: Say C = 0|1|2|43|14|5|6|7|038|29)
  7.  The final encrypted password will be of the following format to account for the calculations performed in generating the encrypted password

    Encrypted password (format) : < C >||< B >< A >
    Encrypted password          : 0|1|2|43|14|5|6|7|308|29||0149


Explanation of Test Case 2:

Second line of input contains 9 characters only hence prints -1
'''
from collections import defaultdict
e_p,e_ps=input().split('||')
s=input()
if len(s)!=10 and len(set(s))!=10:
    print(-1)
else:
    A=defaultdict(list)
    C=defaultdict(list)
    A[0]=int(e_ps[-1])
    for i in e_p.split('|'):
        if len(i)>1:
            k=len(i)
            while k>1:
                C[int(i[k-2])]=int(i[-1])
                k-=1
    for i in e_ps[:-1]:
        C[int(i)]+=10
    for i in range(len(C)-1):
        A[i+1]=C[i]-A[i]
    for i in range(len(A)):
        print(s[A[i]],end='')