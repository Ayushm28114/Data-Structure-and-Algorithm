class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1=Counter(ransomNote)
        dict2=Counter(magazine)

        for key, value in dict1.items():
            if value>dict2[key] or key not in dict2:
                return False
        
        return True