DEFAULT REL
extern printf
extern fflush
global main
section .data
a dq  "%d ", 1
b db 'ab',0
section .text
main:
mov rcx, b
call printf
xor rcx, rcx
call fflush

mov rcx, a
mov rdx, [a +8]
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
