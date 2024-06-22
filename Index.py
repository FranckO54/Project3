import argparse
import json
import os

DATA_FILE = 'Movies.json'

# load previews saved data #
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save Current data #

def save_data(data):
    with open(DATA_FILE, 't') as file:
        json.dump(data, file, indent=4)

# Implement New data #
def add_movie():
    data = load_data()
    new_movie = {
        "id": len(data) + 1,
        "title": input("Title: "),
        "director": input("Director: "),
        "year_released": int(input("Year Released: ")),
        "genre": input("Genre: ")
    }
    data.append(new_movie)
    save_data(data)
    print("Movie added.")

# Update Data #
    def update_movie():
        data = load_data()
        movie_id = int(input("Enter the ID of a movie to update:"))
        for movie in data:
            if movie["id"] == movie_id:
                movie["title"] = input("Title:")
                movie["director"] = input("Director:")
                movie["year_released"] = int(input("Year Released:"))
                movie["genre"] = input("Genre:")
                save_data(data)
                print("Movie has been Updated.")
                return
        print("Movie was not Found.")

# Movies deleted in Data # 
def delete_movie():
    data = load_data()
    movie_id = int(input("Enter the ID of a movie to delete"))
    data = [ movie for movie in data if movie["id"] != movie_id]
    save_data(data)
    print("Movie has been deleted.")

# Movies Viewed in Data #
def view_movies():
    data = load_data()
    for movie in data:
        print(movie)

#searching for movies #
def search_movies():
    data = load_data()
    search_term = input("Enter a search term: ").lower()
    results = [movie for movie in data if search_term in movie["title"].lower()]
    for movie in results:
        print(movie)
        
def main():
    parser = argparse.ArgumentParser(description="Organize your Movie collection.")
    parser.add_argument('command', choices=['add', 'update', 'delete','view','search'])
    args = parser.parse_args()

    if args.command =='add':
        add_movie()

    elif args.command =='add':
        update_movie()
    elif args.command == 'delete':
        delete_movie()
    elif args.command == 'view':
        view_movies()
    elif args.command == 'search':
        search_movies()

if _name_ == '__main__':
    main()
