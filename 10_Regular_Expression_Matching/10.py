class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if not p:
            return not s

        match_inicial = bool(s) and (p[0] == s[0] or p[0] == '.')

        if len(p) > 1 and p[1] == '*':

            if self.isMatch(s, p[2:]):
                return True
            if match_inicial:
                
                if self.isMatch(s[1:], p):
                    return True
            return False
        else:
            if match_inicial:
                return self.isMatch(s[1:], p[1:])
            else:
                return False