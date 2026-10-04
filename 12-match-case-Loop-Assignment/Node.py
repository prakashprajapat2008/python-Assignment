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


# Q=11 File Type Detector --------------------------------------------------------------------------?
File = input("Enter Your File => ")
match File:
    case "pdf":
        print("Document File")
    case "jpg" | "png":
        print("Image File")
    case "mp3":
        print("Audio File")
    case "mp4":
        print("Video File")
    case _:
        print("Unknown File Type")


# Q=12 User Role --------------------------------------------------------------------------------------?
Role = input("Enter Your Role =>")
match Role:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest":
        print("Limited Access")
    case _:
        print("Invalid Role")



# Topic 4 — Multiple Values Using | ------------------------------------------------------------------------------------------------------------------------------------------?
# Q=13  Weekday or Weekend ----------------------------------------------------------------------?
day = int(input("Enter Your Day =>"))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid")


# Q=14 Customer Support Priority ---------------------------------------------------------------?
priority = int(input("Enter Priority => "))
match priority:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
        print("Urgent Priority")
    case _:
        print("Invalid Priority")


# Q=15 Store Discount Category -------------------------------------------------------------------?
Category = int(input("Enter Category => "))
match Category:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("Invalid Membership")
  



# Topic 5 — Nested match-case -----------------------------------------------------------------------------------------------------------------?
# Q=16 University Portal  ------------------------------------------------------------------------?
user_type = int(input("Enter Your user type => "))
option = int(input("Enter Your option => "))
match user_type:
    case 1:
        print("student")
        match option:
            case 1:
                print("Opening courses")
            case 2:
                print("Opening marks")
            case 3:
                print("Opening attendance")
            case _:
                print("invalid")
    case 2:
        print("teacher")
        match option:
            case 1:
                print("Opening student")
            case 2:
                print("Opening marks")
            case 3:
                print("Opening attendance")
            case _:
                print("invalid")

    case _:
        print("Invalid User Type")


# Q=17 ATM with Account Type  --------------------------------------------------------------------------?
account = int(input("Enter Your account =>"))
Selected = int(input("Enter Your account Selected =>"))
match account:
    case 1:
        print("savings")
        match Selected:
            case 1:
                print("check balance")
            case 2:
                print("deposit")
            case 3:
                print("withdraw")
            case _:
                print("invalid deatils")
    case 2:
        print("current")
        match Selected:
            case 1:
                print("check balance")
            case 2:
                print("deposit")
            case 3:
                print("withdraw")
            case _:
                print("invalid deatils")
    case _:
        print("invalid account")


# Q=18 E-Commerce Application ------------------------------------------------------------------------------------------?
category = int(input("Enter Your category =>")) 
product= int(input("Enter Your product =>"))     
match category:
    case 1:
        print("Electronics") 
        match product:
            case 1:
                print("Mobile") 
            case 2:
                print("Laptop")  
            case 3:
                print("Headphones")   
            case _:
                print("invalid items")   
    case 2:
        print("Clothing")   
        match product:
            case 1:
                print("Shirt") 
            case 2:
                print(" Jeans")  
            case 3:
                print("Shoes")   
            case _:
                print("invalid items")  
    case _:
        print("invalid category")


# Q=19 Food Delivery Application  -------------------------------------------------------------------------?
Food = int(input("Enter Your Food category =>"))
Food_Type = int(input("Enter Your Foods =>"))
match Food:
    case 1:
        print("Vegetarian")
        match Food_Type:
            case 1:
                print("paneer")
            case 2:
                print("dal")
            case 3:
                print("veg biryani")
            case _:
                print("invalid food")
    case 2:
        print("Non-vegetarian")
        match Food_Type:
            case 1:
                print("chicken biryani")
            case 2:
                print("chicken curry")
            case 3:
                print("fish curry")
            case _:
                print("invalid food")

    case _:
        print("invalid category")
        



# Topic 6 — match-case with Simple Calculations ----------------------------------------------------------------------------------------------?
# Q=20 Simple Calculator  ------------------------------------------------------------------------?
A = int(input("Enter YOUR Numbers1 =>"))
B = int(input("Enter Your Numbers =>"))
Operators = input("Enter Your Operators(+,-,*,/) =>")
match Operators:
    case "+":
        print(A + B)  
    case "-":
        print(A - B) 
    case "*":
        print(A * B) 
    case "/":
        if B!=0:
            print(A / B)
        else:
            print("divide in zero")
    case _:
        print("invalid")
















    


    

