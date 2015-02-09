from pony.orm import db_session, select
import flask.ext.restful as rest
import json

from Todo.Models.models import *

from Todo import api

from flask import request, abort

#vyer, klassorienterat. get, put, delete.

@api.resource('/Todo/<int:id>')
class Todos(rest.Resource):

    def put(self, id):


        input = json.loads(request.data)        #Hamtar input

        with db_session:                        #Startar session
            item = Todo(data=input['data'])

            for tag_name in input['tags']:
                tag = Tag.get(name=tag_name)    #Forsoker forst hamta tag med hjalp av Tag.get()
                if tag is None:                 #Skapar ny tag om Tag.get returnerar None.
                    tag = Tag(name=tag_name)
                item.tags += tag

        return {}, 200

    def get(self):
        with db_session:
            return {
                    item.id: {
                        'task': item.data,
                        'tags': [tag.id for tag in item.tags]
                    }
                    for item in Todo.select()
            }

    def delete(self):

        return {}