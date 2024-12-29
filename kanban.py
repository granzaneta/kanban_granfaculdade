# Programa de Kanban em Python
# Criado por Gabriel Zaneta Pinheiro

class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "A Fazer"

    def atualizar_status(self, novo_status):
        self.status = novo_status

class Kanban:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        print("\nTarefas no Kanban:")
        for idx, tarefa in enumerate(self.tarefas):
            print(f"{idx + 1}. {tarefa.titulo} - {tarefa.status}")

    def detalhes_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            print(f"\nTítulo: {tarefa.titulo}\nDescrição: {tarefa.descricao}\nStatus: {tarefa.status}")
        else:
            print("Tarefa não encontrada.")

    def mover_tarefa(self, indice, novo_status):
        if 0 <= indice < len(self.tarefas):
            if novo_status in ["A Fazer", "Em Progresso", "Concluído"]:
                self.tarefas[indice].atualizar_status(novo_status)
                print("Status da tarefa atualizado.")
            else:
                print("Status inválido. Escolha entre 'A Fazer', 'Em Progresso' ou 'Concluído'.")
        else:
            print("Tarefa não encontrada.")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
            print("Tarefa removida.")
        else:
            print("Tarefa não encontrada.")

def menu():
    kanban = Kanban()
    while True:
        print("\n--- Kanban ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Detalhes de uma Tarefa")
        print("4. Mover Tarefa")
        print("5. Remover Tarefa")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da Tarefa: ")
            descricao = input("Descrição da Tarefa: ")
            kanban.adicionar_tarefa(titulo, descricao)
        elif opcao == "2":
            kanban.listar_tarefas()
        elif opcao == "3":
            kanban.listar_tarefas()
            indice = int(input("Digite o número da tarefa para ver detalhes: ")) - 1
            kanban.detalhes_tarefa(indice)
        elif opcao == "4":
            kanban.listar_tarefas()
            indice = int(input("Digite o número da tarefa a mover: ")) - 1
            novo_status = input("Novo status (A Fazer, Em Progresso, Concluído): ")
            kanban.mover_tarefa(indice, novo_status)
        elif opcao == "5":
            kanban.listar_tarefas()
            indice = int(input("Digite o número da tarefa a remover: ")) - 1
            kanban.remover_tarefa(indice)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
