import json

from typing import Any

from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> json.JSONEncoder | str:
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)