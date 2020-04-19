
'''
2)
a)Uma variável de ambiente é um atalho para um valor que neste caso está disponível no ambiente de execução (neste caso no sistema operacional inteiro)
Na maioria dos casos, precisamos adicionar valores a essas variáveis para que alguns programas consigam encontrar o que precisam para executar corretamente.

b)Para esses casos o módulo os.path disponibiliza a função expanduser().

c) Através da função expanduser() que irá substituir o símbolo ~ pelo caminho completo de onde devemos guardar esses os arquivos de configuração
'''
import os.path

print (os.path.expanduser("~/.arquivorc"))

#OBS 1 : Resultado casos de linux - /home/username/.arquivorc
#OBS 2 : Resultado casos de windows - C:\\Documents and Settings\\username\\.arquivorc
