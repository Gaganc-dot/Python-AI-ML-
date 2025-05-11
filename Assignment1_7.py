def div(Value):
    res = Value % 5 == 0
    return res

def main():

    print("Enter number to be checked if divisible")

    No = int(input())

    if  div(No):
        print("True")

    else:
        print("False")

if __name__ == "__main__":
    main()
