def is_palindrome(text):
    list_txt = [i.lower() for i in text if i.isalpha()]
    list_check = list_txt.copy()
    list_check.reverse()
    if list_txt == list_check:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))