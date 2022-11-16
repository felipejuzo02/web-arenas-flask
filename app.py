from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO: trocar por BD
quadras = [
  {
    'id': 1,
    'name': 'Quadra do seu zé',
    'preco': 80
  },
  {
    'id': 2,
    'name': 'Fut7',
    'preco': 80
  },
  {
    'id': 3,
    'name': 'Arena 10',
    'preco': 80
  },
]

# Consultar
@app.route('/quadras', methods=['GET'])
def get_quadras():
    return jsonify(quadras)


# Consultar por id
@app.route('/quadras/<int:id>', methods=['GET'])
def get_quadra(id):
    for quadra in quadras:
        if quadra.get('id') == id:
            return jsonify(quadra)


# Alterar
@app.route('/quadras/<int:id>', methods=['PUT'])
def update_quadra(id):
    changed_quadra = request.get_json()

    for index, quadra in enumerate(quadras):
        if quadra.get('id') == id:
            quadras[index].update(changed_quadra)
            return jsonify(quadras[index])

# Criar
@app.route('/quadras', methods=['POST'])
def add_quadra():
    new_quadra = request.get_json()
    quadras.append(new_quadra)

    return jsonify(quadras)

# Deletar
@app.route('/quadras/<int:id>', methods=['DELETE'])
def delete_quadra(id):
    for index, quadra in enumerate(quadras):
        if quadra.get('id') == id:
            del quadras[index]
            
            return quadras

app.run(port=5000, host='localhost', debug=True)