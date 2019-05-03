DEFAULT REL
extern printf
extern fflush
global main
section .data
a dq "%d " ,0,0,0,0,0,0,0,0,0
_STR0 db '1', 0
section .text
main:
mov rax, 10
mov [a + 1 * 8], rax
mov rax, 20
mov [a + 2 * 8], rax
mov rcx, a
mov rdx,[a+8]
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
