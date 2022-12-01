from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
import models as models

app = Flask(__name__)

INSERT_USER = (
    "INSERT INTO tb_users (name, phone, email, document, password, city, superuser) VALUES (%s, %s, %s, %s, %s, %s, %s);"
)

SELECT_USER = (
    "SELECT * FROM tb_users WHERE email = %s AND password = %s"
)

SELECT_ALL_USERS = (
    "SELECT u.id, u.name, u.phone, u.email, u.document, c.name AS city FROM tb_users u, tb_city c WHERE u.city = c.id ORDER BY id"
)

SELECT_USER_BY_ID = (
    "SELECT * FROM tb_users WHERE id = %s"
)

DELETE_USER = (
    "DELETE FROM tb_users WHERE id = %s"
)

SELECT_ALL_ARENAS = (
    "SELECT a.id, a.name, a.category, a.price, c.name AS city FROM tb_city c, tb_arenas a WHERE c.id = a.city"
)

INSERT_ARENAS = (
    "INSERT INTO tb_arenas (name, price, category, city) VALUES (%s, %s, %s, %s);"
)

DELETE_ARENA = (
    "DELETE FROM tb_arenas WHERE id = %s"
)

SELECT_CITY = (
    "SELECT * FROM tb_city"
)

INSERT_CITY = (
    "INSERT INTO tb_city (id, name, state) VALUES (%s, %s, %s)"
)

SELECT_ARENAS_RP = (
    "SELECT * FROM tb_arenas_ribeirao"
)

con = models.connection()
cursor = con.cursor()
cursor.execute(models.model_city())
cursor.execute(models.model_arenas())
cursor.execute(models.model_users())
cursor.execute(models.model_arenas_ribeirao())
con.commit()
con.close()

# Login
@app.route('/login', methods=['GET'])
def login():
    try:
        con = models.connection()
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        with con:
            with con.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(SELECT_USER, (username, password))
                result = cursor.fetchall()

        return jsonify(result)

    except Exception as error:
        print('Ocorreu um erro ao realizar a requisição')
        print(error)
    finally:
        con.close()

# USERS ------------------------------
@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        con = models.connection()
        cursor = con.cursor()
        cursor.execute(DELETE_USER, (str(id)))
        con.commit()
        con.close()
        return {"message": "Excluido com sucesso", "code": 201}, 201
    except Exception as error:
        return {"message": error}

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        try:
            con = models.connection()

            cursor = con.cursor(cursor_factory=RealDictCursor)

            cursor.execute(SELECT_ALL_USERS)
            results = cursor.fetchall()

            return jsonify(results)

        except Exception as error:
            print('Ocorreu um erro ao realizar a requisição')
            print(error)
        finally:
            con.close()
    else:
        try:
            con = models.connection()
            data = request.get_json()
            name = data["name"]
            phone = data["phone"]
            email = data["email"]
            document = data["document"]
            password = data["password"]
            city = data["city"]
            superuser = True

            try:
                with con:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute(INSERT_USER, (name, phone, email, document, password, city, superuser))
                        except Exception as error:
                            return {"message": "Erro ao adicionar", "code": 400, "error": error}, 400

                con.commit()
                return {"message": "Usuário adicionado com sucesso!!", "code": 201}, 201

            except Exception as error:
                print(error)
                return 'Deu erro'
        except Exception:
            print('Deu erro')

@app.route('/user/<int:id>', methods=['GET'])
def get_single_user(id):
    try:
        con = models.connection()

        cursor = con.cursor(cursor_factory=RealDictCursor)

        cursor.execute(SELECT_USER_BY_ID, (str(id)))
        results = cursor.fetchall()

        return jsonify(results[0])
    except Exception as error:
        print('Ocorreu um erro ao carregar seus dados')
        print(error)
    finally:
        con.close()

@app.route('/user/<int:id>', methods=['PUT'])
def edit_user(id):
    try:
        con = models.connection()
        data = request.get_json()

        for key in data:
            cursor = con.cursor()
            cursor.execute(f"UPDATE tb_users SET {key} = '{data[key]}' WHERE id = {id}")
            con.commit()
            con.close()
            return {"user": "Excluido com sucesso", "code": 201}, 201
    except Exception as error:
        return { "message": error }

