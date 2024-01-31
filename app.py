from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)


class Laptops(Resource):
    def get(self):
        data = pd.read_csv("laptops.csv")
        data = data.to_dict("records")
        return {"data": data}, 200

    def post(self):
        marka = request.args["marka"]
        model = request.args["model"]
        ram = request.args["ram"]
        depolama = request.args["depolama"]
        fiyat = request.args["fiyat"]
        req_data = pd.DataFrame(
            {
                "marka": [marka],
                "model": [model],
                "ram": [ram],
                "depolama": [depolama],
                "fiyat": [fiyat],
            }
        )
        data = pd.read_csv("laptops.csv")
        data = data.append(req_data, ignore_index=True)
        data.to_csv("laptops.csv", index=False)
        return {"message": "Record successfully added."}, 200


class Descriptions(Resource):
    def get(self):
        data = pd.read_csv("laptops.csv", usecols=[0, 1, 4])
        data = data.to_dict("records")
        return {"data": data}, 200


api.add_resource(Descriptions, "/desc")
api.add_resource(Laptops, "/lap")

if __name__ == "__main__":
    app.run(host="0.0.0.0")