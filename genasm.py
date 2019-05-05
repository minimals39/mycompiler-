import sys

#Global Var

lexer = None

asmheader = ("DEFAULT REL\n" +
             "extern printf\n" +
             "extern fflush\n" +
             "global main\n")
asmdata = 'section .data\n'
asmtext = "section .text\n" + "main:\n"
asmexit = 'xor rax, rax\npop rbp\nret\n'

fflush_label = "fflush"

empty_str = '""'
str_prefix = "_STR"
int_prefix = "_INT"
global_var2 = {}
global_int_counter = 0
global_str_counter = 0
global_int = {}
global_str = {}
global_var = []
global global_if_counter
global global_while_counter
global_if_counter = 0
global_if_stack = []
global_while_counter = 0
global_while_stack = []

str_prefix = "_STR"

reg_order = ["rcx", "rdx", "r8", "r9"]

#------------------------------------ Get Set Add Function
def checktype(a,b):
    if global_var2[a] == global_var2[b]:
        return True
    else:
        return False

def get_var(symbol):
    if symbol in global_var:
        return symbol
    print_error("Use of undeclare variable %s" % symbol)

def print_error(error_str, show_line=True):
    if show_line:
        print("ERROR : %s At line %d" % (error_str, lexer.lineno))
    else:
        print("ERROR : %s" % error_str)
    sys.exit(1)

def getHeader():
    global asmheader
    return asmheader

def getData():
    global asmdata
    return asmdata

def getText():
    global asmtext
    return asmtext

def getLeave():
    global asmexit
    return asmexit

#------------------------------------ Add Assembly code section
def addDataInt(name, value):
    global asmdata
    asmdata += "%s dq %s\n" % (name, value)

def addDataString(name, value):
    global asmdata
    asmdata += "%s db %s\n" % (name, value)

def addText(asmcode = ""):
    global asmtext
    asmtext += asmcode + "\n"

def addComment(cmd = ""):
    global asmtext
    asmtext += ";" + cmd +"\n"

#------------------------------------ Choose Function Section

def getFunction(Tuple):
    if Tuple[0] is  "End": #Found an error or EoF
        print("EoF")
        return "Exit"

    else:
        if type(Tuple[1]) == tuple :
            TempTuple = Tuple[1]
            return TempTuple[0]
        else :
            return Tuple[0]
def statement_main(tuple):
    ThisTuple = tuple
    state = getFunction(ThisTuple)
    stateTuple = ThisTuple[1]
    if state == "Exit":
        addText("")
        addComment("")
        addText(asmexit)
    elif state == "decl":
        print("")
        declaration_routine(stateTuple)
    elif state == "var_array":
        print("")
        Array_routine(stateTuple)
    elif state == "multiple_stm":
        print("")
        multiple_stm_routine(stateTuple)
    elif state == "print":
        print("")
        print_routine(stateTuple)
    elif state == "assign":
        print("")
        assign_routine(stateTuple)
    elif state == "if":
        print("")
        if_routine(stateTuple)
    elif state == "repeat":
        print("")
        repeat_routine(stateTuple)
        #Next STM
    try :ThisTuple = ThisTuple[2]
    except :
        pass
    print("-----------------------------")

def statement_main_from_multi(tuple):
    ThisTuple = tuple
    state = ThisTuple[0]
    stateTuple = ThisTuple
    if state == "Exit":
        addText("")
        addComment("")
        addText(asmexit)
    elif state == "decl":
        print("")
        declaration_routine(stateTuple)
    elif state == "var_array":
        print("")
        Array_routine(stateTuple)
    elif state == "multiple_stm":
        print("")
        multiple_stm_routine(stateTuple)
    elif state == "print":
        print("")
        print_routine(stateTuple)
    elif state == "assign":
        print("")
        assign_routine(stateTuple)
    elif state == "if":
        print("")
        if_routine(stateTuple)
    elif state == "repeat":
        print("")
        repeat_routine(stateTuple)

        #Next STM
    try :ThisTuple = ThisTuple[2]
    except :
        pass
    print("-----------------------------")


