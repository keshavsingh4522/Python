f=input('Enter file name: ')
try:
    file=open(f,'r')
except:
    print('File can not be opened: ',f)
    quit()
print('File opened successfully!')
file.close()
