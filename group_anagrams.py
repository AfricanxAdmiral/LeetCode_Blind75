class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ## sort of anagrams should result the same string
            ans[''.join(sorted(s))].append(s)
        return ans.values()