#------------------------------------ All Function Section
def if_routine(stm):
    global global_if_counter
    global_if_stack.append(global_if_counter)
    ifcounter = global_if_counter
    if_symbol = 'if'+str(ifcounter)
    global_if_counter += 1
    addText("%s:" %if_symbol)
    cmpexp = stm[1]
    doing = stm[2]
    endif = 'end' + str(global_if_stack.pop())
    if (cmpexp[0]=='==' or cmpexp[0]=='<<'or cmpexp[0]=='>>'or cmpexp[0]=='<=>' ):
        cmp_routine(cmpexp,endif)
    else:
        print_error("no syntax")
    statement_main_from_multi(doing)
    addText("%s:" % endif)

def repeat_routine(stm):
    global global_while_counter
    global_while_stack.append(global_while_counter)
    whilecounter = global_while_counter
    while_symbol = 'loop'+str(whilecounter)
    global_while_counter += 1
    addText("%s:" %while_symbol)
    cmpexp = stm[1]
    doing = stm[2]
    endloop = 'endloop' + str(global_while_stack.pop())
    if (cmpexp[0]=='==' or cmpexp[0]=='<<'or cmpexp[0]=='>>'or cmpexp[0]=='<=>' ):
        cmp_routine(cmpexp,endloop)
    else:
        print_error("no syntax")
    statement_main_from_multi(doing)
    addText("jmp %s" % while_symbol)
    addText("%s:" % endloop)

def cmp_routine(stm,endif):
    if(stm[0] == '=='):
        equal(stm,endif)
    elif(stm[0] == '>>'):
        greater(stm,endif)
    elif (stm[0] == '<<'):
        less(stm,endif)
    elif (stm[0] == '<=>'):
        noequal(stm,endif)

def greater(stm,endif):
    if type(stm[1]) == str:
        if stm[1] in global_var2:
            if global_var2[stm[1]] == 'int':
                addText("mov rax, [%s+8]" % stm[1])
            else:
                print_error("wrong Type")
        else:
            print_error("you didnt declare this variable")
    elif type(stm[1]) == int:
        addText("mov rax,%s" % stm[1])


    if type(stm[2]) == str:
        if stm[2] in global_var2:
            if global_var2[stm[2]] == 'int':
                addText("mov rbx, [%s+8]" % stm[2])
            else:
                print_error("wrong Type")
        else:
            print_error("you didnt declare this variable")
    elif type(stm[2]) == int:
        addText("mov rbx,%s" % stm[2])

    addText("cmp rax,rbx")
    addText("jle %s" % endif)

def less(stm,endif):
    if type(stm[1]) == str:
        if stm[1] in global_var2:
            if global_var2[stm[1]] == 'int':
                addText("mov rax, [%s+8]" % stm[1])
            else:
                print_error("wrong Type")
        else:
            print_error("you didnt declare this variable")
    elif type(stm[1]) == int:
        addText("mov rax,%s" % stm[1])


    if type(stm[2]) == str:
        if stm[2] in global_var2:
            if global_var2[stm[2]] == 'int':
                addText("mov rbx, [%s+8]" % stm[2])
            else:
                print_error("wrong Type")
        else:
            print_error("you didnt declare this variable")
    elif type(stm[2]) == int:
        addText("mov rbx,%s" % stm[2])

    addText("cmp rax,rbx")
    addText("jge %s" % endif)

def noequal(stm,endif):
    if type(stm[1]) == str:
        if stm[1] in global_var2:
            if global_var2[stm[1]] == 'int':
                addText("mov rax, [%s+8]" % stm[1])
            else:
                print_error("wrong Type")
        else:
            print_error("you didnt declare this variable")
    elif type(stm[1]) == int:
        addText("mov rax,%s" % stm[1])


    if type(stm[2]) == str:
        if stm[2] in global_var2:
            if global_var2[stm[2]] == 'int':
                addText("mov rbx, [%s+8]" % stm[2])
            else:
                print_error("wrong Type")
        else:
            print_error("you didnt declare this variable")
    elif type(stm[2]) == int:
        addText("mov rbx,%s" % stm[2])

    addText("cmp rax,rbx")
    addText("je %s" % endif)

