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
global_var2 = {}
global_str_counter = 0
global_str = {}
global_var = []
global_if_counter = 0

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
    elif state == "print":
        print("")
        print_routine(stateTuple)
    elif state == "assign":
        print("")
        assign_routine(stateTuple)
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
    elif state == "print":
        print("")
        print_routine(stateTuple)
    elif state == "assign":
        print("")
        assign_routine(stateTuple)
    elif state == "WHILELOOP":
        print("")

        #Next STM
    try :ThisTuple = ThisTuple[2]
    except :
        pass
    print("-----------------------------")


#------------------------------------ All Function Section
def assign_routine(stm):
    if checktype(stm[1],stm[2]):


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
            asmdata += var_name + " times " + str(value) + " dq 0" + "\n"
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
    if type(stm[3]) != tuple:
        declare_var(stm[1],stm[2],"array")
    else:
        declare_var(stm[1], stm[2], "array")
        now = stm[3]
        arraynum = 1
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
                if type(stm[1]) == tuple:
                    newstm = stm[2]
                elif type(stm[2]) == tuple:
                    print(global_var2[stm[1]])
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
            texts = get_str(text)
            addText("mov rcx, %s" % texts)
            addText("call printf")
            addText("xor %s, %s" % (reg_order[0], reg_order[0]))
            addText("call " + fflush_label)
            addText()
            newstm = stm[2]

        if stm[1] == None:
            break
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