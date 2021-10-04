# Define the find_Novowels function here
def find_Novowels(inp_str):
    # vowel=['a','e','i','o','u']
    vowel = "aeiou"
    n = len(inp_str)
    sl = []

    for i in range(0, n):
        p = inp_str[i]
        s = "".join(p)
        plist = list(p)
        p_l = len(plist)
        #count = [each for each in s if each in vowel]
        #x = len(count)
        count=0
        for i in range(0,p_l):
            if(plist[i]=='a' or plist[i]=='e' or plist[i]=='i' or plist[i]=='o' or plist[i]=='u'):
                count+=1
        if (count > 1):
            pass
        else:
            sl.append(p)
    return sl


# Sample main section.
# Do not remove the below portion of code.
if __name__ == '__main__':
    count = int(input())
    inp_str = []
    for i in range(count):
        inp_str.append(input())
    output = find_Novowels(inp_str)
    if len(output) != 0:
        print('Strings without vowels:')
        for i in output:
            print(i)
    else:
        print('No string found')
