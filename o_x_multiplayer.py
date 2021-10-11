def detect_trio(dic):
    con1=dic[3]==dic[1] and dic[1]==dic[2] and not(dic[1]==" " or dic[1]=="_")
    con2=dic[4]==dic[5] and dic[5]==dic[6] and not(dic[5]==" " or dic[5]=="_") or con1
    con3=dic[7]==dic[8] and dic[8]==dic[9] and not(dic[8]==" " or dic[8]=="_") or con2
    con4=dic[1]==dic[4] and dic[4]==dic[7] and not(dic[4]==" " or dic[4]=="_") or con3
    con5=dic[2]==dic[5] and dic[5]==dic[8] and not(dic[5]==" " or dic[5]=="_") or con4
    con6=dic[3]==dic[6] and dic[6]==dic[9] and not(dic[6]==" " or dic[6]=="_") or con5
    con7=dic[1]==dic[5] and dic[5]==dic[9] and not(dic[5]==" " or dic[5]=="_") or con6
    con8=dic[3]==dic[5] and dic[5]==dic[7] and not(dic[5]==" " or dic[5]=="_") or con7
    if con8:
        return True
    
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
    except:
        print('Please provide valid input')
