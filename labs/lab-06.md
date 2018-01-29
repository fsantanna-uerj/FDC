<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 6: Simulado P1'
=======================

- Fazer todos os itens em um único arquivo, ex., `lab-06.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: FDC, lab-06, João da Silva
    - *Anexos*:
        - `lab-06.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4
Seguem arquivos em anexo...
```

## 1.

Numa turma existem 50 alunos.
Cada aluno tem um número de matrícula e uma nota.

- Crie um programa que leia o número de matrícula e a nota de cada aluno.
  Ao final, exiba o número de matrícula e a nota dos alunos com a maior e menor
  notas.
- Se houver dois ou mais alunos com a maior nota, o seu programa exibirá o de
  maior ou o de menor número de matrícula? Por quê?
  Assuma que os números de matrícula serão sempre digitados em ordem crescente.

## 2.

Crie um programa que lê dois números `N` e `V` e cria uma lista `L` de `N`
elementos crescentes (i.e., cada elemento é maior que o anterior na lista).
O primeiro elemento da lista deve ser igual a `V`.

## 3.

Um jogo de ``Adivinha!'' funciona da seguinte forma:

- Em cada rodada, o ``mestre'' escolhe um número qualquer.
- Em seguida, o jogador tenta adivinhar o número.
- Se o jogador acertar o número do mestre, ele marca 10 pontos.
- Se o jogador errar com uma diferença de até 2, ele marca 5 pontos.
- São 5 rodadas

Faça um programa que leia os números do mestre e do jogador alternadamente
(durante as 5 rodadas) e escreva na tela o total de pontos somados.
Assuma que só serão digitados números entre 0 e 9.

## 4.

Crie um programa que leia uma lista de 10 números inteiros crescentes e, em
seguida, exiba a maior sequência contínua de sucessores dessa lista.

Assuma que os números serão digitados em ordem crescente.

Para a lista `[1,2,4,5,6,9,10]`, a maior sequência contínua de sucessores é
`[4,5,6]`.

## 5.

Considere o programa e a seguir:

```
print "Seja Bem-vindo..."
n1 = input()
n2 = input()
r1 = 0
while n1 >= 0:
    c1 = 1
    while c1 <= n2:
        n1 = n1 - 1
        c1 = c1 + 1
    r1 = r1 + 1
    print "n1", n1, "r1", r1
r1 = r1 - 1
r2 = n1 + n2
print "A resposta é ", r1, r2
```

Considere que, para o programa acima, o usuário digitou os números a seguir:

```
3
10
5
```

a) Simule a execução do programa considerando a entrada e transcreva o estado
   da memória (conteúdo das variáveis) e saída na tela (efeito dos `print`).

A simulação para as duas primeiras linhas já está transcrita a seguir:

```
# Estado da Memória
# Variável val1 val2 val3 ...
# -------- ---- ---- ----
  n1          3
  n2         10

# Tela do Computador
# ------------------
Seja Bem-vindo...
```

b) O que o programa está fazendo? Descreva "em bom português" o significado
   do programa.                          
   Em outras palavras, explique o que o programa faz para alguém que não sabe
   programar.
