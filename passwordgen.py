import random
import pyperclip

text = '1234567890QWERTYUIOP[]\\ASDFGHJKLZXCVBNM./qwertyuiopasdfghjklzxcvbnm;:<>?{}#%!()_-=+'
alphabet = list(text)
k = None

def generate_password(k):
    if k in range(1, 101):
        p_list = [random.choice(alphabet) for _ in range(k)]
        return ''.join(p_list)
    else:
        raise ValueError("Length must be between 1 and 100.")

def copy_to_clipboard(password):
    pyperclip.copy(password)
