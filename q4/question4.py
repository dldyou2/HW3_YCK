def factorial(n):
    if(n <= 1):
        return 1
    return n * factorial(n - 1)

def main():
    for n in range(0, 16, 2):
        print(f"{n} : {factorial(n)}")
if __name__ =="__main__":
    main()