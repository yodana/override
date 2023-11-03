global _start

_start:
    xor ecx, ecx
    push ecx
    push "sswd"
    push "//pa"
    push "/etc"
    mov ebx, esp
    xor eax, eax
    cdq
    mov al, 05H
    int 80H
    mov edi, eax
    mov dl, 1+0FEH
reading:
    mov ecx, esp
    mov ebx, edi
    mov al, 03H
    int 80H
    mov bl,1
    mov al, 04H
    int 80H
    dec dl
    cmp dl, 1H
    jz exit
    jmp reading
exit:
    