class Solution:
    def encode(self, strs: List[str]) -> str:
        delimeter = "👋"
        encode = ""
        for str1 in strs:
            encode += str1 + delimeter
        print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        return s.split("👋")[:-1]
