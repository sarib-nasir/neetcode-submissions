class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())

        # count_s,count_t = {},{}
        # for i in range(len(strs)):
        #     for j in range(i+1, len(strs)):
        #         if len(strs[i]) == len(strs[j]):
        #             if "".join(sorted(strs[i])) == "".join(sorted(strs[j])) :

        #                 print(strs[i],strs[j])
