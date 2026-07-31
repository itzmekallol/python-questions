"""
Q12: Movie Ticket Booking System.

Classes: Movie, Theater, Seat, Booking.
Features: display movies, book seats, cancel booking, prevent double
booking.

Run with: python main.py
"""


class Movie:
    def __init__(self, movie_id, title, duration_minutes):
        self.movie_id = movie_id
        self.title = title
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"{self.title} ({self.duration_minutes} min)"


class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False


class Theater:
    def __init__(self, name, movie, total_seats=10):
        self.name = name
        self.movie = movie
        self.seats = {f"S{i}": Seat(f"S{i}") for i in range(1, total_seats + 1)}

    def available_seats(self):
        return [seat.seat_number for seat in self.seats.values() if not seat.is_booked]


class Booking:
    _next_booking_id = 1

    def __init__(self, customer_name, theater, seat_numbers):
        self.booking_id = Booking._next_booking_id
        Booking._next_booking_id += 1
        self.customer_name = customer_name
        self.theater = theater
        self.seat_numbers = seat_numbers
        self.cancelled = False

    def __str__(self):
        status = "Cancelled" if self.cancelled else "Confirmed"
        return (f"Booking[{self.booking_id}] {self.customer_name} - "
                f"{self.theater.movie.title} - Seats {self.seat_numbers} ({status})")


class BookingSystem:
    def __init__(self):
        self.theaters = []
        self.bookings = []

    def add_theater(self, theater):
        self.theaters.append(theater)

    def display_movies(self):
        return [f"{theater.name}: {theater.movie}" for theater in self.theaters]

    def book_seats(self, customer_name, theater, seat_numbers):
        # Prevent double booking: check every requested seat is currently free
        for seat_number in seat_numbers:
            seat = theater.seats.get(seat_number)
            if seat is None:
                return None, f"Error: seat {seat_number} does not exist"
            if seat.is_booked:
                return None, f"Error: seat {seat_number} is already booked"

        for seat_number in seat_numbers:
            theater.seats[seat_number].is_booked = True

        booking = Booking(customer_name, theater, seat_numbers)
        self.bookings.append(booking)
        return booking, "Booking successful"

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id and not booking.cancelled:
                for seat_number in booking.seat_numbers:
                    booking.theater.seats[seat_number].is_booked = False
                booking.cancelled = True
                return f"Booking {booking_id} cancelled"
        return "Booking not found or already cancelled"


def main():
    print("Q12: Movie Ticket Booking System")

    movie1 = Movie("M1", "Galactic Odyssey", 142)
    theater1 = Theater("Screen 1", movie1, total_seats=8)

    system = BookingSystem()
    system.add_theater(theater1)

    print("Now showing:")
    for entry in system.display_movies():
        print("-", entry)

    booking1, msg1 = system.book_seats("Arjun", theater1, ["S1", "S2"])
    print("\n" + msg1)
    print(booking1)

    booking2, msg2 = system.book_seats("Neha", theater1, ["S2", "S3"])  # S2 already taken
    print("\n" + msg2)

    print("\nAvailable seats now:", theater1.available_seats())

    print("\n" + system.cancel_booking(booking1.booking_id))
    print("Available seats after cancellation:", theater1.available_seats())
    print(booking1)


if __name__ == "__main__":
    main()
