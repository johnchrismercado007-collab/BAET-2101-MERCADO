while True:
    try:
        n = int (input("Enter n "))
        if n > 0:
            break
     print ("please enter a 
        positive number.")
    except ValueError:
      print ("Invalid input. please enter an integer.")
    countdown_list =[]
    for i in range (n, 0, -1):
        countdown_list. append (str(1))
    print (" ".join(countdown_list + " liftoff!")