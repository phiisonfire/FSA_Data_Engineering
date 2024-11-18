import requests

API_URL = 'https://tiki.vn/api/personalish/v1/blocks/listings'
API_DETAILS_URL = 'https://tiki.vn/api/v2/products/'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

BOOK_IDS = [
    42230121, 74460137, 273385286, 187827003, 263070154, 166192600, 48752755, 105663942,
    381234, 48323805
]

def fetch_data_by_book_id(id):
    try:
        print(f"Fetching data for book id: {id}")
        url = f"{API_DETAILS_URL}{id}"
        response = requests.get(url=url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return {
            'id': data.get('id'),
            'name': data.get('name'),
            'price': data.get('price', 0),  # Default to 0 if 'price' key is not present
            'quantity_sold': data.get('quantity_sold', {}).get('value', 0),  # Nested get
            'category_id': data.get('categories', {}).get('id'),
            'category': data.get('categories', {}).get('name'),
            # 'authors': data.get('authors')  # Uncomment if needed
        }
    except requests.RequestException as e:
        print(f"Failed to fetch data from API: {e}")
        return None
    
def fetch_all_book_data_with_ids():
    books = []
    for id in BOOK_IDS:
        book = fetch_data_by_book_id(id=id)
        books.append(book)
    return books