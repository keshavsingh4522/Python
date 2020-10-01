from itertools import combinations

def binary():
    Bin_Dict = {} 
    for i in numbers:
        Bin_Dict[i] = bin(i)[2:].count('1')
    return Bin_Dict

def c():
    count = 0
    for i in range(1,len(numbers)+1):
        for j in combinations(numbers,i):
            number_of_ones = 0
            number_of_zeros = 0
            for elm in j:
                number_of_ones += Bin_Dict[elm]
                number_of_zeros += lar_bit-Bin_Dict[elm]
            if number_of_ones == number_of_zeros:
                count += 1
    return count

if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int,input().split()))
    
    lar = max(numbers)
    lar_bit = len(bin(lar)[2:]) #print upto places
    Bin_Dict = binary()

    ans = c()
    bin_ans = bin(ans)[2:]
    if len(bin_ans) != lar_bit:
        bin_ans = '0'*(lar_bit-len(bin_ans))+bin_ans
    print(bin_ans)
    
    
