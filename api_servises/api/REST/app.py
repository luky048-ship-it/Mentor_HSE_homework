# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример данных
items = [
    {'id': 1, 'name': 'Item One'},
    {'id': 2, 'name': 'Item Two'}
]

# Получение списка всех элементов
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Получение элемента по ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404

# Создание нового элемента
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    items.append(new_item)
    return jsonify(new_item), 201

# Обновление существующего элемента
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    for index, item in enumerate(items):
        if item['id'] == item_id:
            items[index] = updated_item
            return jsonify(updated_item)
    return jsonify({'message': 'Item not found'}), 404

# Удаление элемента
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)
