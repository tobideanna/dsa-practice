class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        we need return a sublsit of anagrams within that list.
        to know if something is an anagram, they have the same characters.
        so we can use a hashmap to put the ocurrence of each character, where the key is
        an array of size 26 with all occurrences, and the value are the strings

        '''

        response = defaultdict(list)

        for word in strs:
            count = [0] * 26 #a to z array

            for char in word:
                count[ord(char) - ord("a")]+= 1 # we increment each character ocurrence by 1 in each word
            
            response[tuple(count)].append(word)
        
        return list(response.values())

        