# Code

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: Write your solution here
    
    str_dict = {}

    for character in str1.replace(" ", ""):
        if character in str_dict:
            str_dict[character] += 1
        else:
            str_dict[character] = 1
    
    for character in str2.replace(" ", ""):
        if character in str_dict:
            str_dict[character] -= 1
        else:
            str_dict[character] = 1

    for character in list(str_dict.values()):
        if character is not 0:
            return False
        else:
            return True

    
    pass

# Test Cases

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")