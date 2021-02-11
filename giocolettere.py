                      #giochino con lettere 
print("""                        BENVENUTO
      X OGNI PAROLA CHE INSERISCI GUADAGNERAI 1 PUNTO 
                  scrivi tutto in minuscolo """)

punti=0
user="cese"
while 'cese' in user:
    user = input('scrivi parole con cese: ')
    punti=punti+1
    print("score:")
    print(punti)
print("il tuo punteggio è {}".format(punti))
