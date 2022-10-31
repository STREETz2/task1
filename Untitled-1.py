from flask import *
import json

app= Flask(__name__)

@app.route('/', methods=['GET'])
def my_details():
    data_set ={'slackUsername':'STz','backend':True,'age': 26,'bio':'humble and Godfearing'}
    json_dump= json.dumps(data_set)

    return json_dump


    return json_dump


if __name__ == '__main__':
    app.run()
