class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we need to group all anagrams together into sublists
        #we need to create a signature for each string in the array
        #each signature can have 0 * 26 characters, and we want to
        #map a to 0 and z to 26
        #we can use this signature as the key in a hashmap, so
        #each word has a key

        map1 = defaultdict(list)

        for word in strs:
            signature = [0] * 26
            for char in word:
                #we need to map character's a count to 0
                signature[ord(char) - ord('a')] += 1
            map1[tuple(signature)].append(word)
        return list(map1.values())
        
        
           
        