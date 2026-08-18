class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            signature = ''.join(sorted(word))
            groups[signature].append(word)
        
        return list(groups.values())
        