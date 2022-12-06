import sqlite3
import os
import biblioteca_cliente
import biblioteca_imovel

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

x = 1
while(x!=0):
    print('1 - Entrar')
    print('2 - Cadastrar')
    print('3 - Listar')
    x=int(input('Digite o número para a opção desejada:'))

    if x == 1:
        email = input('Email: ')
        senha = input('Senha: ')

        if biblioteca_cliente.entrarUsuario(email, senha) == 1:
            os.system('cls')
            cursor.execute("SELECT * FROM clientes;")
            row=cursor.fetchall()
            for l in range(len(row)):

                for c in range(9):

                    if email == row[l][3]:

                        if senha == row[l][4]:
                            
                            if row[l][8] == 'u':
                                print('1 - Lista imóveis')
                                print('2 - Escolher imóvel')
                                print('3 - Ver meu perfil')
                                print('4 - Abrir chat')
                                print('5 - Listar usúarios')
                                opcaoUsuario = int(input(''))

                                if opcaoUsuario == 1:
                                    biblioteca_imovel.listarImoveis()

                                elif opcaoUsuario == 2:
                                    print('Escolha qual imóvel você quer e com quem dividir')
                                    imovelEscolhido = int(input('ID do imóvel: '))
                                    pessoaDividir = input('Email de quem você quer dividir: ')
                                    for l in range(len(row)):
                                        for c in range(9):
                                            if pessoaDividir == row[l][3]:
                                                print('Imovel escolhido e dividido')

                                elif opcaoUsuario == 3:
                                    biblioteca_cliente.listarUsuario(email, senha)

                                elif opcaoUsuario == 5:
                                    biblioteca_cliente.listarEmail()

                            elif row[l][8] == 'd':
                                print('1 - Cadastrar imóvel')
                                print('2 - Listar meus imóveis')
                                print('3 - Ver meu perfil')
                                print('4 - Abrir chat')
                                opcaoUsuario = int(input(''))
                                
                                if opcaoUsuario == 1:
                                    biblioteca_imovel.cadastrarImovel(email)

                                elif opcaoUsuario == 2:
                                    biblioteca_imovel.listarMeusImoveis(email)

                                elif opcaoUsuario == 3:
                                    biblioteca_cliente.listarUsuario(email, senha)

                                #elif opcaoUsuario ==  4:
                                    #chat = str('')
                                    #with open ('chat.txt', 'w') as arquivo:
                                    #arquivo.writelines(chat)

    elif x == 2:
        biblioteca_cliente.cadastrarUsuario()
        os.system('cls')

    elif x == 3:
        biblioteca_cliente.listarTodosUsuarios()