# ARENAS ------------------------------
@app.route('/arenas', methods=['GET', 'POST'])
def handle_arenas():
    try:
        if request.method == 'GET':
            con = models.connection()

            cursor = con.cursor(cursor_factory=RealDictCursor)

            cursor.execute(SELECT_ALL_ARENAS)
            results = cursor.fetchall()

            return jsonify(results)

        else:
            con = models.connection()
            data = request.get_json()
            name = data["name"]
            price = data["price"]
            category = data["category"]
            city = data["city"]
            
            try:
                with con:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute(INSERT_ARENAS, (name, price, category, city))
                        except Exception:
                            return {"message": "Erro ao adicionar", "code": 400}, 400

                con.commit()
                return {"message": "Adicionado com sucesso", "code": 201}, 201

            except Exception as error:
                print(error)
                return 'Deu erro'

    except Exception as error:
        print('Ocorreu um erro ao realizar a requisição')
        print(error)
    finally:
        con.close()

@app.route('/arena/<int:id>', methods=['DELETE'])
def delete_arena(id):
    try:
        con = models.connection()
        cursor = con.cursor()
        cursor.execute(DELETE_ARENA, (str(id)))
        con.commit()
        con.close()
        return {"message": "Excluido com sucesso", "code": 201}, 201
    except Exception as error:
        print(error)

# CITY
@app.route('/city', methods=['GET', 'POST'])
def handle_city():
    if request.method == 'GET':
        try:
            con = models.connection()

            cursor = con.cursor(cursor_factory=RealDictCursor)

            cursor.execute(SELECT_CITY)
            results = cursor.fetchall()

            return jsonify(results)

        except Exception as error:
            print('Ocorreu um erro ao realizar a requisição')
            print(error)
        finally:
            con.close()
    else:
        try:
            con = models.connection()
            data = request.get_json()
            name = data["name"]
            state = data["state"]
            city_id = name.replace(" ", "")[:4].lower()

            try:
                with con:
                    with con.cursor() as cursor:
                        try:
                            cursor.execute(INSERT_CITY, (city_id, name, state))
                        except Exception as error:
                            return {"message": "Erro ao adicionar", "error": str(error.args) }, 400

                con.commit()
                return {"message": "Cidade adicionada com sucesso!!", "code": 201}, 201

            except Exception as error:
                return {"error": str(error.args)}
        except Exception:
            print('Deu erro')

@app.route('/city/<id>', methods=['DELETE'])
def delete_city(id):
    try:
        con = models.connection()
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM tb_city WHERE id = '{id}'")
        con.commit()
        con.close()
        return {"message": "Excluido com sucesso", "code": 201}, 201
    except Exception as error:
        return {"message": "Erro ao excluir", "error": str(error.args)}

# ARENAS RIBEIRÃO PRETO
@app.route('/arenas-rp', methods=['GET', 'POST'])
def handle_arenas_rp():
    if request.method == 'GET':
        try:
            con = models.connection()

            cursor = con.cursor(cursor_factory=RealDictCursor)

            cursor.execute(SELECT_ARENAS_RP)
            results = cursor.fetchall()

            return jsonify(results)

        except Exception as error:
            print('Ocorreu um erro ao realizar a requisição')
            print(error)
        finally:
            con.close()
    else:
        try:
            con = models.connection()
            data = request.get_json()
            for i in data:
                print(i)
            try:
                with con:
                    with con.cursor() as cursor:
                        try:
                            for arena in data:
                                cursor.execute(f"INSERT INTO tb_arenas_ribeirao (name) VALUES ('{arena}');")
                        except Exception as error:
                            print(error)
                            return {"message": "Erro ao importar", "error": str(error.args) }, 400

                con.commit()
                return {"message": "Arenas importadas com sucesso!!", "code": 201}, 201

            except Exception as error:
                return {"error": str(error.args)}
        except Exception:
            print('Deu erro')

app.run(port=5000, host='localhost', debug=True)