def equal(stm,endif):
    if type(stm[1]) == str:
        if stm[1] in global_var2:
            if global_var2[stm[1]] == 'int':
                addText("mov rax, [%s+8]" % stm[1])
            else:
                print_error("wrong Type")
        else:
            print_error("you didnt declare this variable")
    elif type(stm[1]) == int:
        addText("mov rax,%s" % stm[1])

    elif type(stm[1]) == tuple:
        if stm[1][0] == 'MUL' or stm[1][0] == 'MINUS'  or stm[1][0] == 'PLUS':
            expression_select(stm[1])
            addText("pop rbx")
            addText("mov rax,rbx" )
        if stm[1][0] == 'MOD':
            expression_select(stm[1])
            addText("pop ax")
            addText("mov cl, ah")
            addText("movsx rax, cl")

    if type(stm[2]) == str:
        if stm[2] in global_var2:
            if global_var2[stm[2]] == 'int':
                addText("mov rbx, [%s+8]" % stm[2])
            else:
                print_error("wrong Type")
        else:
            print_error("you didnt declare this variable")
    elif type(stm[2]) == int:
        addText("mov rbx,%s" % stm[2])



    addText("cmp rax,rbx")
    addText("jne %s" % endif)
def assign_routine(stm):
    if type(stm[2]) == str:
        if stm[2][0] == '"':
            if stm[1] not in global_var2:
                print_error("you doesnt declare variable %s " % stm[1])
            elif global_var2[stm[1]] != 'string':
                print_error("Wrong type ")
            else:
                textstr = get_str(stm[2][1:-1])
                addText("mov rax, [%s]" % textstr)
                addText("mov [%s], rax" % stm[1])
        else:
            if stm[1] not in global_var2:
                print("you doesnt declare variable ",stm[1])
            elif stm[2] not in global_var2:
                print("you doesnt declare ",stm[2])
            elif checktype(stm[1],stm[2]):
                if (global_var2[stm[1]] == 'int') and (global_var2[stm[2]] == 'int'):
                    addText("mov rax, [%s+8]" % stm[2])
                    addText("mov [%s+8], rax" % stm[1])
                elif global_var2[stm[1]] == 'string' and global_var2[stm[2]] == 'string':
                    addText("mov rax, [%s]" % stm[2])
                    addText("mov [%s], rax" % stm[1])
    elif type(stm[2]) == int:
        if type(stm[1]) == tuple:
            if stm[1][0] == 'array':
                if stm[1][1] not in global_var2:
                    print_error("you didnt declare this variable")
                else:
                    if type(stm[1][2]) == int:
                        element = (stm[1][2]+1) * 8
                        addText("mov rax, %s" % stm[2])
                        addText("mov [%s+%s],rax" % (stm[1][1],element))
                    elif type(stm[1][2]) == str:
                        if stm[1][2][0] == '"':
                            print_error("cant")
                        else:
                            if stm[1][2] not in global_var2:
                                print_error("you didnt declare")
                            else:
                                if global_var2[stm[1][2]] == 'int':
                                    addText("mov rax,%s"% stm[2])
                                    addText("mov rbx, [%s+8]"% stm[1][2])
                                    addText("mov [%s+rbx*8],rax" % stm[1][1])
        elif stm[1] not in global_var2:
            print_error("you doesnt declare variable  ")
        elif global_var2[stm[1]] != 'int':
            print_error("Wrong type ")
        else:
            textint = get_int(str(stm[2]))
            addText("mov rax, [%s+8]" % textint)
            addText("mov [%s+8], rax" % stm[1])
    else:
        if type(stm[2]) == tuple:
            if stm[2][0] == 'MUL' or stm[2][0] == 'MINUS' or stm[2][0] == 'PLUS' :
                expression_select(stm[2])
                addText("pop rbx")
                addText("mov [%s+8],rbx" % stm[1])
                addText("xor rbx,rbx")
            if   stm[2][0] == 'MOD' :
                expression_select(stm[2])
                addText("pop ax")
                addText("mov [%s+8],ah" % stm[1])
            if   stm[2][0] == 'DIV' :
                expression_select(stm[2])
                addText("pop ax")
                addText("mov [%s+8],al" % stm[1])
def expression_select(state):
    if state[0] == 'PLUS':
        plus_routine(state)
    elif state[0] == 'MINUS':
        sub_routine(state)
    elif state[0] == 'MUL':
        mul_routine(state)
    elif state[0] == 'DIV':
        div_routine(state)
    elif state[0] == 'MOD':
        mod_routine(state)
