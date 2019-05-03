DEFAULT REL
extern printf
extern fflush
global main
section .data
a db 1
_STR0 db 'n', 0
section .text
main:
mov rcx, _STR0
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
