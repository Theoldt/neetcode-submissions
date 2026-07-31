class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            lenght = len(word)
            encoded_string += f"{lenght}#{word}"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0 
        decoded_string = []

        while i < len(s):

            j_index = s.find("#",i)
            j = int(s[i:j_index])
            debut = j_index + 1
            fin = debut + j
            decoded_string.append(s[debut:fin])

            
            i = fin
        
        return decoded_string



        




        









