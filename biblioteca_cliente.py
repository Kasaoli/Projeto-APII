import sqlite3
import os
import biblioteca_imovel

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE if NOT EXISTS clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf VARCHAR(14),
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        dia VARCHAR(2) NOT NULL, 
        mes VARCHAR(2) NOT NULL,
        ano VARCHAR(4) NOT NULL,
        tipo_de_conta VARCHAR(1) NOT NULL
);
""")

def entrarUsuario(email, senha):
    os.system('cls')

    seleciona = "SELECT email FROM clientes WHERE email ='{}'".format(email)
    cursor.execute(seleciona)
    resultado = cursor.fetchall()

    if len(resultado)!=0:  #Verifica se o retorno contém alguma linha
        cursor.execute("SELECT * FROM clientes;")
        row=cursor.fetchall()
        
        for l in range(len(row)):
            for c in range(9):
                if email == row[l][3]:
                    if senha == row[l][4]:
                        return 1

    else:
        print("Email existente, tente novamente")
        return 0


def cadastrarUsuario():
    os.system('cls')
    nome = input('Nome: ')
    email = input('Email: ')
    senha = input('Senha: ')
    print('Data de nascimento.')
    dia = input('Dia: ')
    mes = input('Mês: ')
    ano = input('Ano: ')
    cpf = input	('CPF: ')
    tipoDeConta = input("Você é Universitario(digite u) ou Dono de imovel(digite d): ")

    seleciona = "SELECT email FROM clientes WHERE email ='{}'".format(email)
    cursor.execute(seleciona)
    resultado = cursor.fetchall()

    if len(resultado)!=0:  #Verifica se o retorno contém alguma linha
        print('Usuario Já Cadastrado')
        print('Tente novamente')
    else:
        print('Cadastro realizado')
        cursor.execute("INSERT INTO clientes (email,dia,mes,ano,cpf,senha,nome,tipo_de_conta) VALUES ('"+email+"','"+dia+"','"+mes+"','"+ano+"','"+cpf+"','"+senha+"','"+nome+"','"+tipoDeConta+"')")
        cursor.execute("SELECT * FROM clientes;")
        # print(cursor.fetchall())
        conn.commit()

def listarTodosUsuarios():
    os.system('cls')
    cursor.execute("SELECT * FROM clientes;")
    row=cursor.fetchall()

    for l in range(len(row)):
        for c in range(9):
            print(row[l][c], end=" ")
        print("")

def listarUsuario(email, senha):
    os.system('cls')
    cursor.execute("SELECT * FROM clientes;")
    row=cursor.fetchall()

    for l in range(len(row)):
            for c in range(9):
                if email == row[l][3]:
                    if senha == row[l][4]:
                       print(row[l][c], end=" ")
                    print('')

def listarEmail():
    os.system('cls')
    cursor.execute("SELECT * FROM clientes;")
    row=cursor.fetchall()

    for l in range(len(row)):
        if row[l][8] == 'u':
            print(row[l][3], end=" ")
            print('')
        