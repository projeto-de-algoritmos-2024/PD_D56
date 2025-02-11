# Regular Expression Matching

Dada uma string `s` e um padrão `p`, verifique se `s` **corresponde** exatamente ao padrão `p`. O padrão pode conter os caracteres especiais:
- `'.'` (ponto): corresponde a **qualquer** caractere único.
- `'*'`: corresponde a **zero ou mais** ocorrências do elemento (caractere) imediatamente anterior.

A função deve retornar `true` se a correspondência for **completa** (isto é, se todo o padrão for aplicado a toda a string e não sobrar nada), caso contrário, retornar `false`.

## Exemplos

- **Exemplo 1**  
  - **Entrada:** `s = "aa"`, `p = "a"`  
  - **Saída:** `false`  
  - **Explicação:** O padrão `p` descreve apenas um caractere `'a'`, então não consegue corresponder a `"aa"`.

- **Exemplo 2**  
  - **Entrada:** `s = "aa"`, `p = "a*"`  
  - **Saída:** `true`  
  - **Explicação:** O padrão `a*` pode corresponder a zero ou mais `'a'`, atendendo a string `"aa"`.

- **Exemplo 3**  
  - **Entrada:** `s = "ab"`, `p = ".*"`  
  - **Saída:** `true`  
  - **Explicação:** O padrão `.*` pode corresponder a qualquer sequência de caracteres (ponto para qualquer caractere e `*` significa zero ou mais repetições), então `"ab"` se encaixa.

## Observações
1. Atenção às combinações de `.` com `*` e repetições sucessivas.
2. Estratégias comuns para resolver incluem **programação dinâmica** ou um algoritmo de backtracking cuidadoso.
3. A validação deve considerar que `*` age somente sobre o caractere (ou `.`) imediatamente precedente.

## Restrições
- O tamanho de `s` e de `p` pode chegar a 20, tornando soluções com backtracking ou DP viáveis dentro do limite.

> **Nota**: Para o enunciado completo, exemplos adicionais e dicas de implementação,  
> visite a [página do problema no LeetCode](https://leetcode.com/problems/regular-expression-matching/description/).