#--------------------------------------------Maths-------------------
def plus_routine(stm):
    if type(stm[1]) == int and type(stm[2]) == int :
        addText("mov rax, %s" % stm[1])
        addText("mov rbx, %s" % stm[2])
        addText("add rbx, rax")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2]) == tuple:
        expression_select(stm[1])
        expression_select(stm[2])
        addText("pop rbx")
        addText("mov rcx,rbx")
        addText("pop rbx")
        addText("add rbx,rcx")
        addText("xor rcx,rcx")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2]) == int:
        expression_select(stm[1])
        addText("pop rbx")
        addText("mov rax, %s"%stm[2])
        addText("add rbx,rax")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2] )== str:
        if stm[2] not in global_var2:
            print("111111111")
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            expression_select(stm[1])
            addText("pop rbx")
            addText("mov rax, [%s+8]"%stm[2])
            addText("add rbx,rax")
            addText("push rbx")
    if type(stm[1]) == int and type(stm[2]) == str:
        print(type(stm[2]))
        if stm[2] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, %s" % stm[1])
            addText("mov rax, [%s+8]" % stm[2])
            addText("add rbx,rax")
            addText("push rbx")
    if type(stm[1]) == str and type(stm[2]) == int:
        print("33333333333")
        if stm[1] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, [%s+8]" % stm[1])
            addText("mov rax, %s" % stm[2])
            addText("add rbx,rax")
            addText("push rbx")
    if type(stm[1]) == str and type(stm[2]) == str:
        print("4444444444")
        if stm[2] not in global_var2 and stm[1] not in global_var2:
            print_error("you doesnt declare variable ")
        elif global_var2[stm[2]] != 'int' and global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, [%s+8]" % stm[1])
            addText("mov rax, [%s+8]" % stm[2])
            addText("add rbx,rax")
            addText("push rbx")
    addText("xor rax,rax")

def sub_routine(stm):
    if type(stm[1]) == int and type(stm[2]) == int :
        addText("mov rax, %s" % stm[1])
        addText("mov rbx, %s" % stm[2])
        addText("sub rbx, rax")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2]) == tuple:
        sub_routine(stm[1])
        sub_routine(stm[2])
        addText("pop rbx")
        addText("mov rcx,rbx")
        addText("pop rbx")
        addText("sub rbx,rcx")
        addText("xor rcx,rcx")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2]) == int:
        sub_routine(stm[1])
        addText("pop rbx")
        addText("mov rax, %s"%stm[2])
        addText("sub rbx,rax")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2] )== str:
        if stm[2] not in global_var2:
            print("111111111")
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            sub_routine(stm[1])
            addText("pop rbx")
            addText("mov rax, [%s+8]"%stm[2])
            addText("sub rbx,rax")
            addText("push rbx")
    if type(stm[1]) == int and type(stm[2]) == str:
        print(type(stm[2]))
        if stm[2] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, %s" % stm[1])
            addText("mov rax, [%s+8]" % stm[2])
            addText("sub rbx,rax")
            addText("push rbx")
    if type(stm[1]) == str and type(stm[2]) == int:
        print("33333333333")
        if stm[1] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, [%s+8]" % stm[1])
            addText("mov rax, %s" % stm[2])
            addText("sub rbx,rax")
            addText("push rbx")
    if type(stm[1]) == str and type(stm[2]) == str:
        print("4444444444")
        if stm[2] not in global_var2 and stm[1] not in global_var2:
            print_error("you doesnt declare variable ")
        elif global_var2[stm[2]] != 'int' and global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, [%s+8]" % stm[1])
            addText("mov rax, [%s+8]" % stm[2])
            addText("sub rbx,rax")
            addText("push rbx")
    addText("xor rax,rax")

