class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        try:
            for item in ransomNote:
                magazine.remove(item)
            return True
        except:
            return False

test =Solution()
print(test.canConstruct('aa','aan'))