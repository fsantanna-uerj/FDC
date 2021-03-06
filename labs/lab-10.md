<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 10: Arquivos
====================

- Fazer todos os itens em um único arquivo, ex., `lab-10.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: FDC, lab-10, João da Silva
    - *Anexos*:
        - `lab-10.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4 ao 6
Seguem arquivos em anexo...
```

<https://github.com/fsantanna-uerj/FDC/blob/master/slides/fdc-08-arquivos.pdf>

1. .
    - abrir o arquivo *notas.txt* em modo de escrita
    - escrever no arquivo 3 linhas seguindo o formato *nome nota1 nota2*
    - fechar o arquivo
    - verificar se o arquivo *notas.txt* foi escrito corretamente
2. .
    - abrir o arquivo *notas.txt* em modo de escrita
    - ler do teclado, um por vez, o *nome*, *nota1* e *nota2* de um aluno
    - repetir a leitura até o nome ser a string vazia
    - escrever no arquivos todos nomes e notas seguindo o mesmo formato do
      exercício anterior
    - fechar o arquivo
    - verificar se o arquivo *notas.txt* foi escrito corretamente
3. .
    - abrir o arquivo *notas.txt* em modo de leitura
    - ler as linhas do arquivo, uma a uma, e exibi-las na tela
4. .
    - abrir o arquivo *notas.txt* em modo de leitura
    - ler as linhas do arquivo, uma a uma, e guardá-las em uma matriz
        - cada elemento da lista é uma outra lista com o formato
          `[nome, nota1, nota2]`
            - `nome` deve ser uma string
            - `nota1` e `nota2` devem ser números
    - usar a função `split` para separar o nome e as notas
    - usar a função `int` para converter uma string para um número
5. .
    - a partir da lista do exercício anterior, exibir o nome dos alunos com
      média acima de 5.
6. .
    - criar o arquivo *ordenado.txt* com o nome dos alunos ordenados por média
