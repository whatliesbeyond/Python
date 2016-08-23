"""
Introduction: Given  an arbitrary  ransom  note  string and another string 
containing letters from  all the magazines,  write a function that will return 
true if the ransom  note can be constructed from the magazines ; 
otherwise, it will return false.  

Each letter  in  the  magazine string can  only be  used once  in  your ransom  note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Revision        Author          Comment
1.0             Dewang          Solved Using dictionary and Counter objects in
                                Python



++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""



from collections import Counter

# using generic dictionary
def CanConstructMethod1(ransomNote, magazine):
    CharCounter = {}

    for i in magazine:
       if i in CharCounter:
           CharCounter[i] += 1
       else:
           CharCounter[i] = 1

    for i in ransomNote:
        if i not in CharCounter:
            return False
        elif i in CharCounter:
             if CharCounter[i] == 0:
                 return False
        CharCounter[i] -= 1

    return True

# using Counter dictionary available from collections library
def CanConstructMethod2(ransomNote, magazine):
    char_counter_magazine = Counter(magazine)
    char_counter_ransomNote = Counter(ransomNote)
    for i in char_counter_ransomNote:
        if i not in char_counter_magazine:
            return False
    for i in char_counter_ransomNote:
        if char_counter_ransomNote[i] > char_counter_magazine[i]:
            return False
    return True


"""
    Test Cases

"""

ransomNote = " give me your money no" #Input for TC - 1
magazine = " money your give hello how arezzzz you no me"

magazine_1 = "aabcccccccccc" #Input for TC - 2
ransomNote_1 = "bcccdcca"
print "Output from Method 1: " + str(CanConstructMethod1(ransomNote,magazine))
print "Output from Method 2: " + str(CanConstructMethod2(ransomNote_1,magazine_1))
