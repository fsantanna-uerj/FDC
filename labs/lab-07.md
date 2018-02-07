<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></p>

Roteiro 7: Strings
==================

- Fazer todos os itens em um único arquivo, ex., `lab-07.py`.
- Ao final, enviar um e-mail da seguinte forma:
    - *Para*: `francisco@ime.uerj.br`
    - Enviar uma cópia para o seu e-mail.
      **Ao desligar, todos os arquivos são removidos do computador.**
    - *Assunto*: FDC, lab-07, João da Silva
    - *Anexos*:
        - `lab-07.py`
        - Para cada item, um *print screen* da tela de edição e outro da tela de execução
    - *Corpo*: Enumerar os exercícios que foram e não foram feitos, ex.:

```
Sim: 1 ao 3
Não: 4 ao 5
Seguem arquivos em anexo...
```

<https://github.com/fsantanna-uerj/FDC/blob/master/slides/fdc-04-strings.pdf>

<https://github.com/fsantanna-uerj/FDC/blob/master/slides/fdc-05-strings.pdf>

1. .
    - ler do teclado um número `v1`
    - transformar `v1` em uma string `s1`
    - exibir `v1` e `s1` na tela
    - usar o comando `str`
2. .
    - ler do teclado a string `s2`
    - exibir o tamanho da string
    - exibir o primeiro e último caracteres usando índices positivos
    - exibir o primeiro e último caracteres usando índices negativos
3. .
    - ler do teclado as strings `s31` e `s32`
    - concatenar (unir) as duas strings lidas em `s33` separadas por um espaço
    - exibir `s33`
    - usar a operação `+`
4. .
    - ler do teclado a string `s4`
    - exibir todos os códigos numéricos correspondentes aos caracteres de `s4`
    - guardar em uma lista `l4` todos os códigos numéricos correspondentes
      aos caracteres de `s4`
    - usar a função `ord`
5. .
    - ler do teclado uma lista `l5` de números
    - converter `l5` para uma string `s5`
        - cada valor `l5[i]` corresponde ao código numérico de `s5[i]`
    - usar a função `chr`
6. .
    - O método `count` de Python conta quantas vezes um caractere aparece numa
      string. E.x., `'abacaxi'.count('a') --> 3`
    - ler do teclado uma string `s6`
    - ler do teclado um caractere `c6`
    - sem usar `count`, conte o quantas vezes `c6` aparece em `s6`
7. .
    - leia uma string `s7`
    - crie uma lista `l7` vazia
    - guarde em `l7` todas as substrings de `s7` separadas por `','`
    - e.x., `s7 = 'a,bb,c'`, `l7 = ['a','bb','c']`
