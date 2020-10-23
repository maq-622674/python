import time
def main():
    a=[]
    b={
        "1":"2"
    }
    a.append(b)
    print(a)
    c={
        "1":"2",
        "2":"3"
    }
    d={
        "1":"2"
    }
    if c in a:
        print("123")
    if c not in a:
        print("456")
    
if __name__ == "__main__":
    main()