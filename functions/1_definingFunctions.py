def main():
    try:
        moveObject(45)
    except TypeError as e:
        print("Could not initiate: ",e)

#None is a singleton, a special object and it can be test its identify
def moveObject(n,x=None):
    if x is None:
        x = 76 #x will have a default value and it will be displayed.
    print ("{} {}".format(n,x))
if __name__ == '__main__':
    main()