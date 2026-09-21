from src.movies import get_movie_by_id, get_all_movies
bookings_db = []
TOTAL_SEATS = 100


def book_tickets(movie_id, ticket_count):
    movie = get_movie_by_id(movie_id)
    if not movie:
        return {"success": False, "message": "Фільм не знайдено"}

    booking_id = len(bookings_db) + 1
    new_booking = {
        "booking_id": booking_id,
        "movie_title": movie["title"],
        "movie_id": movie_id,
        "tickets": ticket_count
    }
    bookings_db.append(new_booking)
    return {"success": True, "booking": new_booking}


def get_all_bookings():
    return bookings_db


def cancel_booking(booking_id):
    global bookings_db
    for booking in bookings_db:
        if booking["booking_id"] == booking_id:
            bookings_db.remove(booking)
            return {"success": True, "message": f"Бронювання №{booking_id} скасовано"}
    return {"success": False, "message": "Бронювання не знайдено"}


def get_statistics():
    movies_count = len(get_all_movies())
    booked_tickets = sum([b["tickets"] for b in bookings_db])
    free_seats = TOTAL_SEATS - booked_tickets
    return {
        "movies_count": movies_count,
        "booked_tickets": booked_tickets,
        "free_seats": free_seats
    }


def calculate_discount(total_price, discount_code):
    if discount_code == "SAVE10":
        return total_price * 0.9
    return total_price