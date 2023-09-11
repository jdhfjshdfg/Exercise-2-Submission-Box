# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sqlite3

# Read the file and copy to the list
with open("stephen_king_adaptations.txt", "r") as file:
    stephen_king_adaptations_list = file.readlines()

# Establish a connection to the SQLite database
conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

# create table
cursor.execute("CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (movieID INTEGER, movieName TEXT, movieYear INTEGER, imdbRating REAL)")

for line in stephen_king_adaptations_list:
    movieID, movieName, movieYear, imdbRating = line.strip().split(",")
    cursor.execute("INSERT INTO stephen_king_adaptations_table (movieID, movieName, movieYear, imdbRating) VALUES (?, ?, ?, ?)",
                   ((movieID), movieName, int(movieYear), float(imdbRating)))

# Commit the change and close the connection
conn.commit()
conn.close()

def search_movies(option):
    conn = sqlite3.connect("stephen_king_adaptations.db")
    cursor = conn.cursor()

    if option == 1:
        movie_name = input("Please enter the movie name you want to search for:")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
        movie = cursor.fetchone()
        if movie:
            print("Movie name：", movie[1])
            print("Movie year：", movie[2])
            print("Rating：", movie[3])
        else:
            print("No such movie exists in our database.")

    elif option == 2:
        movie_year = input("Please enter the movie year you want to search for：")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (int(movie_year),))
        movies = cursor.fetchall()
        if movies:
            for movie in movies:
                print("Movie name：", movie[1])
                print("Movie year：", movie[2])
                print("Rating：", movie[3])
        else:
            print("No movies were found for that year in our database.")

    elif option == 3:
        rating = float(input("Please enter rating limits:"))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating,))
        movies = cursor.fetchall()
        if movies:
            for movie in movies:
                print("Movie name：", movie[1])
                print("Movie year：", movie[2])
                print("Rating：", movie[3])
        else:
            print("No movies at or above that rating were found in the database.")

    conn.close()

# main
while True:
    print("Please select an action to perform：")
    print("1. Search movie name")
    print("2. Search movie year")
    print("3. Search for movies by rating")
    print("4. STOP")
    print("Please enter your options")
    option = int(input())

    if option == 4:
        print("The program has terminated.")
        break

    search_movies(option)