def main():
    multiArguments(56,78,54,"hello","python",one="python",movement="right")
def multiArguments(arg1,arg2,arg3,*args,**kwargs):
    # print(arg1,arg2,arg3,args,kwargs['one'])
    for k in kwargs:
        print(k)
if __name__ == '__main__':
    main()