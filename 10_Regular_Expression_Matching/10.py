class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Caso base: p está vazio, s também deve estar vazio
        if not p:
            return not s

        # Se o primeiro caractere casa (ou p[0] == '.'), definimos match_inicial
        match_inicial = bool(s) and (p[0] == s[0] or p[0] == '.')

        # Verifica se há '*'
        if len(p) > 1 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    (match_inicial and self.isMatch(s[1:], p[2:])))
        else:
            # Se não tem '*', apenas prossegue
            if match_inicial:
                return self.isMatch(s[1:], p[1:])
            else:
                return False