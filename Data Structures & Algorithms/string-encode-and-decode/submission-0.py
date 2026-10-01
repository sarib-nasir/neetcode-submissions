class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        encoded_string = ""
        for i in strs:
            encoded_string = str(len(i))+"#"+i 
            encoded_list.append(encoded_string)
        encoded_string = "".join(encoded_list)
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":          
                j += 1
            length = int(s[i:j])        
            word = s[j + 1 : j + 1 + length]   
            decode_list.append(word)
            i = j + 1 + length          
        return decode_list

