import datetime

# Initialize seats
seats = []
for row in range(5):
    L_temp = []
    for col in range(5):
        L_temp.append("0")
    seats.append(L_temp)

alpha = ['A', 'B', 'C', 'D', 'E']

def display_theatre():
    print()
    print("       1   2   3   4   5")
    print("________________________")
    for row in range(5):
        print(alpha[row] + "-->", end=" ")
        for col in range(5):
            print(seats[row][col].ljust(6), end=" ")
        print()
    print()
    print("-------------------------- <- All Eyes this way ")
    print()

def print_invoice(Name, a, b):
    now = datetime.datetime.now()
    date_str = now.strftime("%d-%m-%Y")
    time_str = now.strftime("%I:%M:%S %p")

    print()
    print("=" * 38)
    print("        🎬 MOVIE THEATRE INVOICE        ")
    print("=" * 38)
    print(f"  Customer Name  : {Name}")
    print(f"  Date           : {date_str}")
    print(f"  Time           : {time_str}")
    print("-" * 38)
    print("        BOOKING DETAILS                ")
    print("-" * 38)
    print(f"  Row            : {a}")
    print(f"  Seat No.       : {b}")
    print(f"  Seat Code      : {a}{b}")
    print(f"  Status         : ✅ CONFIRMED")
    print("=" * 38)
    print("   Thank you for booking with us! 🎟️  ")
    print("=" * 38)

# ✅ Main loop — keeps running for multiple customers
while True:

    display_theatre()

    # Count available seats
    count = sum(1 for r in range(5) for c in range(5) if seats[r][c] == "0")
    print(f"🪑 {count} Seats are available\n")

    # Stop if theatre is full
    if count == 0:
        print("🚫 Sorry! Theatre is fully booked. No seats available.")
        break

    # Name validation
    while True:
        Name = input("Enter your name (1 to 5 letters): ").strip()
        if 1 <= len(Name) <= 5 and Name.isalpha():
            break
        elif len(Name) == 0:
            print("❌ Name cannot be empty.")
        elif not Name.isalpha():
            print("❌ Letters only. No numbers or symbols.")
        else:
            print("❌ Name must be 1 to 5 letters long.")

    # Row validation
    while True:
        a = input("Enter a sitting Row (A-E): ").strip().upper()
        if a in alpha:
            break
        print("❌ Invalid row. Please enter A to E.")

    # Seat number validation
    while True:
        try:
            b = int(input("Enter a seat no. (1-5): "))
            if 1 <= b <= 5:
                break
            print("❌ Seat number must be between 1 and 5.")
        except ValueError:
            print("❌ Please enter a valid number.")

    row = alpha.index(a)
    col = b - 1

    # Book the seat
    if seats[row][col] != "0":
        print("⚠️  SORRY! That seat is already booked. Try another seat.")
    else:
        seats[row][col] = Name
        print("✅ Successfully! Your ticket is booked")
        print_invoice(Name, a, b)

    # Ask to continue or exit
    print()
    again = input("👉 Do you want to book another seat? (yes/no): ").strip().lower()
    if again != "yes":
        print()
        print("👋 Thank you for visiting! Enjoy the movie! 🎬")
        break