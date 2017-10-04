<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 5: Listas [2/2]
=======================

- Fazer todos os itens em um único arquivo, ex., `lab-05.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: FDC, lab-05, João da Silva
    - *Anexos*:
        - `lab-05.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 5
Não: 6 e 7
Seguem arquivos em anexo...
```

Listas
------

<https://github.com/fsantanna-uerj/FDC/blob/master/slides/fdc-03.pdf>

1. .
    - criar uma lista `L1` vazia
    - ler do teclado e inserir 10 elementos novos na lista usando `for` ou `while`
    - exibir a lista
2. .
    - percorrer a lista `L1` usando `for` ou `while`
        - exibir os valores pares da lista
3. .
    - ler um número do teclado
    - percorrer a lista `L1` usando `for` ou `while`
        - contar quantas vezes o número lido aparece na lista
4. .
    - fazer um programa com a seguinte funcionalidade:
        1. cria uma lista `L4` vazia
        2. lê do teclado uma letra
            - caso seja `'A'`, lê do teclado um novo número e o adiciona a `L4`
            - caso seja `'R'`, remove o último elemento com `L4.pop()`
            - caso seja `'E'`, exibe a lista
            - caso seja `'T'`, termina o programa
        3. repete o passo `b`
5. .
    - criar duas listas `LA` e `LB`
    - criar uma nova lista `LC` com os valores que aparecem em `LA` e em `LB`,
      ou seja, a união entre `LA` e `LB`
        - `LC` não deve ter repetições, ou seja, o mesmo número não deve
          aparecer duas vezes
    - exibir a lista `LC`
6. .
    - criar uma lista `L6` com alguns números quaisquer
    - percorrer a lista inteira comparando elementos consecutivos dois a dois (i.e., `L6[0]` vs `L6[1]`, `L6[1]` vs `L6[2]`, ...)
    - trocar os valores quando o maior estiver no índice menor (e.g., `4,2` deve virar `2,4`)
    - exibir a lista `L6`
    - exemplo
        - `[4,2,5,1]`
            - `4,2 -> 2,4`
            - `4,5 -> 4,5`
            - `5,1 -> 1,5`
        - `[2,4,1,5]`
7. .
    - modificar o exercício anterior para ordenar uma lista inteira
    - exemplo
        - `[4,2,5,1]`, lista desordenada
            - ...
        - `[1,2,4,5]`, lista ordenada
    - dica: criar um loop por fora do exercício anterior
