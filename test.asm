DEFAULT REL
extern printf
extern fflush
global main
section .data
a dq  "%d ", 1
section .text
main:
mov rax, 1
mov rbx, 2
add rbx, rax
push rbx
xor rax,rax
mov rax, 3
mov rbx, 4
add rbx, rax
push rbx
xor rax,rax
pop rbx
mov rcx,rbx
pop rbx
add rbx,rcx
xor rcx,rcx
push rbx
xor rax,rax
mov rbx, 5
mov rax, [a+8]
add rbx,rax
push rbx
xor rax,rax
pop rbx
mov rcx,rbx
pop rbx
add rbx,rcx
xor rcx,rcx
push rbx
xor rax,rax
mov rax, 7
mov rbx, 8
add rbx, rax
push rbx
xor rax,rax
pop rbx
mov rcx,rbx
pop rbx
add rbx,rcx
xor rcx,rcx
push rbx
xor rax,rax
pop rbx
mov [a+8],rbx
xor rbx,rbx
mov rcx, a
mov rdx, [a +8]
call printf
xor rcx, rcx
call fflush

xor rax, rax
pop rbp
ret
