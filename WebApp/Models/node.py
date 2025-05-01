
class SQLEntity(tuple):
    id:int

    def get_id(self):
       return (self.id)

class Author(SQLEntity):
    def __init__(self, content_data):
        self.id:int = content_data[0]

class Book(SQLEntity):
    def __init__(self, book_data):
        self.id:int = book_data[0]
        self.name:str = book_data[1]
        self.author:Author = book_data[3]



