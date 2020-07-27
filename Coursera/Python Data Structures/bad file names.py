f=input('Enter file name: ')
try:
    file=open(f,'r')
except:
    print('file can not be opend: ',f)
    quit()
print('file opened successfully')
file.close()