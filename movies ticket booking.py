import csv

print("----MOVIE TICKET BOOKING----")

def show_movie():
    with open("movies.csv", "r") as file:
        reader = csv.reader(file)
        for rows in reader:
            movie_name = rows[0]
            total_seats = rows[1]
            seats_available = rows[2]
            print(f"{movie_name}, {total_seats}, {seats_available}")

def books_ticket():
    movie_input = input("Enter movie name: ").strip().lower()
    found = False

    with open("movies.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            movie_name = row[0].strip().lower()
            available = int(row[2])

            if movie_input == movie_name:
                found = True
                print("Movie available!")
                if available > 0:
                    print("Tickets are also available.")
                else:
                    print("Tickets are not available.")
                break  # Stop loop once movie found

    if not found:
        print("Movie not found.")

def update_seat():
    movie_to_book = input("Enter the movie name to book a ticket: ").strip().lower()
    updated_movies = []
    movie_found = False

    with open("movies.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # <-- IMPORTANT
        for row in reader:
            movie_name = row[0].strip().lower()
            total_seats = row[1]
            seats_available = int(row[2])

            if movie_name == movie_to_book:
                movie_found = True
                if seats_available > 0:
                    seats_available -= 1
                    print("Ticket booked successfully!")
                else:
                    print("Sorry, no seats available.")
            updated_movies.append([row[0], total_seats, str(seats_available)])

    if movie_found:
        with open("movies.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(updated_movies)
    else:
        print("Movie not found.")

# Menu
while True:
    print("\nMOVIES MENU")
    print("1. Show movies list")
    print("2. Book movie tickets")
    print("3. Update seats")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_movie()
    elif choice == 2:
        books_ticket()
    elif choice == 3:
        update_seat()
    elif choice == 4:
        print("Thanks for using Movie Ticket Booking System!")
        break
    else:
        print("Invalid input. Try again.")

                         