def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    
    # TODO: Write your solution here
    list_our_string = list(our_string)
    length_of_string = len(our_string)
    first = 0
    last = length_of_string - 1
    while(first < last):
        temp = list_our_string[first]
        list_our_string[first] = list_our_string[last]
        list_our_string[last] = temp
        first += 1
        last -= 1
    output_string = ''.join(list_our_string)
    return output_string
    
    pass

# Test Cases

print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")