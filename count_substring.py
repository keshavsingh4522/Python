def count_substring(string, substring):
    count = 0
    for x in range(len(string)):
        if string[x:len(substring)+x] == substring:
            count += 1
        else: 
            continue
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
