from database import initialize_vector_search_database
from model import Model
from user_interface import create_user_interface

def main():
  database = initialize_vector_search_database()
  model = Model(database)
  app = create_user_interface(model)
  app.launch()

if __name__ == "__main__":
  main()