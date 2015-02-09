from pony.orm import PrimaryKey, Required, Set
from Todo import db

#databasmodell

class Todo(db.Entity):

    _table_ = "Todos"

    data = Required(unicode)
    tags = Set("Tag")

class Tag(db.Entity):

    _table_ = "Tags"

    namn = PrimaryKey(int, auto=True)
    tags = Set("Todo")

db.sql_debug(True)
db.generate_mapping(create_tables=True)
