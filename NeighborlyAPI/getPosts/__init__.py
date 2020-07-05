import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from ..mongo_config import MongoConfig


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = MongoConfig.MONGO_CONNECTION_STRING
        client = pymongo.MongoClient(url)
        database = client[MongoConfig.MONGO_DATABASE]
        collection = database[MongoConfig.POSTS_COLLECTION]

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)