import sqlite3 as con
conexao = con.connect('meu_banco.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL)''')

conexao.commit()


def inserir_usuario(nome, email):
    cursor.execute('''
        INSERT INTO Usuarios (nome, email) VALUES (?, ?)''', (nome, email))
    conexao.commit()

    return cursor.lastrowid

def atualizar_usuario(user_id, nome, email):
    cursor.execute('''
        UPDATE Usuarios
        SET nome = ?, email = ?
        WHERE id = ?''', (nome, email, user_id))
    conexao.commit()
    return cursor.rowcount


def deletar_usuario(user_id):
    cursor.execute('''
        DELETE FROM Usuarios
        WHERE id = ?''', (user_id,))
    conexao.commit()


def listar_usuarios():
    cursor.execute('''SELECT * FROM Usuarios''')
    registros = cursor.fetchall()
    print("Lista de usuarios:\n")
    if registros:
        for usuarios in registros:
            print(f"ID: {usuarios[0]}, Nome: {usuarios[1]}, Email: {usuarios[2]}")
    else:
        print("Nenhum usuario foi encontrado.")

def pesquisar_usuario_nome(nome):
    cursor.execute('''SELECT * FROM Usuarios WHERE nome LIKE  ?''', ('%' + nome + '%',))
    usuarios = cursor.fetchall()
    print(f"Busca por nome: '{nome}'")
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")
    else:
        print("Usuario nao encontrado.")


def pesquisar_usuario_id(user_id):
    cursor.execute('''SELECT * FROM Usuarios WHERE id = ?''',
                   (user_id,))
    result = cursor.fetchone()

    print(f"\nResultados da busca:")
    if result:
        print(f"ID: {result[0]}, Nome: {result[1]}, Email: {result[2]}")
    else:
        print("Usuario nao encontrado.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Usuário")
        print("2. Listar todos os Usuários")
        print("3. Buscar Usuário por Nome")
        print("4. Buscar Usuário por ID")
        print("5. Atualizar Usuário")
        print("6. Deletar Usuário")
        print("0. Sair")

        opcao = input("Escolha sua opção: ")

        if opcao == '1':
            nome = input("Digite o nome do usuário:")
            email = input("Digite o email do usúario: ")
            user_id = inserir_usuario(nome, email)
            print(f"Usuário adicionado com ID: {user_id}")
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            nome = input("Digite o nome do usuario a buscar: ")
            pesquisar_usuario_nome(nome)
        elif opcao == '4':
            user_id = input("Digite o ID do usuário a buscar: ")
            pesquisar_usuario_id(user_id)
        elif opcao == '5':
            user_id = int(input("Digite o ID a atualizar: "))
            nome = input("Digite o novo nome do usuario: ")
            email = input("Digite o novo email do usuario: ")
            rows_updated = atualizar_usuario(user_id, nome, email)
            if rows_updated:
                print(f"Usuario com ID {user_id} atualizado com sucesso.")
            else:
                print(f"Nenhum usuario encontrado com ID {user_id}.")
        elif opcao == '6':
            user_id = int(input("Digite o ID do usuario a deletar: "))
            rows_deleted = deletar_usuario(user_id)
            if rows_deleted:
                print(f"Usuario com ID {user_id} deletado com sucesso.")
            else:
                print("Opção inválida. Tente novamente.")
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
    conexao.close()