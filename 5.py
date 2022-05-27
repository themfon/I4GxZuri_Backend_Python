# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
        # [assignment] code added
        str1 = "link"
        str2 = "kiln"
        str1_anagram = sorted(str1)
        str2_anagram = sorted(str2)
                            
        if str1_anagram == str2_anagram:
            return True
        else:
            return False
print(find_anagram("link", "kiln"))
