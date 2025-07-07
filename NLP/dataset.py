import requests
import json
import csv

API_KEY = '65779aa6edd6aefbf5664d4255e3a14b'
BASE_URL = 'https://api.themoviedb.org/3'
GENRE_URL = f'{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US'
MOVIE_URL = f'{BASE_URL}/movie/popular'

# Get genre dictionary {id: name}
def get_genre_map():
    response = requests.get(GENRE_URL)
    data = response.json()
    return {genre['id']: genre['name'] for genre in data['genres']}

# Fetch movies from multiple pages
def fetch_movies(pages=20):
    genre_map = get_genre_map()
    movie_data = []

    for page in range(1, pages + 1):
        response = requests.get(f'{MOVIE_URL}?api_key={API_KEY}&language=en-US&page={page}')
        data = response.json()

        for movie in data['results']:
            title = movie.get('title', '')
            overview = movie.get('overview', '')
            genre_ids = movie.get('genre_ids', [])
            genres = [genre_map.get(gid, 'Unknown') for gid in genre_ids]

            movie_data.append({
                'title': title,
                'description': overview,
                'genres': ", ".join(genres)
            })

    return movie_data

# Save data to CSV
def save_to_csv(data, filename='movies_dataset.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'description', 'genres'])
        writer.writeheader()
        for item in data:
            writer.writerow(item)

if __name__ == '__main__':
    movies = fetch_movies(pages=10)  # Fetch data from first 10 pages
    save_to_csv(movies)
    print("✅ Movie dataset saved to 'movies_dataset.csv'")
