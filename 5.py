# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
        # [assignment] code added
        word = input("Please write a word: \n")
        anagram = input("please write an anagram: \n")

        str1_anagram = sorted(word)
        str2_anagram = sorted(anagram)
                            
        if str1_anagram == str2_anagram:
            return True
        else:
            return False
print(find_anagram("word", "anagram"))
