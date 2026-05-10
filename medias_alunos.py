def calcular_media(notas):
    """
    Recebe uma lista de notas (floats) e retorna a média aritmética destas notas.

    Args:
        notas (list): uma lista contendo as notas (floats) do estudante.

    Returns:
        float: O valor da média resultante. ou 0.0 se a lista estiver vazia.
    """
    if not notas:
        return 0.0
    else:
        return sum(notas) / len(notas)

def verificar_aprovacao (media, media_minima = 7.0):
    """
    Avalia se aluno atingiu a média mínima necessária da instituição

    Args:
        media (float): O valor da média final calculada do estudante.
        media_minima(float): A nota de corte para aprovação
            por padrão é 7.0

    Returns:
        str: 'Aprovado' Caso a média seja maior ou igual a à mínima, ou 'Reprovado' caso a média esteja a baixo da mínima
    """
    if media >= media_minima:
        return 'Aluno aprovado!'
    else:
        return 'Aluno reprovado!'
    
def gerar_relatorio(alunos):
    """
    Processa a lista de estudantes para exibir um relatório consolidado no terminal.

    A função irá percorrer os registros, acionando as rotinas de cálculo de média e verificação de status, formatando os resultados em uma tabela centralizada.

    Args:
        estudantes(list): uma lista  de dicionários, onde cada dicionário deve conter as chaves 'nome'(str) e 'notas'(float list)

    Returns:
        none: A função realiza apenas operações de saída não possui valor de retorno.    

    """
    divisor = ("-" * 55)
    
    print(divisor)
    print(f"{'Nome':^20} | {'Média':^10} | {'Situação':^15}")
    print(divisor)

    for aluno in alunos:
        nome = aluno['nome']
        notas = aluno['notas']

        media = calcular_media(notas)
        situacao = verificar_aprovacao(media)

        print(f"{nome:<20} | {media:^10.2f} | {situacao:<15}")
    
    print(divisor)

alunos = [
    {"nome": "Alice Silva", "notas": [8.0, 9.5, 7.8]},
    {"nome": "Bruno Souza", "notas": [6.0, 5.5, 6.0]},
    {"nome": "Carla Dias", "notas": [10.0, 9.0, 9.5]}
]

gerar_relatorio(alunos)