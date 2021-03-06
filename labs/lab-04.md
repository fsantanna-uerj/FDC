<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 4: Listas [1/2]
=======================

- Fazer todos os itens em um único arquivo, ex., `lab-04.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: FDC, lab-04, João da Silva
    - *Anexos*:
        - `lab-04.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 8
Não: 9 ao 10
Seguem arquivos em anexo...
```

Listas
------

<https://github.com/fsantanna-uerj/FDC/blob/master/slides/fdc-03.pdf>

1. .
    - criar uma lista `L1` com os valores *1,2,3,4*
    - exibir a lista
    - exibir o tamanho da lista
    - exibir o 3o elemento da lista (deve exibir o valor *3*)
2. .
    - criar uma lista `L2` com 100 zeros
    - exibir a lista
    - exibir o tamanho da lista
    - alterar o 8o elemento para `50`
    - exibir a lista
3. .
    - criar uma lista `L3` vazia
    - exibir a lista
    - ler do teclado e inserir 2 elementos novos na lista
        - `L3.append(x)` insere `x` em `L3`
    - exibir novamente a lista
4. .
    - criar uma lista `L4` vazia
    - ler do teclado e inserir 10 elementos novos na lista usando `for` ou `while`
    - exibir a lista
5. .
    - percorrer a lista `L4` com um *loop*
    - exibir os valores da lista maiores que 5
6. .
    - criar uma lista `L6` vazia
    - percorrer a lista `L4` e guardar os valores maiores que 5 em `L6`
    - exibir `L6`
7. .
    - criar uma lista `L7` vazia
    - percorrer a lista `L4` e guardar os **índices** dos valores maiores que 5
      em `L7`
    - exibir `L7`
8. .
    - criar uma lista `L8` vazia
    - percorrer a lista `L4` e guardar os índices e valores maiores que 5 em `L8`
    - exibir `L8`
9. .
    - criar uma lista `P1` com as notas da P1
    - criar uma lista `P2` com as notas da P2
    - exibir o número de chamada (índice na lista) dos alunos aprovados com média `>= 7`
10. .
    - criar duas listas `LA` e `LB`
    - exibir os valores que aparecem nas duas listas, ou seja, a sua interseção
        - essa questão necessita de um `while` dentro de um `while`
