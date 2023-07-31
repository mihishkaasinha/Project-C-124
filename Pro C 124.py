from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = {
    "data": [
    {
        "Contact":"9846699901",
        "Name":"Arnav",
        "done": "false",
        "id":1
    },
    {
        "Contact":"9747389631",
        "Name":"Yjurv",
        "done": "false",
        "id":2
    }
]
}
@app.route('/get-data')
def gettask():
    return jsonify({"data":contacts})

@app.route('/add-data', methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({
                        "status":"error",
                        "message":"Please provide the data"
                        }), 400
    contact = {
        "id": contacts[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "Done": False
    }
    contacts.append(contact)
    return jsonify({
                    "status":"succsess",
                    "message":"Task added"
                    }), 100
if __name__ == "__main__":
    app.run()