def mul_routine(stm):
    if type(stm[1]) == int and type(stm[2]) == int :
        addText("mov rax, %s" % stm[1])
        addText("mov rbx, %s" % stm[2])
        addText("imul rbx, rax")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2]) == tuple:
        expression_select(stm[1])
        expression_select(stm[2])
        addText("pop rbx")
        addText("mov rcx,rbx")
        addText("pop rbx")
        addText("imul rbx,rcx")
        addText("xor rcx,rcx")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2]) == int:
        expression_select(stm[1])
        addText("pop rbx")
        addText("mov rax, %s"%stm[2])
        addText("imul rbx,rax")
        addText("push rbx")
    if type(stm[1]) == tuple and type(stm[2] )== str:
        if stm[2] not in global_var2:
            print("111111111")
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            expression_select(stm[1])
            addText("pop rbx")
            addText("mov rax, [%s+8]"%stm[2])
            addText("imul rbx,rax")
            addText("push rbx")
    if type(stm[1]) == int and type(stm[2]) == str:
        print(type(stm[2]))
        if stm[2] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, %s" % stm[1])
            addText("mov rax, [%s+8]" % stm[2])
            addText("imul rbx,rax")
            addText("push rbx")
    if type(stm[1]) == str and type(stm[2]) == int:
        print("33333333333")
        if stm[1] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, [%s+8]" % stm[1])
            addText("mov rax, %s" % stm[2])
            addText("imul rbx,rax")
            addText("push rbx")
    if type(stm[1]) == str and type(stm[2]) == str:
        print("4444444444")
        if stm[2] not in global_var2 and stm[1] not in global_var2:
            print_error("you doesnt declare variable ")
        elif global_var2[stm[2]] != 'int' and global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov rbx, [%s+8]" % stm[1])
            addText("mov rax, [%s+8]" % stm[2])
            addText("imul rbx,rax")
            addText("push rbx")
    addText("xor rax,rax")

def div_routine(stm):
    if type(stm[1]) == int and type(stm[2]) == int :
        addText("mov ax, %s" % stm[1])
        addText("xor rdx, rdx")
        addText("mov bl, %s" % stm[2])
        addText("div bl")
        addText("push ax")
    if type(stm[1]) == tuple and type(stm[2]) == tuple:
        expression_select(stm[1])
        expression_select(stm[2])
        if stm[1][0] == 'MUL' or stm[1][0] == 'MINUS' or stm[1][0] == 'DIV' or stm[1][0] == 'PLUS':
            addText("pop rbx")
            addText("mov ax,rbx")
        elif stm[1][0] == 'MOD':
            addText("pop ax")
            addText("mov ax,al")
        if stm[2][0] == 'MUL' or stm[2][0] == 'MINUS' or stm[2][0] == 'DIV' or stm[2][0] == 'PLUS':
            addText("pop rbx")
            addText("mov bl,rbx")
        elif stm[2][0] == 'MOD':
            addText("pop ax")
            addText("mov bl,al")
        addText("div bl")
        addText("push ax")
    if type(stm[1]) == tuple and type(stm[2]) == int:
        expression_select(stm[1])
        if stm[1][0] == 'MUL' or stm[1][0] == 'MINUS' or stm[1][0] == 'DIV' or stm[1][0] == 'PLUS':
            addText("pop rbx")
            addText("mov ax,rbx")
        elif stm[1][0] == 'MOD':
            addText("pop ax")
            addText("mov ax,al")
        addText("mov bl, %s"%stm[2])
        addText("div bl")
        addText("push ax")
    if type(stm[1]) == tuple and type(stm[2] )== str:
        if stm[2] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            expression_select(stm[1])
            if stm[1][0] == 'MUL' or stm[1][0] == 'MINUS' or stm[1][0] == 'DIV' or stm[1][0] == 'PLUS':
                addText("pop rbx")
                addText("mov ax,rbx")
            elif stm[1][0] == 'MOD':
                addText("pop ax")
                addText("mov ax,al")
            addText("mov bl, [%s+8]"%stm[2])
            addText("div bl")
            addText("push ax")
    if type(stm[1]) == int and type(stm[2]) == str:
        print(type(stm[2]))
        if stm[2] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov ax, %s" % stm[1])
            addText("mov bl, [%s+8]" % stm[2])
            addText("div bl")
            addText("push ax")
    if type(stm[1]) == str and type(stm[2]) == int:
        print("33333333333")
        if stm[1] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov ax, [%s+8]" % stm[1])
            addText("mov bl, %s" % stm[2])
            addText("div bl")
            addText("push ax")
    if type(stm[1]) == str and type(stm[2]) == str:
        print("4444444444")
        if stm[2] not in global_var2 and stm[1] not in global_var2:
            print_error("you doesnt declare variable ")
        elif global_var2[stm[2]] != 'int' and global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov ax, [%s+8]" % stm[1])
            addText("mov bl, [%s+8]" % stm[2])
            addText("div bl")
            addText("push ax")
    addText("xor al,al")
