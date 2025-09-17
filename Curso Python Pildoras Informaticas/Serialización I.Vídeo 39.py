import pickle
from distutils.dist import fix_help_options

fichero = open("lista_nombres", "rb")

lista=pickle.load(fichero)

print(lista)
