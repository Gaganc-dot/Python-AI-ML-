def ChkNum(Number):
    Result = Number % 2 == 0
    return Result

def main():    
    print("Enter Number")
    No1 = int(input())

    if ChkNum(No1):
        print("Number is Even")

    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()
    