
def sprawdza_czy_palindrom(x):
    """ 
    Funkcja sprawdza czy dany zrot, 
    słowo zestaw cyfr itp. jest palidormem 
    tzn. czy dany zestaw znaków pisany na wspak
    jest taki sam jak pisany oryginalnie np
    kajak = kajak od tyłu
    12sas21 = 12sas21
    """

    x = input("Wpisz zwrot : ")

    odwroc = x[::-1]

    if( x == odwroc ):
        print ("TRUE - yes it is palindrome")
    else:
        print ("FALSE - it is not palindrome")

sprawdza_czy_palindrom('')

print("Przepraszam za spoźnienie z zadaniem, ale wyjechałem na tydzień i nie spodziewałem sie zę tam gdzie będę nie będzie internetu, teraz postaram się nadgonić materiał")