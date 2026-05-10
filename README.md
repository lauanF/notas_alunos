# Sistema de Gerenciamento de Notas Acadêmicas

## 📋 Sobre o Projeto
Este sistema foi desenvolvido como parte da **Experiência Prática IV** da disciplina de Análise e desenvolvimento de sistemas. A aplicação tem como objetivo automatizar o registro e o acompanhamento do desempenho acadêmico de estudantes, permitindo o armazenamento de dados, o cálculo automático de médias e a verificação de status de aprovação.

O projeto foca em pilares fundamentais da engenharia de software, como:
* **Modularização:** Funções independentes com responsabilidade única (SRP).
* **Documentação:** Uso rigoroso de docstrings e padrões PEP 8.
* **Robustez:** Validação de dados e tratamento de casos extremos (Edge Cases).

## 🛠️ Tecnologias Utilizadas
* **Python**
* **Estruturas de Dados:** Listas e Dicionários.

## 🚀 Como Executar o Código Principal
Para rodar o sistema em sua máquina local, siga os passos abaixo:

1.  Certifique-se de ter o Python instalado em seu sistema.
2.  Abra o terminal ou o CMD na pasta onde o arquivo `medias_alunos.py` está localizado.
3.  Execute o comando:
    ```bash
    python medias_alunos.py
    ```
4.  O sistema processará a lista de estudantes pré-cadastrada e exibirá o relatório formatado diretamente no terminal.

## 🧪 Como Acionar o Ambiente de Testes
O projeto conta com rotinas de validação para garantir que os cálculos matemáticos e as regras de negócio estejam corretos.

Para executar os testes:
1.  No mesmo terminal, você pode executar o script no modo interativo para testar funções isoladamente:
    ```bash
    python -i medias_alunos.py
    ```
2.  No console Python, você pode realizar chamadas manuais para validar o comportamento, por exemplo:
    ```python
    print(calcular_media([10.0, 8.0, 9.0]))
    print(verificar_aprovacao(5.5))
    ```

## 📝 Licença
Este projeto foi desenvolvido para fins educacionais.
