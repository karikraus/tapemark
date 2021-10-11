#!/usr/bin/env python3
import random
import sys
 
versi = \
[[" l accecante   /  globo  /  di fuoco  ", "1/4", "2/3", "1"],\
[" si espande   /  rapidamente  ", "1/2", "3/4", "1"],\
[" trenta volte  / piu luminoso  / del sole ", "2/3", "2/4", "1"],\
[" quando  raggiunge / la stratosfera  ", "3/4", "1/2", "1"],\
[" la  sommita  /  della nuvola ", "1/3", "2/3", "1"],\
[" assume   / la ben nota forma  / di fungo ", "2/4", "3/4", "1"], \

[" la testa / premuta  / sulla spalla  ", "1/4", "2/4", "2"],\
[" i  capelli   /  tra le labbra ", "1/4", "2/4", "2"],\
[" giacquero  /   immobili / senza parlare ", "2/3", "2/3", "2"],\
[" finche non mosse  /  le dita  / lentamente    ", "3/4", "1/3", "2"],\
[" cercando / di afferrare  ", "3/4", "1/2", "2"],\

[" mentre la moltitudine  /  delle cose  /   accade   ", "1/2", "1/2", "3"],\
[" io contemplo  /  il loro ritorno    ", "2/3", "3/4", "3"],\
[" malgrado / che le cose  /  fioriscano    ", "1/2", "2/3", "3"],\
[" esse tornano  / tutte    / alla loro radice   ", "2/3", "1/4", "3"]]

#~ gruppo "1", 0-5: Diario di Hiroshima, di Michihito Hachiya
#~ gruppo "2", 6-10: Il Mistero dell'ascensore, di Paul Goldwin
#~ gruppo "3", 11-14: Tao te King, di Lao Tse

random.shuffle(versi)
strofa_uno = [None] * 10
strofa_uno[0] = versi[0]
versi.remove(strofa_uno[0])


try:
    i = 0 ; j = 0
    while j < 9:
        if (versi[i][1][0] == strofa_uno[j][2][0] \
        or versi[i][1][2] == strofa_uno[j][2][0] \
        or versi[i][1][2] == strofa_uno[j][2][2]) \
        and versi[i][3] != strofa_uno[j][3]:
            # se le strofe "stanno bene insieme"
            # e non appartengono allo stesso gruppo
            strofa_uno[j+1] = versi[i]
            versi.remove(versi[i])
            i = 0
            j += 1
        # altrimenti, esamina l'elemento successivo
        else:
            i += 1
            continue

# se la combinazione in esame non soddisfa le condizioni, viene scartata
except: sys.exit()


strofa = []
for k in range(len(strofa_uno)):
	strofa.append(strofa_uno[k][0])

s = '/'.join(strofa).split("/")

print("")

for k in range(len(s)):
	
	if k == (len(s) - 1): sys.stdout.write(s[k].upper())
	else: sys.stdout.write(s[k].upper())

    # senza la seguente istruzione l'output di una strofa
    # viene formattato come nel tabulato originale, senza 'a capo'
    
	# if k > 0 and (k+1)%4 == 0: print ""
	
print("")