def generate_hashtag(s : str):
    return '#' + ''.join(s.title().split())

def generate_str(n):
    from random import choice
    from string import ascii_letters

    
    res = ''
    for _ in range(n):
        res += choice(seq = ascii_letters + ' ')
        
generate_hashtag(generate_str(123)) #?