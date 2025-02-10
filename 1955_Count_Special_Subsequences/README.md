# Count Number of Special Subsequences

Dado um array de inteiros positivos (`nums`), uma **subsequência especial** é definida como uma subsequência de comprimento 4, representada por índices `(p, q, r, s)`, onde `p < q < r < s`. Esta subsequência deve satisfazer as seguintes condições:

- `nums[p] * nums[r] == nums[q] * nums[s]`
- Deve haver pelo menos um elemento entre cada par de índices. Em outras palavras, `q - p > 1`, `r - q > 1` e `s - r > 1`.

O objetivo é **contar o número de diferentes subsequências especiais** em `nums`.

## Exemplo 1

- **Entrada:** `nums = [1, 2, 3, 4, 3, 6, 1]`
- **Saída:** `1`

**Explicação:**
- Há uma subsequência especial em `nums`:
  - `(p, q, r, s) = (0, 2, 4, 6)`: 
    - Corresponde aos elementos `(1, 3, 3, 1)`.
    - `nums[p] * nums[r] = nums[0] * nums[4] = 1 * 3 = 3`
    - `nums[q] * nums[s] = nums[2] * nums[6] = 3 * 1 = 3`

## Exemplo 2

- **Entrada:** `nums = [3, 4, 3, 4, 3, 4, 3, 4]`
- **Saída:** `3`

**Explicação:**
- Há três subsequências especiais em `nums`:
  - `(p, q, r, s) = (0, 2, 4, 6)`:
    - Corresponde aos elementos `(3, 3, 3, 3)`.
    - `nums[p] * nums[r] = nums[0] * nums[4] = 3 * 3 = 9`
    - `nums[q] * nums[s] = nums[2] * nums[6] = 3 * 3 = 9`
  - `(p, q, r, s) = (1, 3, 5, 7)`:
    - Corresponde aos elementos `(4, 4, 4, 4)`.
    - `nums[p] * nums[r] = nums[1] * nums[5] = 4 * 4 = 16`
    - `nums[q] * nums[s] = nums[3] * nums[7] = 4 * 4 = 16`
  - `(p, q, r, s) = (0, 2, 5, 7)`:
    - Corresponde aos elementos `(3, 3, 4, 4)`.
    - `nums[p] * nums[r] = nums[0] * nums[5] = 3 * 4 = 12`
    - `nums[q] * nums[s] = nums[2] * nums[7] = 3 * 4 = 12`

## Restrições

- `7 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`