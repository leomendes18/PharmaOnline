from app import db
import peewee


'''
class: Base Model
'''
class BaseModel(peewee.Model):

  class Meta:
    # Indica em qual banco de dados a tabela sera criada (obrigatorio). Neste caso, utilizamos o banco 'movies.db'
    database = db

class User(BaseModel):

  name = peewee.CharField(max_length=255)
  email = peewee.CharField(unique=True, max_length=255)
  password = peewee.CharField(max_length=255)
  usuario = peewee.CharField(unique=True)
  endereco = peewee.CharField(max_length=255)
  telefone = peewee.CharField(max_length=255)


  # @property
  #  def is_authenticated(self):
  #     return True
      
  #  @property
  #   def is_active(self):
  #     return True
      
  #  @property
  #  def is_anonymous(self):
  #     return False
  
  #  def get_id(self):
  #    return str(self.id)

      
class Medicamento(BaseModel):
  name = peewee.CharField()
  price = peewee.DecimalField()

