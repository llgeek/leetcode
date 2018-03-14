class Solution:
    def sentenceFitting(self, sentence, rows, cols):
        """
        type sentence: list of words
        type rows: int
        type cols: int
        rtype: int
        """
        sentencestr = ' '.join(sentence) + ' '
        sentencelen = len(sentencestr)
        totalspace = 0
        for i in range(rows):
            totalspace += cols
            # totalspace % sentencelen represents the position of next character!!
            if sentencestr[totalspace % sentencelen] == ' ':
                totalspace += 1
            else:
                while totalspace > 0 and sentencestr[(totalspace -1) % sentencelen] != ' ':
                    totalspace -= 1
            print(totalspace)
        return totalspace // sentencelen

s = Solution() 
sentence = ['ab', 'cde', 'f']
print(s.sentenceFitting(sentence, 5, 4))


        
        
