from pony.orm import db_session, select
import flask.ext.restful as rest

from Todo.Models.models import *

from Todo import api

from flask import request, abort

#vyer, klassorienterat. get, put, delete.

@api.resource('/Todo/<int:id>')
class TodoResources(rest.Resource):

    def put(self, id):

        Todo = request.json.get("text", None)
        tag = request.json.get("tag", None)
        return {}

    def get(self):

        return {}

    def delete(self):

        return {}