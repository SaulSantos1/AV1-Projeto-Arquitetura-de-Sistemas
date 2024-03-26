class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\nPreço: R${self.preco:.2f}\nQuantidade: {self.quantidade}"

class ProdutoFactory:
    @staticmethod
    def criar_produto(nome, descricao, preco, quantidade):
        return Produto(nome, descricao, preco, quantidade)

class CadastroProduto:
    def __init__(self):
        self.produtos = []

    def cadastrar(self, produto):
        self.produtos.append(produto)

    def listar(self):
        for produto in self.produtos:
            print(produto)
            print(" ")

    def buscar_por_nome(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

    def atualizar(self, nome, descricao, preco, quantidade):
        produto = self.buscar_por_nome(nome)
        if produto is not None:
            produto.descricao = descricao
            produto.preco = preco
            produto.quantidade = quantidade

    def remover(self, nome):
        produto = self.buscar_por_nome(nome)
        if produto is not None:
            self.produtos.remove(produto)
            
    def menu(self):
        print("""Digite o número correspondente à ação desejada:\n
1. Cadastrar Produto\n
2. Remover Produto\n
3. Atualizar Produto\n
4. Listar Produtos\n
0. Sair """)

    def executar(self):
        while True:
            self.menu()
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 0:
                print("Saindo do Sistema de Cadastro")
                break
            elif opcao == 1:
                self.cadastrar_produto()
            elif opcao == 2:
                self.remover_produto()
            elif opcao == 3:
                self.atualizar_produto()
            elif opcao == 4:
                self.listar_produtos()
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")

    def cadastrar_produto(self):
        quantidade = int(input("Quantos produtos você quer cadastrar? "))
        for i in range(quantidade):
            nome = input(f"Digite o nome do produto {i + 1}: ")
            descricao = input(f"Digite a descrição do produto {i + 1}: ")
            preco = float(input(f"Digite o preço do produto {i + 1}: "))
            quantidade = int(input(f"Digite a quantidade do produto {i + 1}: "))
            print(" ")
            produto = ProdutoFactory.criar_produto(nome, descricao, preco, quantidade)
            self.cadastrar(produto)

    def remover_produto(self):
        self.listar()
        nome = input("Digite o nome do produto que deseja remover: ")
        self.remover(nome)

    def atualizar_produto(self):
        self.listar()
        nome = input("Digite o nome do produto que deseja atualizar: ")
        descricao = input("Digite a nova descrição do produto: ")
        preco = float(input("Digite o novo preço do produto: "))
        quantidade = int(input("Digite a nova quantidade do produto: "))
        self.atualizar(nome, descricao, preco, quantidade)

    def listar_produtos(self):
        print("Lista de Produtos:")
        self.listar()

cadastro = CadastroProduto()
cadastro.executar()