#---------------------------------------mod how2---------------------------
def mod_routine(stm):
    if type(stm[1]) == int and type(stm[2]) == int :
        addText("mov ax, %s" % stm[1])
        addText("xor rdx, rdx")
        addText("mov bl, %s" % stm[2])
        addText("div bl")
        addText("push ax")
    if type(stm[1]) == tuple and type(stm[2]) == tuple:
        expression_select(stm[1])
        expression_select(stm[2])
        if stm[1][0] == 'MUL' or stm[1][0] == 'MINUS' or stm[1][0] == 'DIV' or stm[1][0] == 'PLUS':
            addText("pop rbx")
            addText("mov ax,rbx")
        elif stm[1][0] == 'MOD':
            addText("pop ax")
            addText("mov ax,ah")
        if stm[2][0] == 'MUL' or stm[2][0] == 'MINUS' or stm[2][0] == 'DIV' or stm[2][0] == 'PLUS':
            addText("pop rbx")
            addText("mov bl,rbx")
        elif stm[2][0] == 'MOD':
            addText("pop ax")
            addText("mov bl,ah")
        addText("div bl")
        addText("push ax")
    if type(stm[1]) == tuple and type(stm[2]) == int:
        expression_select(stm[1])
        if stm[1][0] == 'MUL' or stm[1][0] == 'MINUS' or stm[1][0] == 'DIV' or stm[1][0] == 'PLUS':
            addText("pop rbx")
            addText("mov ax,rbx")
        elif stm[1][0] == 'MOD':
            addText("pop ax")
            addText("mov ax,ah")
        addText("mov bl, %s"%stm[2])
        addText("div bl")
        addText("push ax")
    if type(stm[1]) == tuple and type(stm[2] )== str:
        if stm[2] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            expression_select(stm[1])
            if stm[1][0] == 'MUL' or stm[1][0] == 'MINUS' or stm[1][0] == 'DIV' or stm[1][0] == 'PLUS':
                addText("pop rbx")
                addText("mov ax,rbx")
            elif stm[1][0] == 'MOD':
                addText("pop ax")
                addText("mov ax,ah")
            addText("mov bl, [%s+8]"%stm[2])
            addText("div bl")
            addText("push ax")
    if type(stm[1]) == int and type(stm[2]) == str:
        print(type(stm[2]))
        if stm[2] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[2]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov ax, %s" % stm[1])
            addText("mov bl, [%s+8]" % stm[2])
            addText("div bl")
            addText("push ax")
    if type(stm[1]) == str and type(stm[2]) == int:
        print("33333333333")
        if stm[1] not in global_var2:
            print_error("you doesnt declare variable %s " % stm[1])
        elif global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov ax, [%s+8]" % stm[1])
            addText("mov bl, %s" % stm[2])
            addText("div bl")
            addText("push ax")
    if type(stm[1]) == str and type(stm[2]) == str:
        print("4444444444")
        if stm[2] not in global_var2 and stm[1] not in global_var2:
            print_error("you doesnt declare variable ")
        elif global_var2[stm[2]] != 'int' and global_var2[stm[1]] != 'int':
            print_error("wrong input type")
        else:
            addText("mov ax, [%s+8]" % stm[1])
            addText("mov bl, [%s+8]" % stm[2])
            addText("div bl")
            addText("push ax")
    addText("xor ah,ah")

def multiple_stm_routine(stm):
    statement_main_from_multi(stm[1])
    statement_main_from_multi(stm[2])

def declare_var(var_name, value, assign=None):
    global global_var
    global asmdata

    if var_name in global_var:
        print("Error!, Duplicate var is declared")
    else:
        global_var.append(var_name)
        print(global_var)
        if assign != 'array':
            if assign == 'int':
                global_var2[var_name] = 'int'
                addDataInt(var_name, value)
            elif assign == 'string':
                global_var2[var_name] = 'string'
                addDataString(var_name, value)
        elif assign == "array":
            asmdata += var_name + ' dq "%d " '
            for i in range(value-1):
                asmdata += ',0'
            asmdata += "\n"
            global_var2[var_name] = 'array'
        elif assign == None:
            print("something is wrong law na")

