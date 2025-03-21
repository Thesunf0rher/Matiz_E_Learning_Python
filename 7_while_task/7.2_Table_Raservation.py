table_reservation = int(input("How many seats do you want to reserve a table for?"))

if table_reservation > 8:
    print("You'll have to wait")
else:
    print(f"The table is ready, {table_reservation}")