from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic = {}
        # for string in strs:
        #     if "".join(sorted(string)) in dic:
        #         dic["".join(sorted(string))] = dic["".join(sorted(string))] + [string]
        #     else:
        #         dic["".join(sorted(string))] = [string]
        # return list(dic.values())

        dic=defaultdict(list) ## mapping charCount to list of anagrams
	
        for str in strs:
            count = [0] * 26 # a…z
            for char in str:
                count[ord(char) - ord('a')] += 1
            
            dic[tuple(count)] = dic[tuple(count)] + [str]
        return list(dic.values())
