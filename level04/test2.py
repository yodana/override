from pwn import asm, context

# Définir l'architecture cible (32 bits)
context.arch = 'i386'
# Assembler le code
shellcode = asm("push 0")

# Afficher le shellcode en format hexadécimal
print(shellcode.encode('hex'))