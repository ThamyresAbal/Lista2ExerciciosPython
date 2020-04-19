
import os

executavel = input('Digite o nome de um exe na área de trabalho')
print(executavel)
os.system("notepad "+executavel+".txt")
