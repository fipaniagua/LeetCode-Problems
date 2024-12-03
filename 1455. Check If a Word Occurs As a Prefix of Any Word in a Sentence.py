class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        searchWordLen = len(searchWord)
        for index_of_word, word in enumerate(sentence.split(" ")):
            if searchWordLen > len(word):
                continue
            if word[:searchWordLen] == searchWord:
                return index_of_word
        return -1