def check_palindrom(x):
    """ 
    Funkcja sprawdza czy dany zrot, 
    słowo zestaw cyfr itp. jest palidormem 
    tzn. czy dany zestaw znaków pisany na wspak
    jest taki sam jak pisany oryginalnie np
    kajak = kajak od tyłu
    12sas21 = 12sas21
    """

    x = input("Wpisz zwrot : ")
    if (x == x[::-1]):
        return True
    return False  

result = check_palindrom("kajak")
print(result)

