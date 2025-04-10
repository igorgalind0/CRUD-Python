
# 📄 Sistema de Gerenciamento de Usuários (SQLite)

Este projeto é um sistema de terminal em Python para o gerenciamento de usuários com operações CRUD (Create, Read, Update, Delete), utilizando SQLite como banco de dados.

---

## 📌 Estrutura da Tabela

O banco de dados `meu_banco.db` contém a tabela `Usuarios` com a seguinte estrutura:
![image](https://github.com/user-attachments/assets/4d9adb30-faa5-4a77-b33e-8a00053a2dbc)


| Campo | Tipo     | Descrição                             |
|-------|----------|----------------------------------------|
| id    | INTEGER  | Identificador único (auto incremento) |
| nome  | TEXT     | Nome do usuário                        |
| email | TEXT     | Email do usuário                       |

---

## ⚙️ Funcionalidades

1. **Adicionar Usuário**: Insere novo usuário com nome e email.

![image](https://github.com/user-attachments/assets/5216db70-6844-448a-a8af-078083b77953)

2. **Atualizar Usuário**: Modifica dados de um usuário com base no ID.

![image](https://github.com/user-attachments/assets/ef1625e7-56dd-4fa4-b2bb-bf5f746ad65d)

3. **Deletar Usuário**: Remove um usuário do banco pelo ID.

![image](https://github.com/user-attachments/assets/cbb3b578-0454-4bee-bd1b-14c87c06c25c)

4. **Listar todos os Usuários**: Exibe todos os registros no banco de dados.

![image](https://github.com/user-attachments/assets/7bd7f712-7895-4e4b-9e63-d262461f40c2)

5. **Buscar Usuário por Nome**: Busca parcial por nome.

![image](https://github.com/user-attachments/assets/a140faff-396e-4f64-880c-0e54fec1f00c)

6. **Buscar Usuário por ID**: Busca exata pelo ID.

![image](https://github.com/user-attachments/assets/efc55b6e-a47f-4e8e-b1e2-60e01d549c4a)

7. **Sair**: Encerra o programa.

![image](https://github.com/user-attachments/assets/87c83308-d7d4-41dd-942c-2f7662c751ce)

---

## Execução do Sistema
**O Sistema Iniciará mostrando o Menu de opções**
(Chamando uma função que mostra o menu e dá início as tarefas ao escolher cada opção)

![image](https://github.com/user-attachments/assets/1ce02688-3d7e-45e7-8465-3b59d94479e3)

![image](https://github.com/user-attachments/assets/8298cf47-67cd-43c9-9c63-9cf51a0bcc6e)

**Adicionando Usuário**
Ao escolher a opção de Adicionar Usuário (1), o Sistema pedirá o nome e e-mail do usuário para adicionar ao banco.

![image](https://github.com/user-attachments/assets/7335045b-484e-47b7-a83e-ae5f95e5370c)

![image](https://github.com/user-attachments/assets/f82cab65-b90a-4224-b04b-0fb9a2fb4592)

**Listando Usuários**
Ao escolher a opção de Listar Usuários (2), o Sistema mostrará uma lista de todos os usuários cadastrados (ID, nome, email)

![image](https://github.com/user-attachments/assets/b26e84a1-c6c1-4b86-9670-9209e4679839)

![image](https://github.com/user-attachments/assets/0e204cde-a2e5-4fdb-b578-990b10ebbc5a)

**Buscando Usuário por Nome**
Ao escolher a opção de Buscar por nome (3), será requisitado o nome do usuário que desja buscar, e aparecerá sua respectiva tabela (ID, nome, email)

![image](https://github.com/user-attachments/assets/bd87d538-14cd-4a8d-a26b-4a912ecddf5c)

![image](https://github.com/user-attachments/assets/5bbf96d1-37d3-4f23-871a-7dd3fbadc08a)

**Buscando Usuário por ID**
A busca de usuário por ID será feito através da opção 4, sendo pedido o ID do usuário e mostrado no terminal o usuário completo (ID, nome, email)

![image](https://github.com/user-attachments/assets/6f1a94ad-acc0-4760-a4ca-12d009569272)

![image](https://github.com/user-attachments/assets/4ba037f4-ec7a-4c1a-85e1-c3ee7937c168)

**Atualizar Usuário**
Ao escolher a opção de Atualizar Usuário (5), o sistema requisitará o ID do usuário e solicitará a troca do nome e email

![image](https://github.com/user-attachments/assets/94424a26-4dcc-4ab6-92ef-cf976b575ecc)

![image](https://github.com/user-attachments/assets/d4271be9-92a3-447a-8d42-50da3a78d117)

**Deletando Usuário**
Ao escolher a opção de Deletar Usuário (6), o sistema requisitará o ID do usuário e excluirá o usuário da tabela

![image](https://github.com/user-attachments/assets/0ddd0873-c35c-44db-ba15-4f01d8cc3d24)

![image](https://github.com/user-attachments/assets/570ee090-8a48-49e1-9bb6-f503d199f8db)

**Saindo do Sistema**
Ao escolher a opção 0, o sistema encerra.

![image](https://github.com/user-attachments/assets/bcfd7982-cb21-473a-9cbf-15a1ab364bc2)

![image](https://github.com/user-attachments/assets/c67662bf-ad47-4078-a6ee-50a65b0a2e5d)

## 📚 Bibliotecas Utilizadas

| Biblioteca | Descrição |
|------------|-----------|
| `sqlite3`  | Biblioteca padrão para manipulação de banco de dados SQLite. |

---

## ✅ Conclusão

Este projeto apresentou a construção de um sistema simples de gerenciamento de usuários utilizando Python e SQLite. Através de um menu interativo no terminal, o usuário pôde cadastrar, listar, buscar, atualizar e deletar registros de forma prática e eficiente.
Além de reforçar conceitos fundamentais como estruturas condicionais, funções, e manipulação de banco de dados, o projeto também proporcionou experiência na organização do código e no tratamento de exceções. A utilização do SQLite mostrou-se uma ótima escolha por sua leveza e praticidade para aplicações locais ou de pequeno porte.
