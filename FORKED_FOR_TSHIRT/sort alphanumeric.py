s=input()
l1=list('a b c d e f g h i j k l m n o p q r s t u v w x y z'.split())
l2=list('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split())
l3='1,3,5,7,9'.split(',')
l4='0,2,4,6,8'.split(',')
l5=[]
l6=[]
l7=[]
l8=[]
for i in range(len(s)):
    if s[i] in l1:
        l5.append(s[i])
    elif s[i] in l2:
        l6.append(s[i])
    elif s[i] in l3:
        l7.append(s[i])
    elif s[i] in l4:
        l8.append(s[i])
print(*sorted(l5),*sorted(l6),*sorted(l7),*sorted(l8),sep='')
