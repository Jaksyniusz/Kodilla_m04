#1
def is_palindrome(word):
    word_reversed = word[::-1]
    return word == word_reversed


#2
def is_palindrome2(word):
    letter_list = list(word)
    letter_list.reverse()
    result = "".join(letter_list)
    return result == word


#3
def is_palindrome3(word):
    return "".join(reversed(word)) == word


#4
def is_palindrome4(word):
    rev_word = ""
    for letter in word:
        rev_word = letter + rev_word
    return rev_word == word


#5
def is_palindrome5(word):
    rev_word = ""
    w_lenght = len(word) - 1

    while w_lenght >= 0:
        rev_word = rev_word + word[w_lenght]
        w_lenght = w_lenght - 1
    return rev_word == word


print(is_palindrome("ojciec"))
print(is_palindrome2("ojciec"))
print(is_palindrome3("ojciec"))
print(is_palindrome4("ojciec"))
print(is_palindrome5("ojciec"))