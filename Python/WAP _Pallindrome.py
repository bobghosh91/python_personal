
def checkStringPallindrome(str1='madam'):

    new_str = str1[::-1]

    if (str1 == new_str):
        print('string is pallindrome')
    else:
        print('ain\'t no b')


checkStringPallindrome('arjun')