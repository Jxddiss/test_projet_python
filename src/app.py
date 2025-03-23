from flask import Flask, jsonify, request, abort
from utils.data_manager import load_books, save_books


app = Flask(__name__)

# +VISIBLE
@app.route('/books', methods=['GET'])
def get_books():
    """Récupère tous les livres"""
    # +TODO
    books = load_books()
    return jsonify(books)
    # -TODO

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    """Récupère un livre par son ID"""
    # +TODO
    books = load_books()
    book = next((b for b in books if b['id'] == id), None)
    
    if not book:
        abort(404, description="Livre non trouvé")
    return jsonify(book)
    # -TODO

@app.route('/books', methods=['POST'])
def add_book():
    """Ajoute un nouveau livre"""
    # +TODO
    if not request.is_json:
        abort(400, description="Les données doivent être au format JSON")
    
    data = request.get_json()
    required_fields = ['title', 'author', 'year']
    
    if not all(field in data for field in required_fields):
        abort(400, description="Données incomplètes")
    
    books = load_books()
    new_id = max(b['id'] for b in books) + 1 if books else 1
    
    new_book = {
        'id': new_id,
        'title': data['title'],
        'author': data['author'],
        'year': data['year']
    }
    
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201
    # -TODO

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    """Met à jour un livre existant"""
    # +TODO
    if not request.is_json:
        abort(400, description="Les données doivent être au format JSON")
    
    data = request.get_json()
    books = load_books()
    book = next((b for b in books if b['id'] == id), None)
    
    if not book:
        abort(404, description="Livre non trouvé")
    
    # Mise à jour des champs fournis
    updates = {
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author']),
        'year': data.get('year', book['year'])
    }
    
    book.update(updates)
    save_books(books)
    return jsonify(book)
    # -TODO

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    # +TODO
    """Supprime un livre"""
    books = load_books()
    book = next((b for b in books if b['id'] == id), None)
    
    if not book:
        abort(404, description="Livre non trouvé")
    
    books.remove(book)
    save_books(books)
    return jsonify({'message': 'Livre supprimé avec succès'}), 200
    # -TODO

# -VISIBLE
if __name__ == '__main__':
    app.run(debug=False)