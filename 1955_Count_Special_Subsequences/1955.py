class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7 # Constante para o módulo
        count_0, count_1, count_2 = 0, 0, 0 # Inicializa os contadores para subsequências que terminam com 0, 1 e 2.
        
        for num in nums:
            if num == 0:
                # Para um elemento 0, podemos:
                # - Dobrar as subsequências existentes terminadas com 0 (incluindo o novo 0 em cada uma delas)
                # - Iniciar uma nova subsequência que consiste apenas deste 0
                count_0 = (count_0 * 2 + 1) % mod
            elif num == 1:
                # Para um elemento 1, podemos:
                # - Dobrar as subsequências existentes terminadas com 1 (adicionando o 1 em cada uma delas)
                # - Estender todas as subsequências que terminam com 0, convertendo-as em subsequências terminadas com 1
                count_1 = (count_1 * 2 + count_0) % mod
            elif num == 2:
                # Para um elemento 2, podemos:
                # - Dobrar as subsequências existentes terminadas com 2 (adicionando o 2 em cada uma delas)
                # - Estender todas as subsequências que terminam com 1, convertendo-as em subsequências terminadas com 2
                count_2 = (count_2 * 2 + count_1) % mod

        # Ao final, count 2 representa o número total de subsequências especiais que seguem a ordem 0 -> 1 -> 2
        return count_2
