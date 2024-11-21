from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in map_.keys():
                map_[key] = [s]
            else:
                map_[key].append(s)
        res = []
        for k,v in map_.items():
            res.append(v)
        return sorted(res) 