import copy

def palindrome(word, left_ind, right_ind=-1):
    if left_ind == len(word) // 2:
        return f'{word} is a palindrome'
    if word[left_ind] != word[right_ind]:
        return f'{word} is not a palindrome'
    return palindrome(word, left_ind+1, right_ind-1)

print(palindrome("abca", 0))