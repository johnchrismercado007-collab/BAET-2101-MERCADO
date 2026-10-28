correct_pin = "1234"
max_tries = 3
tries = 0

while tries < mas_tries:
    pin = input("PIN: ")
    if pin  == correct_pin:
        print("Acces granted")
        break
    tries  += 1

    if tries == max_tries: 
        print( " Card blocked ")