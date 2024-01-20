from flask import Flask, request, jsonify

app = Flask(__name__)


# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "John Doe",
#         "email": "John.doe@example.com",
#     }

#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra

#     return jsonify(user_data), 200


# @app.route("/create-user", methods=["POST"])
# def create_user():
#     data = request.get_json()

#     return jsonify(data), 201

tmdb_api_key = "6561c9424e4ad6bc0f2f49bc9b283342"


@app.route("/")
def test():
    return jsonify({"name": "Petter"})


if __name__ == "__main__":
    app.run(debug=True)
