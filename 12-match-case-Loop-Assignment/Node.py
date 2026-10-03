# Topic 1 — Basic Real-Life Choice Problems ---------------------------------------------------------------------------------------------------?
# Q=1 Food Ordering System --------------------------------------------------------------?
choice = int(input("Enter your choice => "))
match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case 4:
        print("Sandwich")
    case _:
        print("Invalid Menu Choice")


# Q=2  Mobile Settings ----------------------------------------------------------------------?
Setting = int(input("Enter your Setting => "))
match Setting:
    case 1:
        print("Wi-Fi")
    case 2:
        print("Bluetooth")
    case 3:
        print("Mobile Data")
    case 4:
        print("Airplane Mode")
    case _:
        print("Exit")


# Q=3 ATM Main Menu ----------------------------------------------------------------------------?
ATM = int(input("Enter your ATM Main Menu => "))
match ATM:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Change PIN")
    case _:
        print("Exit")


# Q=4 Traffic Signal --------------------------------------------------------------------------?
color = input("Enter Your Color =>")
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Singnal")




# Topic 2 — Practical Menu Systems  ------------------------------------------------------------------------------------------------------------------------?
# Q=5 Student Portal  --------------------------------------------------------------------------------?
choice = int(input("Enter Your choice => "))
match choice:
    case 1:
        print("Opening Profile")
    case 2:
        print("Opening Courses")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendance")
    case 5:
        print("Logging out")
    case _:
        print("Invalid choice")


# Q=6 Online Shopping Menu -----------------------------------------------------------------------?
choice = int(input("Enter Your choice => "))
match choice:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening  Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case _:
        print("Invalid choice")


# Q=7 Banking Service Selection ------------------------------------------------------------------?
choice = int(input("Enter Your choice => "))
match choice:
    case 1:
        print("Opening Account Balance")
    case 2:
        print("Opening  Mini Statement")
    case 3:
        print("Opening Fund Transfer")
    case 4:
        print("Opening Bill Payment")
    case 5:
        print("Opening Customer Support")
    case _:
        print("Invalid choice")


# Q=8 Movie Ticket Booking --------------------------------------------------------------------------?
choice = int(input("Enter Your choice => "))
match choice:
    case 1:
        print("Morning Show")
    case 2:
        print("Afternoon Show")
    case 3:
        print("Evening Show")
    case 4:
        print("Night Show")
    case _:
        print("Invalid choice")




# Topic 3 — String-Based Real-Life Problems --------------------------------------------------------------------------------------------------------------------------?
# Q=9 Weather Advice -----------------------------------------------------------------------------?
weather = input("Enter Your weather => ")
match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothes")
    case _:
        print("Unknown Weather")



# Q=10 Payment Method --------------------------------------------------------------------------?
payment = input("Enter Your payment => ")
match payment:
    case "upi":
        print("UPI Payment Selected")
    case "card":
        print("Card Payment Selected")
    case "cash":
        print("Cash Payment Selected")
    case "wallet":
        print("Wallet Payment Selected")
    case _:
        print("Invalid Payment Method")






