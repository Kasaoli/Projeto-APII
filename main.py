import sqlite3
import os
import biblioteca_cliente
import biblioteca_imovel

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

x=1
while(x!=0):
    print('1 - Entrar')
    print('2 - Cadastrar')
    print('3 - Listar')
    x=int(input('Digite o número para a opção desejada:'))

    if x == 1:   
        email = input('Email: ')
        senha = input('Senha: ')
        biblioteca_cliente.entrarUsuario(email, senha)
    elif x == 2:
        biblioteca_cliente.cadastrarUsuario()
        os.system('cls')
    elif x == 3:
        biblioteca_cliente.listar_usuario()
    