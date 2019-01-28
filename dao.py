from models import Livro

class LivroDao():

    def __init__(self,db):
        self.db = db

    def create(self, titulo, autor, editora):
        cursor = self.db.cursor()
        query = 'INSERT into livros (titulo, autor, editora) values (%s, %s, %s)'
        cursor.execute(query, (titulo,autor,editora))
        self.db.commit()

    def read_all(self):
        cursor = self.db.cursor()
        query  = 'SELECT titulo,editora,autor,id FROM livros GROUP BY autor,editora,titulo,id'
        cursor.execute(query)
        return cursor.fetchall()

    def read_one(self, id):
        cursor = self.db.cursor()
        query  = 'SELECT * FROM livros WHERE id=%s'
        cursor.execute(query,(id,))
        return cursor.fetchone()

    def update(self, id, titulo, autor, editora):
        cursor = self.db.cursor()
        query = ('UPDATE livros SET titulo=%s, autor=%s, editora=%s  WHERE id=%s')
        print(query)
        cursor.execute(query,(titulo,autor,editora,id))
        self.db.commit()


    def delete(self, id):
        cursor = self.db.cursor()
        query  = f'DELETE FROM livros WHERE id={id}'
        cursor.execute(query, (id))
        self.db.commit()
    