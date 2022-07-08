num = int(input("Enter a positive integer : \n "))
if num > 0 :
    def perfectNumber(num):
        sum = 0
        for i in range(1,num):
            if (num % i) == 0:
                sum+=i
        if sum == num :
            print(f"{num} is a perfect number ")
        else:
            print(f"{num} is not a perfect number")
    perfectNumber(num)

else:
    print("input positive integer")
