from src.movies import get_all_movies, add_movie, search_movies_by_title
from src.booking import book_tickets, get_all_bookings, cancel_booking, get_statistics, calculate_discount
from src.favorites import add_to_favorites, get_favorites


def show_menu():

    print("\n=== ГОЛОВНЕ МЕНЮ ===")
    print("1] Перегляд фільмів")
    print("2] Бронювання")
    print("3] Обрані фільми")
    print("4] Вихід")


def main():
    print("=== ДЕМОНСТРАЦІЯ РОБОТИ СИСТЕМИ ===")


    print("\n--- 1. Додавання та перегляд фільмів ---")
    add_movie("Dune: Part Two", "Sci-Fi", 166)
    for m in get_all_movies():
        print(f"[{m['id']}] {m['title']} ({m['genre']}) - {m['duration']} хв")


    print("\n--- 2. Пошук фільму за назвою 'dune' ---")
    search_results = search_movies_by_title("dune")
    for m in search_results:
        print(f"Знайдено: {m['title']}")


    print("\n--- 3. Бронювання квитків ---")
    book_tickets(movie_id=3, ticket_count=3)
    book_tickets(movie_id=1, ticket_count=2)
    for b in get_all_bookings():
        print(f"Бронювання №{b['booking_id']}: {b['movie_title']} — {b['tickets']} квитків")


    print("\n--- 4. Перевірка системи знижок ---")
    ticket_price = 200
    total = ticket_price * 3
    discounted_total = calculate_discount(total, "SAVE10")
    print(f"Ціна за 3 квитки: {total} грн. Зі знижкою 'SAVE10': {discounted_total} грн.")

    # 5. Обране
    print("\n--- 5. Робота з обраним ---")
    fav_res = add_to_favorites(3, "Dune: Part Two")
    print(fav_res["message"])
    print(f"ID фільмів у списку обраного: {get_favorites()}")

    # 6. Статистика (Rebase фіча)
    print("\n--- 6. Статистика кінотеатру ---")
    stats = get_statistics()
    print(f"Доступно фільмів: {stats['movies_count']}")
    print(f"Заброньовано квитків: {stats['booked_tickets']}")
    print(f"Вільних місць у залі: {stats['free_seats']}")

    # 7. Скасування бронювання
    print("\n--- 7. Скасування бронювання №1 ---
    cancel_res = cancel_booking(1)
    print(cancel_res["message"])

    show_menu()

    if __name__ == "__main__":
        main()