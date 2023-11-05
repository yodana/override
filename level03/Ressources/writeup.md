# Override / Level04

## Lire le fichier level03

Cette fois ci on change un peu, j'ai utiliser chatgpt pour me rendre le code asm lisible a la place de chatgpt. Le code est dans source.c

## Vulnerabilite

On peut voir dans source.c que pour avoir le code "Congraluations!" qui nous permet d'acceder au /bin/sh on doit faire face a ce cryptage:
`input ^= key[i % key_length];`

Avec decrypt.py, on peut voir que l'input doit etre 18.
Mais juste avant on a cette ligne

`test(0x1337d00d, input);`

`int difference = input_2 - input_1;`

Je dois juste faire la diff entre 1337d00d et mon input pour donner 18.
Donc 1337CFFB, 322424827 en hex

> (python -c 'print "322424827"'; cat) | ./level03