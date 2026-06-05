import datetime

# Initialize seats for each movie separately
def create_seats():
    return [["0"] * 5 for _ in range(5)]

movies = {
    "1": {"name": "Matrubhumi", "seats": create_seats()},
    "2": {"name": "Toxic",      "seats": create_seats()},
    "3": {"name": "King",       "seats": create_seats()},
}

alpha = ['A', 'B', 'C', 'D', 'E']

def display_theatre(seats, movie_name):
    print()
    print(f"       🎬 {movie_name} - Seating Chart")
    print("        1      2      3      4      5")
    print("_" * 42)
    for row in range(5):
        print(alpha[row] + "-->", end=" ")
        for col in range(5):
            print(seats[row][col].ljust(6), end=" ")
        print()
    print()
    print("------------------------------------ <- All Eyes this way")
    print()

def print_invoice(Name, a, b, movie_name):
    now = datetime.datetime.now()
    date_str = now.strftime("%d-%m-%Y")
    time_str = now.strftime("%I:%M:%S %p")

    print()
    print("=" * 42)
    print("          🎬 MOVIE THEATRE INVOICE          ")
    print("=" * 42)
    print(f"  Customer Name  : {Name}")
    print(f"  Date           : {date_str}")
    print(f"  Time           : {time_str}")
    print("-" * 42)
    print("            BOOKING DETAILS                 ")
    print("-" * 42)
    print(f"  Movie          : {movie_name}")
    print(f"  Row            : {a}")
    print(f"  Seat No.       : {b}")
    print(f"  Seat Code      : {a}{b}")
    print(f"  Status         : ✅ CONFIRMED")
    print("=" * 42)
    print("     Thank you for booking with us! 🎟️     ")
    print("=" * 42)

# ✅ Main loop
while True:

    # Movie selection
    print()
    print("=" * 42)
    print("         🎬 WELCOME TO MOVIE THEATRE        ")
    print("=" * 42)
    print("  Select a Movie:")
    print("  1 --> Matrubhumi")
    print("  2 --> Toxic")
    print("  3 --> King")
    print("=" * 42)

    while True:
        movie_choice = input("Enter movie number (1/2/3): ").strip()
        if movie_choice in movies:
            break
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

    selected_movie = movies[movie_choice]["name"]
    selected_seats = movies[movie_choice]["seats"]

    display_theatre(selected_seats, selected_movie)

    # Count available seats
    count = sum(1 for r in range(5) for c in range(5) if selected_seats[r][c] == "0")
    print(f"🪑 {count} Seats available for {selected_movie}\n")

    # Stop if movie is fully booked
    if count == 0:
        print(f"🚫 Sorry! {selected_movie} is fully booked!")
        again = input("👉 Want to check another movie? (yes/no): ").strip().lower()
        if again != "yes":
            print()
            print("👋 Thank you for visiting! Enjoy the movie! 🎬")
            break
        continue

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
    if selected_seats[row][col] != "0":
        print("⚠️  SORRY! That seat is already booked. Try another seat.")
    else:
        selected_seats[row][col] = Name
        print(f"✅ Successfully! Your ticket for {selected_movie} is booked")
        print_invoice(Name, a, b, selected_movie)

    # Continue or exit
    print()
    again = input("👉 Do you want to book another seat? (yes/no): ").strip().lower()
    if again != "yes":
        print()
        print("👋 Thank you for visiting! Enjoy the movie! 🎬")
        break