def declaration_routine(stm):
    #print("visited declacration_routine")
    #print(type(stm[2]))
    if stm[1] == "type_s":
        if type(stm[3]) == int:
            stmnum = str(stm[3])
            valuename = "'" + stmnum + "',0"
        else:
            stmsplit = stm[3][1:-1]
            valuename = "'" + stmsplit + "',0"
        declare_var(stm[2],valuename,'string')
    elif stm[1] == "type_n":
        stmint = ' "%d ", '+str(stm[3])
        declare_var(stm[2],stmint,'int')

def Array_routine(stm):
    arrcounter = 1
    declare_var(stm[1],stm[2],"array")
    if type(stm[3]) == tuple:
        thisstm = stm[3]
        while True:
            if thisstm[1] != None:
                addText("mov rax, %s" % thisstm[1])
                addText("mov [%s + %s * 8], rax" % (stm[1], arrcounter))
                arrcounter += 1
                thisstm = thisstm[2]
                if thisstm[1] == None:
                    break

def print_routine(stm):
    print("-> print_routine")
    while True:
        if type(stm[1]) == str:
            if stm[1][0] == '"':
                text = stm[1][1:-1]
                texts = get_str(text)
                addText("mov rcx, %s" % texts)
                addText("call printf")
                addText("xor %s, %s" % (reg_order[0], reg_order[0]))
                addText("call " + fflush_label)
                addText()
                newstm = stm[2]
            else:
                if type(stm[2]) == tuple:
                    if global_var2[stm[1]] == 'int':
                        texts = stm[1]
                        addText("mov rcx, %s" % texts)
                        addText("mov rdx, [%s +8]" % texts)
                        addText("call printf")
                        addText("xor %s, %s" % (reg_order[0], reg_order[0]))
                        addText("call " + fflush_label)
                        addText()
                        newstm = stm[2]
                    elif global_var2[stm[1]] == 'string':
                        texts = stm[1]
                        addText("mov rcx, %s" % texts)
                        addText("call printf")
                        addText("xor %s, %s" % (reg_order[0], reg_order[0]))
                        addText("call " + fflush_label)
                        addText()
                        newstm = stm[2]
        elif type(stm[1]) == int:
            text = str(stm[1])
            texts = get_int(text)
            addText("mov rcx, %s" % texts)
            addText("mov rdx, [%s+8]" % texts)
            addText("call printf")
            addText("xor %s, %s" % (reg_order[0], reg_order[0]))
            addText("call " + fflush_label)
            addText()
            newstm = stm[2]
        elif type(stm[1]) == tuple:
            if stm[1][0] == 'array':
                if stm[1][1] not in global_var2:
                    print_error("you didnt declare this variable")
                else:
                    element = (stm[1][2]+1)*8
                    texts = stm[1][1]
                    addText("mov rcx, %s" % texts)
                    addText("mov rdx, [%s +%s]" % (texts,element))
                    addText("call printf")
                    addText("xor %s, %s" % (reg_order[0], reg_order[0]))
                    addText("call " + fflush_label)
                    addText()
        stm = stm[2]
        if stm[1] == None:
            break

def get_str(text):
    if text not in global_str:
        newstring(text)
    return global_str[text]

def newstring(text):
    global global_str_counter
    if text not in global_str:
        asm_symbol = str_prefix + str(global_str_counter)
        global_str[text] = asm_symbol
        _text = ''
        if '\\n' in text:
            texts = text.replace('"', '').split('\\n')
            for t in texts:
                if t:
                    _text += "'" + t + "', 10,"
            _text += ' 0'
        else:
            _text = "'"+text+"'" + ', 0'
        addDataString(asm_symbol, _text)
        global_str_counter += 1

def get_int(text):
    if text not in global_int:
        newint(text)
    return global_int[text]

def newint(text):
    global global_int_counter
    if text not in global_int:
        asm_symbol = int_prefix + str(global_int_counter)
        global_int[text] = asm_symbol
        _text = '"%d ",'+text
        addDataInt(asm_symbol, _text)
        global_int_counter += 1