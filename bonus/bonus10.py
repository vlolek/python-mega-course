try:
    widht = float(input("Enter widht: "))  
    length = float(input("Enter height: "))

    if widht == length:
        exit("That looks like a square.")

    area = widht * length
    print(area)
except ValueError:
    print("Please enter a number.")
     