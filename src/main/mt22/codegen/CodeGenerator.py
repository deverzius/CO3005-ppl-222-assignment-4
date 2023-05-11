from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Visitor import Visitor


class MType:
    def __init__(self, partype: list, rettype: Type):
        self.partype = partype
        self.rettype = rettype

class ClassType(Type):
    def __init__(self, classname: str):
        self.name = classname

class Symbol:
    def __init__(self, name: str, mtype: MType or Type, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
            Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
            Symbol("readBoolean", MType(list(), BooleanType()), CName(self.libName)),
            Symbol("readString", MType(list(), StringType()), CName(self.libName)),
            Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
            Symbol("printFloat", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
            Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
        ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value

class BaseVisitor(Visitor):
    pass

class CodeGenVisitor(BaseVisitor):
    
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = "MT22Class"
        self.emit = Emitter(self.path + "/MT22Class.j")

    def visitProgram(self, ast, o):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        env = SubBody(None, self.env)
        for decl in ast.decls:
            env = self.visit(decl, env)
        
        # generate default constructor
        self.genMETHOD(FuncDecl("<init>", None, list(), list(), BlockStmt([])), self.env, Frame("<init>", VoidType()))
        
        self.emit.emitEPILOG()
        return o
    
    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.return_type)
        self.genMETHOD(ast, o.sym, frame)
        
        name = ast.name
        symbol = Symbol(name, 
                        MType([x.typ for x in ast.params], ast.return_type),
                        CName(self.className))
        return SubBody(None, [symbol] + o.sym)
    
    def visitVarDecl(self, ast, o): 
        frame = o.frame
        typ = ast.typ
        name = ast.name
        
        if frame is None:
            # Global Var
            codeVar = self.emit.emitATTRIBUTE(name, typ, False, "")
            if ast.init:
                dummySubBody = SubBody(Frame(name, typ), o.sym)
                codeInit, InitTyp = self.visit(ast.init, dummySubBody)
                codeWrite = self.emit.emitPUTFIELD(name, typ, None)
            else:
                codeInit = codeWrite = ''
            
            self.emit.printout(codeInit + codeVar + codeWrite)
            return SubBody(None, [Symbol(name, typ, CName(ast.name))] + o.sym)
        else:
            # Local Var
            idx = frame.getNewIndex()
            codeVar = self.emit.emitVAR(idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame)
            
            if ast.init:
                codeInit, InitTyp = self.visit(ast.init, Access(frame, o.sym, True))
                codeWrite = self.emit.emitWRITEVAR(name, typ, idx, frame)
            else:
                codeInit = codeWrite = ''
            
            self.emit.printout(codeInit + codeVar + codeWrite)
            return SubBody(frame, [Symbol(name, typ, Index(idx))] + o.sym)
    
    def visitParamDecl(self, ast, o): pass

    def visitIntegerType(self, ast, o): pass
    def visitFloatType(self, ast, o): pass
    def visitBooleanType(self, ast, o): pass
    def visitStringType(self, ast, o): pass
    def visitArrayType(self, ast, o): pass
    def visitAutoType(self, ast, o): pass
    def visitVoidType(self, ast, o): pass

    def visitBinExpr(self, ast, o): pass
    def visitUnExpr(self, ast, o): pass
    def visitId(self, ast, o):
        # print("========================")
        # for decl in o.sym:
        #     print(decl.name + " " + str(decl.value.value))
        # print(ast.name)
        
        for decl in o.sym:
            if decl.name == ast.name:
                typ = decl.mtype
                #def __init__(self, name: str, mtype: MType, value=None):
                if type(decl.value) is Index:
                    return self.emit.emitREADVAR(decl.name, typ, decl.value.value, o.frame), typ
                if type(decl.value) is CName:
                    return self.emit.emitGETSTATIC(decl.name, decl.value.value, o.frame), typ
        
    def visitArrayCell(self, ast, o): pass
    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()
        
    def visitFloatLit(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()
        
    def visitStringLit(self, ast, o):
        return self.emit.emitPUSHCONST('"' + ast.val + '"', StringType(), o.frame), StringType()
        
    def visitBooleanLit(self, ast, o):
        val = "true" if ast.val == True else "false"
        return self.emit.emitPUSHICONST(val, o.frame), BooleanType()
    
    def visitArrayLit(self, ast, o): pass
    def visitFuncCall(self, ast, o): pass

    def visitAssignStmt(self, ast, o): 
        
        pass
    
    def visitBlockStmt(self, ast, o):
        for stmt in ast.body:
            o = self.visit(stmt, o)
        pass
    def visitIfStmt(self, ast, o): pass
    def visitForStmt(self, ast, o): pass
    def visitWhileStmt(self, ast, o): pass
    def visitDoWhileStmt(self, ast, o): pass
    def visitBreakStmt(self, ast, o): pass
    def visitContinueStmt(self, ast, o): pass
    def visitReturnStmt(self, ast, o): pass
    def visitCallStmt(self, ast, o: SubBody):
        frame = o.frame
        nenv = o.sym
        sym = next(filter(lambda x: ast.name == x.name, nenv), None)
        cname = sym.value.value
        mtype = sym.mtype
        in_ = ("", list())
        
        
        # handle io functions
        if cname == "io":
            if "read" in ast.name:
                funcName = "read"
                mtype = MType(list(), StringType())
                
                # if ast.name == "readInteger":
                #     pass
                # elif ast.name == "readFloat":
                #     str1 += self.emit.emitINVOKESTATIC("io/string_of_float", MType([typ1], StringType()), frame)
                # elif ast.name == "readBoolean":
                #     str1 += self.emit.emitINVOKESTATIC("io/string_of_bool", MType([typ1], StringType()), frame)
                
                #invokestatic io/read()Ljava/lang/String;\n
                in_ = (self.emit.emitINVOKESTATIC("io/read", MType([], StringType()), frame), [])
                
            elif "print" in ast.name:
                funcName = "print"
                str1, typ1 = self.visit(ast.args[0], Access(frame, nenv, False, True))
                mtype.partype[0] = StringType()
                
                if ast.name == "printInteger":
                    str1 += self.emit.emitINVOKESTATIC("io/string_of_int", MType([typ1], StringType()), frame)
                elif ast.name == "printFloat":
                    str1 += self.emit.emitINVOKESTATIC("io/string_of_float", MType([typ1], StringType()), frame)
                elif ast.name == "printBoolean":
                    str1 += self.emit.emitINVOKESTATIC("io/string_of_bool", MType([typ1], StringType()), frame)
                
                in_ = (str1, [typ1])
        else:
            funcName = ast.name
            for x in ast.args:
                str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
                in_ = (in_[0] + str1, in_[1].append(typ1))
        
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + funcName, mtype, frame))

    
    

    # def visitProgram(self, ast, c):
    #     [self.visit(i, c)for i in ast.decl]
    #     return c

    # def visitClassDecl(self, ast, c):
    #     self.className = ast.classname.name
    #     self.emit = Emitter(self.path+"/" + self.className + ".j")
    #     self.emit.printout(self.emit.emitPROLOG(
    #         self.className, "java.lang.Object"))
    #     [self.visit(ele, SubBody(None, self.env))
    #      for ele in ast.memlist if type(ele) == MethodDecl]
    #     # generate default constructor
    #     self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
    #     ), None, Block([], [])), c, Frame("<init>", VoidType()))
    #     self.emit.emitEPILOG()
    #     return c
    
    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.return_type is None
        isMain = consdecl.name == "main" and len(
            consdecl.params) == 0 and type(consdecl.return_type) is VoidType
        returnType = VoidType() if isInit else consdecl.return_type
        methodName = "<init>" if isInit else consdecl.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.typ, consdecl.params))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)] + env.sym), consdecl.params, SubBody(frame, []))
            glenv = local.sym + glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        # Visit Function Body
        #list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.body))
        for stmt in body.body:
            if type(stmt) is VarDecl:
                newSubBody = self.visit(stmt, SubBody(frame, glenv))
                frame = newSubBody.frame
                glenv = newSubBody.sym
            else:
                self.visit(stmt, SubBody(frame, glenv))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    # def visitFuncDecl(self, ast, o):
    #     frame = Frame(ast.name, ast.returnType)
    #     self.genMETHOD(ast, o.sym, frame)
    #     return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    # def visitCallStmt(self, ast, o):
    #     ctxt = o
    #     frame = ctxt.frame
    #     nenv = ctxt.sym
    #     sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
    #     cname = sym.value.value
    #     ctype = sym.mtype
    #     in_ = ("", list())
    #     for x in ast.param:
    #         str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
    #         in_ = (in_[0] + str1, in_[1].append(typ1))
    #     self.emit.printout(in_[0])
    #     self.emit.printout(self.emit.emitINVOKESTATIC(
    #         cname + "/" + ast.method.name, ctype, frame))

    # def visitIntLiteral(self, ast, o):
    #     return self.emit.emitPUSHICONST(ast.value, o.frame), IntegerType()

    # def visitBinaryOp(self, ast, o):
    #     e1c, e1t = self.visit(ast.left, o)
    #     e2c, e2t = self.visit(ast.right, o)
    #     return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t

