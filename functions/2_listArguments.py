def main():
    multiArguments(1,4,8,67,45,"hh",78)
def multiArguments(arg1,arg2,arg3,*args):
    print(arg1,arg2,arg3,args)
    for arg in args:
        print(arg,end=' ')
if __name__ == '__main__':
    main()