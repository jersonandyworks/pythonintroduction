def main():
    for x in inclusiveRange(2,25,5):
        print(x,end=' ')
def inclusiveRange(*args):
    numArgs = len(args)
    if numArgs < 1:
        raise ValueError("You must have at least one paramenter")
    else:
        if numArgs == 1:
            start = 1
            stop = args[0]
            step = 1
        if numArgs == 2:
            start = args[0]
            stop = args[1]
            step = 1
        if numArgs == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        i = start
        while i <= stop:
            yield i
            i += step


if __name__ == '__main__':
    main()