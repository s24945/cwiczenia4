def fun(wiadomosc, klucz, alphabet="abcdefghijklmnopqrstuvwxyz"):
    tekst = wiadomosc.lower()
    litery = ''
    for litera in tekst:
        if litera in alphabet:
            litery += litera

    szyfr = ''
    for litera in litery:
        x = alphabet.index(litera)
        szyfr += alphabet[(x + klucz) % len(alphabet)]
    x = 0

    calytekst = ''
    for litera in tekst:
        if litera in alphabet:
            calytekst += szyfr[x]
            x += 1
        else:
            calytekst += litera
    return calytekst

print(fun("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 5))