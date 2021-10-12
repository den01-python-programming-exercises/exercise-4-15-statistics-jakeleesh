from src.statistics import Statistics

def main():
    #write your code below this line
    total = Statistics()
    even = Statistics()
    odd = Statistics()
    print("Enter numbers: ")
    while True:
        num = int(input())
        if (num != -1):
            if (num % 2 == 0):
                total.add_number(num)
                even.add_number(num)
            else:
                total.add_number(num)
                odd.add_number(num)
        else:
            break
    print("Sum: " + str(total.sum()))
    print("Sum of even numbers: " + str(even.sum()))
    print("Sum of odd numbers: " + str(odd.sum()))

if __name__ == '__main__':
    main()
