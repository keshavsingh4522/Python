# better method then sys module
import argparse as arg
parser=arg.ArgumentParser()
parser.add_argument('arg1',help='1st argument',type=int)
parser.add_argument('arg2',help='2nd argument',type=int)
args=parser.parse_args()
print('sum of these argment is: ',args.arg1+args.arg2)
# convert in dictionary by vars
print('dictionary is: ',vars(args))