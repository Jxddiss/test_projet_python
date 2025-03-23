import json
import os
# +VISIBLE
# Chemin du fichier JSON
BOOKS_FILE = 'resources/books.json'

def load_books() -> list:
    """Charge les livres depuis le fichier JSON"""
    # +TODO
    if not os.path.exists(BOOKS_FILE):
        return []
    
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    # -TODO

def save_books( books: list) -> None:
    """Sauvegarde les livres dans le fichier JSON"""
    # +TODO
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=2, ensure_ascii=False)
    # -TODO
# -VISIBLE

