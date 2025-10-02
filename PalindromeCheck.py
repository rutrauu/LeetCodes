def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start +=1
        end -=1

    return True

frase = "a b c d c b a"
is_palindrome(frase)