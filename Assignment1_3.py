def Add(Value1,Value2):
    res = Value1 + Value2
    return res

def main():
    print("Enter First Number")
    No1 = int(input())
    
    print("Enter Second Number")
    No2 = int(input())

    result = Add(No1,No2)

    print("Addition is :",result)

    return result

if __name__ == "__main__":
    main()
