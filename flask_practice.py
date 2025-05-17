from flask import Flask,  request, jsonify

app = Flask(__name__)

names_lst = []

@app.route("/")
def main():
    return "Hello to Names"

@app.route("/names", methods=['POST'])
def names():
    data = request.get_json()
    print(data)
    new_name = {"message": "Names Received", "received_data": data.get('first_name', "") + " " + data.get('last_name', "")}
    names_lst.append(new_name)
    return jsonify(new_name), 201


if __name__ == '__main__':
    app.run(debug=True)