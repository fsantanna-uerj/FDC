<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>        

Roteiro 11: Simulado P2
=======================

- Fazer todos os itens em um único arquivo, ex., `lab-11.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: FDC, lab-11, João da Silva
    - *Anexos*:
        - `lab-11.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4 e 5
Seguem arquivos em anexo...
```

## 1. (strings)

Crie um programa que leia uma frase e exiba uma nova frase onde todos os
dígitos são subtraídos por `1`.
Por exemplo, para a frase *a3b5c6*, o programa deve exibir *a2b4c5*.
Assuma que as frases não terão o dígito `0`.

(A função `ord` transforma um caractere em seu código numérico.
 A função `chr` transforma um código numérico em seu caractere.)

## 2. (arquivos)

Crie um programa que leia um arquivo `entrada.txt`, inverta as linhas
ímpares com as pares, e escreva o resultado para um arquivo `saida.txt`.

## 3. (matrizes e funções)

Crie a função `soma_linhas(mat)` que receba uma matriz `mat` e retorne uma nova
matriz na qual cada linha `i` é a soma entre as linhas `i` e `i-1` da matriz
recebida.
A primeira linha da matriz retornada deve ser igual à primeira linha da matriz
recebida.
Por exemplo, `soma_linhas([1,2],[3,4],[5,6])` deve retornar
`[[1,2],[4,6],[8,10]]`.

## 4. (listas, matrizes, e funções)

Crie a função `expande(lista)` que receba uma lista de pares com o formato
`[ [V0,N0], ..., [Vn,Nn] ]` e retorne uma lista expandida na qual cada `Vi` da
lista recebida deve ser repetido `Ni` vezes na lista expandida.
Por exemplo, `expande([[3,4],[7,3],[13,2],[23,1]]` deve retornar
`[3,3,3,3,7,7,7,13,13,23]`.

## 5. (listas)

Crie um programa que leia 100 números do teclado para uma lista.
Em seguida, o programa deve criar uma nova lista com as metades trocadas, i.e.,
os 50 primeiros valores lidos devem aparecer nas últimas posições e os últimos
valores lidos devem aparecer nas primeiras posições.
Por exemplo, para a lista `[1,2,3,4,...,100]`, uma nova lista
`[51,52,...,100,1,2,...,50]` deve ser criada.
