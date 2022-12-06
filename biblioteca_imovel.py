import sqlite3
import os
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE if NOT EXISTS imoveis (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        dono VARCHAR(100),
        cidade VARCHAR(100),
        estado VARCHAR(100),
        endereço VARCHAR(100),
        localidade VARCHAR(100),
        quartos VARCHAR(100),
        banheiros VARCHAR(100),
        descricao VARCHAR(1000) NOT NULL
        );
""")

def cadastrarImovel(email):
    dono=email
    cidade=input('Cidade:')
    estado=input('UF(Estado):')
    endereço=input('Endereço:')
    localidade=input('Proximo a:')
    quartos=input('Quantos quartos o imovel possui:')
    banheiros=input('Quantos banheiros o imovel possui:')
    descricao=input("Digite informações adicionais do imovel:")
    cursor.execute("INSERT INTO imoveis (dono, cidade, estado, endereço, localidade, quartos, banheiros, descricao) VALUES ('"+dono+"','"+cidade+"','"+estado+"','"+endereço+"','"+localidade+"','"+quartos+"','"+banheiros+"','"+descricao+"')")
    conn.commit()

def listarImoveis():
    os.system('cls')
    cursor.execute("SELECT * FROM imoveis;")
    row=cursor.fetchall()

    for l in range(len(row)):
        for c in range(9):
                print(row[l][c], end=" ")
        print("")

def listarMeusImoveis(email):
    os.system('cls')
    cursor.execute("SELECT * FROM imoveis;")
    row=cursor.fetchall()

    for l in range(len(row)):
            if email == row[l][1]:
                    for c in range(9):
                        print(row[l][c], end=" ")
            print("")