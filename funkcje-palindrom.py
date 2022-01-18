
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

    reverse = x[::-1]

    if( x == reverse ):
        print(x == reverse) 
    else :   
        print(x == reverse) 
   
check_palindrom('')
