from pony.orm import PrimaryKey, Required, Set, orm
from Todo import db

#databasmodell

class Todo(db.Entity):

    _table_ = "Todos"

    data = orm.Required(unicode)
    tags = orm.Set("Tag")

class Tag(db.Entity):

    _table_ = "Tags"

    namn = PrimaryKey(int, auto=True)
    tags = orm.Set("Todo")

db.sql_debug(True)
db.generate_mapping(create_tables=True)