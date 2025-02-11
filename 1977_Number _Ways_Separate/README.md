# Number of Ways to Separate Numbers

Dada uma string numérica (`num`), o objetivo é encontrar o número de maneiras possíveis de separá-la em uma sequência de números inteiros não decrescentes.

Cada número formado pela separação não pode ter zeros à esquerda e deve ser maior ou igual ao número anterior na sequência.

## Exemplo 1

- **Entrada:** `num = "327"`
- **Saída:** `2`

**Explicação:**
- As possíveis separações são:
  - `["3", "27"]`
  - `["327"]`
- A separação `["32", "7"]` não é válida, pois `7` não é maior ou igual a `32`.

## Exemplo 2

- **Entrada:** `num = "222"`
- **Saída:** `4`

**Explicação:**
- As possíveis separações são:
  - `["2", "2", "2"]`
  - `["2", "22"]`
  - `["22", "2"]`
  - `["222"]`

## Restrições

- `1 <= num.length <= 3500`
- `num` consiste apenas em dígitos (`0-9`) e não contém zeros à esquerda, exceto no caso do próprio número `0`.