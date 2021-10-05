def password_generator():    
    import random

    flag=True

    while flag:
        nc=int(input("Number of characters:"))
        nu=int(input("Number of upper case letters:"))
        nl=int(input("Number of lower case letters:"))
        nd=int(input("Number of digits:"))
        ns=int(input("Number of symbols:"))

        if nu+nl+nd+ns>nc:
            print("character numbers do not match")
        else:
            flag=False

    n_extra=nc-(nu+nl+nd+ns)
    
    get_characters=lambda cl,n:[random.choice(cl) for i in range(n)]

    digits=[str(i) for i in range(10)]
    digit_char=get_characters(digits,nd)

    upper_case_letters=[chr(i) for i in range(65,91)]
    upper_char=get_characters(upper_case_letters,nu)

    lower_case_letters=[chr(i) for i in range(97,123)]
    lower_char=get_characters(lower_case_letters,nl)

    symbols=[chr(i) for i in range(32,48)]+[chr(i) for i in range(58,65)]+[chr(i) for i in range(91,97)]+[chr(i) for i in range(123,127)]
    symbol_char=get_characters(symbols,ns)

    character_list=digits+upper_case_letters+lower_case_letters+symbols
    extra_char=get_characters(character_list,n_extra)

    password_letters=digit_char+upper_char+lower_char+symbol_char+extra_char
    random.shuffle(password_letters)

    password="".join(password_letters)
    
    return password
  
#Number of characters:5
#Number of upper case letters:1
#Number of lower case letters:2
#Number of digits:1
#Number of symbols:1

#'b*Sm5'
