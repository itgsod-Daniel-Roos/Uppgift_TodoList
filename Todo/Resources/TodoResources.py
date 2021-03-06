from pony.orm import db_session, select, ObjectNotFound, orm
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

        return {}, 200                          #"Success!"

    def get(self):                              #Ger alla Todos
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

@api.resource('/TodoItem/<int:id>')
class TodoItem(rest.Resource):                      #Ger ett Todo Item
    def get(self, todo_id):
        try:
            with db_session:
                todo = Todo[todo_id]                     #Egentligen samma som Todo.get(id=todo_id)
                tags = [{tag.name: tag.url} for tag in todo.tags]

                return {
                    "task": todo.data,
                    "tags": tags
                }

        except ObjectNotFound:
            return {}, 404

@api.resource('/Tags/<int:id>')
class Tags(rest.Resource):                          #Ger alla tags
    def get(self):
        with db_session:
           return {
               tag.name: tag.url
               for tag in Tag.select()
           }

@api.resource('/TagItem/<int:id>')
class TagItem(rest.Resource):
    def get(self, tag_id):
        try:
            with db_session:
                tag = Tag[tag_id]
                todos = list(tag.todos.data)

                return {
                    "tag": tag.name,
                    "tasks": todos
                }

        except ObjectNotFound:
            return {}, 404