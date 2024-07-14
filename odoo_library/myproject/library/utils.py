import requests

GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes'

def fetch_book_data(isbn, api_key):
    params = {
        'q': f'isbn:{isbn}',
        'key': api_key
    }
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            book_info = data['items'][0]['volumeInfo']
            return {
                'title': book_info.get('title', 'No Title'),
                'authors': book_info.get('authors', ['Unknown Author']),
                'description': book_info.get('description', ''),
                'categories': book_info.get('categories', []),
                'image_url': book_info.get('imageLinks', {}).get('thumbnail', '')  # Get the image URL
            }
    return None

