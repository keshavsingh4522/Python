def detect_trio(dic):
    con=False
    for i in range(1,8,3):
        con=con or dic[i]==dic[i+1] and dic[i+1]==dic[i+2] and not(dic[i]==" " or dic[i]=="_")
    for i in range(1,4):
        con=con or dic[i]==dic[i+3] and dic[i+3]==dic[i+6] and not(dic[i]==" " or dic[i]=="_")
    con=dic[1]==dic[5] and dic[5]==dic[9] and not(dic[5]==" " or dic[5]=="_") or con
    con=dic[3]==dic[5] and dic[5]==dic[7] and not(dic[5]==" " or dic[5]=="_") or con
    if con:
        return True
    return False    
print('_1_|_2_|_3_')
print("_4_|_5_|_6_")
print(" 7 | 8 | 9 ")
dic={}
for i in range(1,10):
    dic[i]="_"
dic[7]=" "
dic[8]=" "
dic[9]=" "
game_on=True
i=0
gameon=True
while i<9 and gameon:
    if i%2==0:
        x=input("Enter Number Player 1 - ")
    else:
        x=input("Enter Number Player 2 - ")
    try:
        x=int(x)
        if x>9 or x<1 or not (dic[x]==" " or dic[x]=="_"):
            print('Please provide valid input')
            continue
        if i%2==0:
            dic[x]="x"
        else:
            dic[x]='o'
        i+=1
        print(f'_{dic[1]}_|_{dic[2]}_|_{dic[3]}_')
        print(f"_{dic[4]}_|_{dic[5]}_|_{dic[6]}_")
        print(f" {dic[7]} | {dic[8]} | {dic[9]} ")
        if detect_trio(dic):
            gameon=False
            print(f"Player {(i+1)%2+1} Won !!")
    except ValueError:
        print('Please provide integer input')
