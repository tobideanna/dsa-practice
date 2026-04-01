class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        we need return a sublsit of anagrams within that list.
        to know if something is an anagram, they have the same characters.
        so we can use a hashmap to put the ocurrence of each character, where the key is
        an array of size 26 with all occurrences. each key for the hashmap is a unique
        signature for each word. and then we need to use a list of words that fall
        within that category as a value there

        '''
        #to start, create a hashmap, but it needs to have default value of list
        response = defaultdict(list)

        #for each word, create that array with slots for a to z letters
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] +=1

        # we now have unique signatures of the characters, and each word has that
        #so we add that as a key:
            response[tuple(count)].append(word)
        return list(response.values())
