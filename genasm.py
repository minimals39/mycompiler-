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
global_str_counter = 0
global_str = {}
global_var = []
global_if_counter = 0

reg_order = ["rcx", "rdx", "r8", "r9"]

#------------------------------------ Get Set Add Function

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
def addData(name, value):
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
    print(Tuple[0])
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
    print(state)
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
    elif state == "PRINT":
        print("")
#       print_routine(stateTuple)
    elif state == "PRINTLN":
        print("")
#       println_routine(stateTuple)
    elif state == "FORLOOP":
        print("")
    elif state == "WHILELOOP":
        print("")

        #Next STM
    try :ThisTuple = ThisTuple[2]
    except :
        pass
    print("-----------------------------")

def statement_main_from_multi(tuple):
    ThisTuple = tuple
    state = ThisTuple[0]
    stateTuple = ThisTuple
    print(state)
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
    elif state == "PRINT":
        print("")
#       print_routine(stateTuple)
    elif state == "PRINTLN":
        print("")
#       println_routine(stateTuple)
    elif state == "FORLOOP":
        print("")
    elif state == "WHILELOOP":
        print("")

        #Next STM
    try :ThisTuple = ThisTuple[2]
    except :
        pass
    print("-----------------------------")


#------------------------------------ All Function Section

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

        if assign is None:
            addData(var_name, value)
        elif assign == "array":
            asmdata += var_name + " times " + str(value) + " dq 0" + "\n"

def declaration_routine(stm):
    #print("visited declacration_routine")
    #print(type(stm[2]))
    if stm[1] == "type_s":
        valuename = "'"+stm[3]+"',0"
        declare_var(stm[2],valuename)
    elif stm[1] == "type_n":
        declare_var(stm[2],stm[3])

def Array_routine(stm):
    if type(stm[3]) != tuple:
        declare_var(stm[1],stm[2],"array")
    else:
        declare_var(stm[1], stm[2], "array")
        now = stm[3]
        arraynum = 0
        while True:
            try:
                if now[0] == "argument":
                    if(now[1] == None):
                        break
                    addText("mov rax, %s" % now[1])
                    addText("mov [%s + %s * 8], rax" % (stm[1], arraynum))
                    arraynum+=1
            except:
                break
            try:
                now = now[2]
            except:
                break


