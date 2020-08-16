'''
A computer scientist has developed an encryption algorithm. This algorithm takes two inputs - one plain word and another, a key. Characteristics of inputs are as below.

Plain word: It is a string consisting of lowercase alphabets only.

Key: It is a set of pairs of strings consisting of lowercase alphabets only. For each pair, first string is the plain word and second string is its secret word. The characters of these secret words are jumbled but lengths of Plain Word and Secret Word are equal.

This algorithm finds the secret characters for each character in the inputted plain word by using the key. Then it combines all the secret characters in the same order to form a string called the secret word. Finally output this secret word. Below table shows how secret characters can be obtained from the key.

Examples

Your task is to help him in implementing the algorithm as a computer program.

Note: It is guaranteed that all characters in the given plain word can be converted to secret characters by using the given key.

Note: It is guaranteed that one plain text can be converted to only one encrypted text.

Constraints
1 <= P <= 52000

1 <= N <= 26

1 <= Length of a plain word in pair <= 50000

1 <= Length of a secret word in pair <= 50000

Length (plain word) == Length (secret word)

Input
First line contains string P denoting the plain text.

Second line contains an integer N denoting number of key pairs.

Next N lines, each contain two space separated strings denoting plain text and key.

Output
Print the encrypted word.

Time Limit
1


Examples
Example 1

Input

load

3

app lol

old tip

odd itt

Output

piot

Explanation

""load"" is the plain word to be encrypted. Given Key contains 3 pairs of Plain word and Secret word combination. They are <""app"", ""lol"">, <""old"", ""tip""> and <""odd"", ""itt"">. From first pair, it's clear that the secret character of 'p' is 'l' and that of 'a' is 'o'. From third pair, it's clear that the secret character of 'd' is 't' and that of 'o' is 'i'. By using above findings, from second pair, it is clear that the secret character of 'l' is 'p'. Now we can build the secret word by replacing the characters of plain word by its corresponding secret characters as ""piot"".

Example 2

Input

a

1

a b

Output

b

Explanation

The word ""a"" is the plain word to be converted to secret word. The given key consists of only one plain word - secret word pair. i.e., <""a"", ""b"">. From this, it is clear that the secret character of 'a' is 'b', since there is only one character in both secret and plain words. So, the final output is ""b""."
'''

string = input()
f1 = []
f2 = []
for i in range(int(input())):
    l_1 = input().split()
    f1.append(l_1[0])
    f2.append(l_1[1])

dict1 = {}
dict2 = {}

for _ in ''.join(f1):
    dict1[_]=dict1.get(_,0)+1

for _ in ''.join(f2):
    dict2[_]=dict2.get(_,0)+1

f1 = []
f2 = []
for tup in sorted(dict2.items(), key = lambda x:x[1]):
    f2.append(tup[0])
for tup in sorted(dict1.items(), key = lambda x:x[1]):
    f1.append(tup[0])

result = ''
for i in range(len(string)):
    ind = f1.index(string[i])
    result += f2[ind]
print(result)
