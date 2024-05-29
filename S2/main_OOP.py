import sys
choice = int(sys.argv[1])
if choice == 1:
    # First example
    import Class_ex1
    Apple_1 = Class_ex1.Apple("green", 150)
    Apple_1.size = 300
    print(Apple_1.size)
    print("Apple_1 is an Apple of color", Apple_1.color, "with a mass of", Apple_1.mass, "from", Apple_1.Country)
    Taste_of_my_Apple = Apple_1.taste("sweet")
    print(Taste_of_my_Apple)
    Apple_1.juice()
if choice == 2:
    # Static method
    import Class_method_bank_account as static

    # Creating instances of BankAccount
    account1 = static.BankAccount("ACC001", 1000)
    account2 = static.BankAccount("ACC002", 2000)
    print(account1)
    # Accessing total accounts count using class method
    #print("Total accounts:", static.BankAccount.get_total_accounts())  # Output: 2
    lemon1 = static.basiclemon("yellow", "standard")
    print(lemon1)


