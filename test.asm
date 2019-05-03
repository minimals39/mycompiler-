DEFAULT REL
extern printf
extern fflush
global main
section .data
a db 1
section .text

main:
mov rcx, a
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
