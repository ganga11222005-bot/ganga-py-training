year = int(input("Enter the year:"))

if year % 4 == 0 and 100 % 4 != 0:
    print(f" {year} is leap year")

else:
    print(f" {year} is not leap year")