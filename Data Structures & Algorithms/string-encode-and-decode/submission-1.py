class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1

            length = int(length)
            i += 1

            word = ""
            for _ in range(length):
                word += s[i]
                i += 1
            
            result.append(word)

        return result
        
        
        
