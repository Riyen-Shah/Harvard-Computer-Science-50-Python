AmountDue = 50
while AmountDue > 0:
    money = int(input("Insert coin: "))
    if money == 25 or money == 10 or money == 5:
        AmountDue -= money
        if AmountDue > 0:
            print(f"Amount Due: {AmountDue}")
    else:
        print(f"Amount Due: {AmountDue}")
if AmountDue <= 0:
    if AmountDue == 0:
        print(f"Change owed: {AmountDue}")
    elif AmountDue < 0:
        print(f"Change owed: {-AmountDue}")
