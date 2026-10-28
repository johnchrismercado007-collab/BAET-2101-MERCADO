total = 0
count = 0

while True:
    try:
    price = float(input("price (0 to stop) "))
 except ValueError:
    print ("Invalid input. please enrer a number.")
if price ==0:
   break

    total += price
    count += 1
if count > 0:
    average = total / count
    print(f"Items: {count)")
    print(f"Total: {total:.2f)")
    print("f"average: {Average:.2f)")
else 
    print("No items  were entered.")
