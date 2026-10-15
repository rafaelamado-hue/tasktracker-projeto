"""
TaskTracker - Aplicação CLI para Gerenciamento de Tarefas
Desenvolvido em Python 3.
"""


def validar_titulo() -> str:
    """Solicita e valida o título da tarefa.
    Rejeita entradas vazias ou compostas apenas por espaços em branco.
    """
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("❌ Erro: O título é obrigatório e não pode conter apenas espaços!")


def validar_prioridade() -> str:
    """Solicita e valida a prioridade da tarefa.
    Aceita estritamente: Alta, Média (ou Media) e Baixa.
    """
    prioridades_validas = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }

    while True:
        prioridade = input("Digite a prioridade (Alta, Média ou Baixa): ").strip().lower()
        if prioridade in prioridades_validas:
            return prioridades_validas[prioridade]
        print("❌ Erro: Prioridade inválida! Escolha entre 'Alta', 'Média' e 'Baixa'.")


def cadastrar_tarefa(tarefas: list) -> None:
    """Coleta os dados do usuário, aplica as validações e cadastra a nova tarefa."""
    print("\n--- 📝 Cadastro de Nova Tarefa ---")
    titulo = validar_titulo()
    descricao = input("Digite a descrição da tarefa (opcional): ").strip()
    prioridade = validar_prioridade()
    data_limite = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não informada",
        "status": "Pendente",  # Definido automaticamente
    }

    tarefas.append(tarefa)
    print(f"\n✅ Tarefa '{titulo}' cadastrada com sucesso!")


def listar_tarefas(tarefas: list) -> None:
    """Exibe todas as tarefas cadastradas de forma legível e organizada."""
    print("\n--- 📋 Lista de Tarefas Cadastradas ---")

    if not tarefas:
        print("ℹ️ Nenhuma tarefa cadastrada no momento.")
        return

    for idx, t in enumerate(tarefas, start=1):
        print(f"\n[Tarefa #{idx}]")
        print(f"  • Título:      {t['titulo']}")
        print(f"  • Descrição:   {t['descricao']}")
        print(f"  • Prioridade:  {t['prioridade']}")
        print(f"  • Data Limite: {t['data_limite']}")
        print(f"  • Status:      {t['status']}")
        print("-" * 35)


def exibir_menu() -> None:
    """Exibe as opções do menu principal."""
    print("\n" + "=" * 35)
    print("      TASKTRACKER - MENU CLI")
    print("=" * 35)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=" * 35)


def main() -> None:
    """Função principal que gerencia o loop da aplicação."""
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando a aplicação... Até logo!")
            break
        else:
            print("❌ Opção inválida! Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
