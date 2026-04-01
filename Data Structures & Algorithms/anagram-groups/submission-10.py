class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all anagrams together
        #the way to do this is to create a hashmap, and to know if words are ana
        #grams, they should share the same 'signature' key in the hashmap
        #so first, create a hashmap
        hash_map = defaultdict(list)

        for word in strs:
            signature = [0] * 26
            for char in word:
                signature[ord(char) - ord('a')] += 1
            hash_map[tuple(signature)].append(word)
        return list(hash_map.values())
            