from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host='localhost', port=27017, serverSelectionTimeoutMS=1000)
    db = mongo.company
    mongo.server_info()     # trigger exception if cannot connect to db
    print('DB connected.')
except Exception as ex:
    print(f'DB Connection Error - {ex}')


##############################################
@app.route('/users', methods=['GET'])
def get_users():
    try:
        data = list(db.users.find())
        for user in data:
            user['_id'] = str(user['_id'])
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                'message': 'cannot read users',
            }),
            status=500,
            mimetype='application/json'
        )

@app.route('/users', methods=['POST'])
def create_user():
    try:
        user = {
            'firstName': request.form['firstName'],
            'lastName': request.form['lastName']
        }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response=json.dumps({
                'message': 'user created',
                'id': f'{dbResponse.inserted_id}'
            }),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                'message': 'cannot create user',
            }),
            status=500,
            mimetype='application/json'
        )
##############################################


if __name__ == '__main__':
    app.run(port=80, debug=True)