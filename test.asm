DEFAULT REL
extern printf
extern fflush
global main
section .data
a dq  "%d ", 0
b dq  "%d ", 0
section .text
main:
if0:
mov rax, [a+8]
mov rbx,0
cmp rax,rbx
jne end0
end0:
xor rax, rax
pop rbp
ret
