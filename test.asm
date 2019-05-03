DEFAULT REL
extern printf
extern fflush
global main
section .data
a dd 'hello',0
section .text
main:
mov rcx, a
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
