def generate_multiplication_table():
    
        number = int(input("Enter a number: "))
        if number <= 0:
            print("Please enter a positive number.")
            return
        
        table = []
        for i in range(1, number + 1):
            row = [i * j for j in range(1, i + 1)]
            table.append(row)

        for row in table:
            print(row)
    
generate_multiplication_table()
