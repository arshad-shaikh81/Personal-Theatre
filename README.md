# 🎬 Movie Theatre Booking System

A beginner-friendly terminal-based movie theatre seat booking system built with **Python**.
Supports multiple movies, real-time seat tracking, input validation, and auto-generated invoices.

---

## 🎥 Movies Available

| No. | Movie |
|-----|-------|
| 1   | Matrubhumi |
| 2   | Toxic |
| 3   | King |

---

## ✨ Features

- 🎬 Choose from 3 different movies
- 💺 5x5 seating grid (25 seats per movie)
- 🙍 Customer name validation (1–5 letters only)
- ✅ Real-time seat availability tracking
- 🚫 Duplicate seat booking prevention
- 🧾 Auto-generated invoice (only for successful bookings)
- 👥 Multiple customer bookings in one session
- 🔄 Continue or exit after each booking

---

## 🧾 Invoice Includes

- Customer Name
- Date & Time of booking
- Movie Name
- Row, Seat Number & Seat Code
- Booking Status

---

## 🚀 How to Run

### 1. Clone the repository
git clone https://github.com/your-username/movie-theatre-booking-system.git

### 2. Navigate to the folder
cd movie-theatre-booking-system

### 3. Run the program
python booking.py

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed (only built-in `datetime`)

---

## 📁 Project Structure

movie-theatre-booking-system/
│
├── booking.py       # Main booking program
└── README.md        # Project documentation

---

## 📸 Sample Output

🎬 WELCOME TO MOVIE THEATRE
==================================
  Select a Movie:
  1 --> Matrubhumi
  2 --> Toxic
  3 --> King
==================================

==========================================
          🎬 MOVIE THEATRE INVOICE          
==========================================
  Customer Name  : Roman
  Date           : 05-06-2026
  Time           : 07:09:58 PM
------------------------------------------
  Movie          : Toxic
  Row            : E
  Seat No.       : 3
  Seat Code      : E3
  Status         : ✅ CONFIRMED
==========================================
     Thank you for booking with us! 🎟️
==========================================

---

## 👨‍💻 Author

Shaikh Arshad
- GitHub: https://github.com/arshad-shaikh81

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
