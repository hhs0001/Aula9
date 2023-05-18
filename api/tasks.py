from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from settings import books_collection

books_blueprint = Blueprint('books', __name__)

# Inserir um livro (C)
@books_blueprint.route('/books', methods=['POST'])
def create_book():
    book = request.get_json()
    result = books_collection.insert_one(book)
    book['_id'] = str(result.inserted_id)
    return jsonify(book), 201

# Listar todos os livros (R)
@books_blueprint.route('/books', methods=['GET'])
def get_books():
    books = []
    for book in books_collection.find():  # filtrando os livros
        book['_id'] = str(book['_id'])
        books.append(book)
    return jsonify(books), 200

# Alterar um livro (U)
@books_blueprint.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.get_json()
    updated_book.pop('_id', None)  # Remove o campo '_id' se estiver presente
    books_collection.update_one({'_id': ObjectId(book_id)}, {'$set': updated_book})
    return jsonify(updated_book), 200

# Remover um livro (D)
@books_blueprint.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    books_collection.delete_one({'_id': ObjectId(book_id)})
    return jsonify({'result': 'Book deleted'}), 200
