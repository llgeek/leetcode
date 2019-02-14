"""
Given a list of word Strings, return the longest String S such that:
1. S can be reduced to a single character String eventually by deleting a single leading or ending character each step.
2. The new string word that we get when deleting a single character should also exist in the list of Strings. 

given [spirnt， print，rint，int，in，i], return 'sprint'
"""

class Solution():
    def longestString(self, strings):
        
