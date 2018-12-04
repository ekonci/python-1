#-*- coding: utf-8 -*-

secret = 8

guess = int(raw_input("Ugibaj skrito številko (1-10): "))

if secret == guess:
    print "Bravo! Uspelo ti je uganiti. Število je bilo 8."

else:
    print "Ni ti uspelo uganiti."
    print "Poskusi ponovno, ta številka ni enaka  " + str(guess)

