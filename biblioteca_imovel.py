import sqlite3
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE if NOT EXISTS imoveis (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cidade VARCHAR(100),
        estado VARCHAR(100),
        endereço VARCHAR(100),
        localidade VARCHAR(100),
        quartos VARCHAR(100),
        banheiros VARCHAR(100),
        descricao VARCHAR(1000) NOT NULL
        );
""")

def cadastrar_imovel():
    cidade=input('Cidade:')
    estado=input('UF(Estado):')
    endereço=input('Endereço:')
    localidade=input('Proximo a:')
    quartos=input('Quantos quartos o imovel possui:')
    banheiros=input('Quantos banheiros o imovel possui:')
    descricao=input("Digite informações adicionais do imovel:")
    cursor.execute("INSERT INTO imoveis (cidade, estado, endereço, localidade, quartos, banheiros, descricao) VALUES ('"+cidade+"','"+estado+"','"+endereço+"','"+localidade+"','"+quartos+"','"+banheiros+"','"+descricao+"')")
    conn.commit()

def listar_imoveis():
    cursor.execute("SELECT * FROM imoveis;")
    row=cursor.fetchall()

    for l in range(len(row)):
        for c in range(8):
                print(row[l][c], end=" ")
                if (c==7):
                    print("")
                    print("Descrição do Imovel:")
                    print(row[l][7])
        print("")
    
    print('1 - Escolher imovel')
    print('2 - Descartar imovel especifico')
    print('3 - Voltar')

#cadastrar_imovel()
