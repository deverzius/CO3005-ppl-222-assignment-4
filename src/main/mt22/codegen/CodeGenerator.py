from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Visitor import Visitor


class MType:
    """This class is used for function type"""
    def __init__(self, partype: list, rettype: Type):
        self.partype = partype
        self.rettype = rettype

class ClassType(Type):
    def __init__(self, classname: str):
        self.name = classname

class Symbol:
    """This class is used for storing VarDecl and FuncDecl"""
    def __init__(self, name: str, mtype: Type or MType, value=None):
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
    """This class is used when visiting statements or functions"""
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    """This class is used when visiting expressions"""
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
            if type(decl) is VarDecl:
                env = self.visit(decl, env)
        
        # generate default constructor
        self.genMETHOD(FuncDecl("<init>", None, list(), list(), BlockStmt([])), env, Frame("<init>", VoidType()))
        self.genGlobalVarInit(env, Frame("<clinit>", VoidType()), ast.decls)
        
        
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                env = self.visit(decl, env)

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
    
    def visitVarDecl(self, ast: VarDecl, o): 
        frame = o.frame
        typ = ast.typ
        name = ast.name
        
        if frame is None:
            # Global Var
            if type(typ) is ArrayType:
                # codeSize = self.emit.emitPUSHICONST(typ.dimensions[0], frame)
                # codeNew = self.emit.emitNEWARRAY("int", frame)
                
                # codeInit = self.visit(ast.init, Access(frame, o.sym, False))
                # self.emit.printout(codeSize + codeNew + codeInit[0])
                pass
            code = self.emit.emitATTRIBUTE(name, typ, False, "")
            self.emit.printout(code)
            
            return SubBody(None, [Symbol(name, typ, CName(self.className))] + o.sym)
        else:
            # Local Var
            idx = frame.getNewIndex()
            
            if type(typ) is ArrayType:
                codeSize = self.emit.emitPUSHICONST(typ.dimensions[0], frame)
                codeNew = self.emit.emitNEWARRAY(typ.typ, frame)
                codeInit, InitTyp = self.visit(ast.init, Access(frame, o.sym, False))
                self.emit.printout(codeSize + codeNew + codeInit + self.emit.emitWRITEVAR(name, typ, idx, frame))
                
            else:
                codeVar = self.emit.emitVAR(idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame)
                
                if ast.init:
                    codeInit, InitTyp = self.visit(ast.init, Access(frame, o.sym, True))
                    codeWrite = self.emit.emitWRITEVAR(name, typ, idx, frame)
                    self.emit.printout(codeInit + codeVar + codeWrite)
                else:
                    self.emit.printout(codeVar)
                
            return SubBody(frame, [Symbol(name, typ, Index(idx))] + o.sym)
    
    def visitParamDecl(self, ast, o): pass
    def visitIntegerType(self, ast, o): pass
    def visitFloatType(self, ast, o): pass
    def visitBooleanType(self, ast, o): pass
    def visitStringType(self, ast, o): pass
    def visitArrayType(self, ast, o): pass
    def visitAutoType(self, ast, o): pass
    def visitVoidType(self, ast, o): pass

    def visitBinExpr(self, ast, o):
        frame = o.frame
        sym = o.sym
        op = ast.op
        
        lc, lt = self.visit(ast.left, Access(frame, sym, False))
        rc, rt = self.visit(ast.right, Access(frame, sym, False))
        
        if type(lt) != type(rt):
            if type(lt) is IntegerType:
                lc += self.emit.emitI2F(o.frame)
            if type(rt) is IntegerType:
                rc += self.emit.emitI2F(o.frame)
        
        typ = lt
        if op in ['+', '-']:
            code = self.emit.emitADDOP(op, lt, o.frame)
        elif op in ['*', '/']:
            code = self.emit.emitMULOP(op, lt, o.frame)
        elif op == '%':
            code = self.emit.emitMOD(o.frame)
        elif op == '&&':
            code = self.emit.emitANDOP(o.frame)
        elif op == '||':
            code = self.emit.emitOROP(o.frame)
        elif op in ['==', '!=', '<', '<=', '>', '>=']:
            code = self.emit.emitREOP(op, lt, o.frame)
            typ = BooleanType()
        elif op == '::':
            code = self.emit.emitINVOKEVIRTUAL('java/lang/String.concat', MType([StringType()], StringType()), frame)
        
        return lc + rc + code, typ
        
        
    def visitUnExpr(self, ast, o):
        code, typ = self.visit(ast.val, Access(o.frame, o.sym, False))
        if ast.op == '-':
            code += self.emit.emitNEGOP(typ, o.frame)
        elif ast.op == '!':
            code += self.emit.emitNOT(IntegerType(), o.frame)
        return code, typ
    
    def visitId(self, ast, o):
        for decl in o.sym:
            if decl.name == ast.name:
                typ = decl.mtype
                if o.isLeft == False:
                    if type(decl.value) is Index:
                        return self.emit.emitREADVAR(decl.name, typ, decl.value.value, o.frame), typ
                    if type(decl.value) is CName:
                        return self.emit.emitGETSTATIC(self.className + '.' + decl.name, typ, o.frame), typ
                else:
                    if type(decl.value) is Index:
                        return self.emit.emitWRITEVAR(decl.name, typ, decl.value.value, o.frame), typ
                    if type(decl.value) is CName:
                        return self.emit.emitPUTSTATIC(self.className + '.' + decl.name, typ, o.frame), typ
        
    def visitArrayCell(self, ast: ArrayCell, o):
        # chỉ mới đọc chưa có ghi
        frame = o.frame
        env = o.sym
        isLeft = o.isLeft

        arrCellCode, arrCellTyp = self.visit(Id(ast.name), Access(frame, env, False))
        idxCode, atomicType = self.visit(ast.cell[0], Access(frame, env, False))
        
        if isLeft == False:
            res = arrCellCode + idxCode + self.emit.emitALOAD(arrCellTyp.typ, frame)
        else:
            res = [arrCellCode + idxCode, self.emit.emitASTORE(arrCellTyp.typ, frame)]
        
        return res, atomicType
    
    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()
        
    def visitFloatLit(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()
        
    def visitStringLit(self, ast, o):
        return self.emit.emitPUSHCONST('"' + ast.val + '"', StringType(), o.frame), StringType()
        
    def visitBooleanLit(self, ast, o):
        val = "true" if ast.val == True else "false"
        return self.emit.emitPUSHICONST(val, o.frame), BooleanType()
    
    #####################
    def visitArrayLit(self, ast: ArrayLit, o):
        """vtyp: AtomicType"""
        frame = o.frame
        env = o.sym
        
        code = ""
        for idx, elemt in enumerate(ast.explist):
            code += self.emit.emitDUP(frame)
            code += self.emit.emitPUSHICONST(idx, frame)
            vcode, vtyp = self.visit(elemt, Access(frame, env, False))
            code += vcode
            code += self.emit.emitASTORE(vtyp, frame)
            
        return code, vtyp
    
    def visitFuncCall(self, ast, o):
        frame = o.frame
        nenv = o.sym
        sym = next(filter(lambda x: ast.name == x.name, nenv), None)
        cname = sym.value.value
        mtype: MType = sym.mtype
        in_ = ("", list())
        
        funcName = ast.name
        # visit params
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))

        code = in_[0]
        code += self.emit.emitINVOKESTATIC(cname + "/" + funcName, mtype, frame)
        
        return code, mtype.rettype


    def visitAssignStmt(self, ast, o):
        frame = o.frame
        sym = o.sym
        
        rhsc, rhstyp = self.visit(ast.rhs, Access(frame, sym, False))
        lhsc, lhstyp = self.visit(ast.lhs, Access(frame, sym, True))
        
        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lhsc[0] + rhsc + lhsc[1])
        else:
            self.emit.printout(rhsc + lhsc)


    def visitBlockStmt(self, ast, o):
        frame: Frame = o.frame
        env: SubBody = o
        
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        for stmt in ast.body:
            if type(stmt) is VarDecl:
                env = self.visit(stmt, env)
            else:
                self.visit(stmt, env)
                
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
    
    def visitIfStmt(self, ast: IfStmt, o):
        frame: Frame = o.frame
        
        # visit cond
        code, typ = self.visit(ast.cond, Access(frame, o.sym, False))
        self.emit.printout(code)
        
        # if false, jump
        FLABEL = frame.getNewLabel()
        code = self.emit.emitIFFALSE(FLABEL, frame)
        self.emit.printout(code)
        
        self.visit(ast.tstmt, o)
        
        if ast.fstmt is None:
            code = self.emit.emitLABEL(FLABEL, frame)
            self.emit.printout(code)
        else:
            # if true, jump to elabel
            ELABEL = frame.getNewLabel()
            code = self.emit.emitGOTO(ELABEL, frame)
            self.emit.printout(code)
            
            code = self.emit.emitLABEL(FLABEL, frame)
            self.emit.printout(code)
            
            self.visit(ast.fstmt, o)
            
            # place elabel
            code = self.emit.emitLABEL(ELABEL, frame)
            self.emit.printout(code)
        
        
    def visitForStmt(self, ast: ForStmt, o): 
        o.frame.enterLoop()
        CLABEL = o.frame.getContinueLabel()
        BLABEL = o.frame.getBreakLabel()
        
        # visit init
        astmt: AssignStmt = ast.init
        nenv: SubBody = self.visit(VarDecl(astmt.lhs.name, IntegerType(), astmt.rhs), o)
        frame: Frame = nenv.frame
        sym = nenv.sym 
        
        # CLABEL and check condition
        code = self.emit.emitLABEL(CLABEL, frame)
        ccode, ctyp = self.visit(ast.cond, Access(frame, sym, False))
        code += ccode
        
        # if false, break the loop
        code += self.emit.emitIFFALSE(BLABEL, frame)
        self.emit.printout(code)
        
        # visit stmt
        self.visit(ast.stmt, nenv)
        
        # update 
        self.visit(AssignStmt(astmt.lhs, ast.upd), nenv)
        
        # go to continue label
        code = self.emit.emitGOTO(CLABEL, frame)
        
        # place BLABEL
        code += self.emit.emitLABEL(BLABEL, frame)
        self.emit.printout(code)
        
        frame.exitLoop()
    
    
    def visitWhileStmt(self, ast: WhileStmt, o):
        frame: Frame = o.frame
        
        frame.enterLoop()
        BLABEL = frame.getBreakLabel()
        CLABEL = frame.getContinueLabel()
        
        code = self.emit.emitLABEL(CLABEL, frame)
        self.emit.printout(code)
        
        code, typ = self.visit(ast.cond, Access(frame, o.sym, False))
        self.emit.printout(code)
        
        code = self.emit.emitIFFALSE(BLABEL, frame)
        self.emit.printout(code)
        
        self.visit(ast.stmt, o)
        
        code = self.emit.emitGOTO(CLABEL, frame)
        self.emit.printout(code)
        
        code = self.emit.emitLABEL(BLABEL, frame)
        self.emit.printout(code)
        
        frame.exitLoop()
        
        
    def visitDoWhileStmt(self, ast: DoWhileStmt, o):
        frame: Frame = o.frame
        
        frame.enterLoop()
        BLABEL = frame.getBreakLabel()
        CLABEL = frame.getContinueLabel()
        TOPLABEL = frame.getNewLabel()
        
        # Place TOPLABEL
        code = self.emit.emitLABEL(TOPLABEL, frame)
        self.emit.printout(code)
        
        # Visit stmt
        self.visit(ast.stmt, o)
        
        # Place CLABEL
        code = self.emit.emitLABEL(CLABEL, frame)
        self.emit.printout(code)
        
        # Visit cond
        code, typ = self.visit(ast.cond, Access(frame, o.sym, False))
        
        # Check cond
        code += self.emit.emitIFTRUE(TOPLABEL, frame)
        
        # Go to and place break label
        code += self.emit.emitGOTO(BLABEL, frame)
        code += self.emit.emitLABEL(BLABEL, frame)
        self.emit.printout(code)
        
        frame.exitLoop()
    
    def visitBreakStmt(self, ast: BreakStmt, o):
        frame: Frame = o.frame
        code = self.emit.emitGOTO(frame.getBreakLabel(), frame)
        self.emit.printout(code)
        
    def visitContinueStmt(self, ast: ContinueStmt, o):
        frame: Frame = o.frame
        code = self.emit.emitGOTO(frame.getContinueLabel(), frame)
        self.emit.printout(code)
        
    def visitReturnStmt(self, ast, o):
        frame = o.frame
        
        if ast.expr:
            code, typ = self.visit(ast.expr, Access(frame, o.sym, False))
            
            if type(typ) is IntegerType and type(frame.returnType) is FloatType:
                code += self.emit.emitI2F(frame)
            
            self.emit.printout(code)
            
        self.emit.printout(self.emit.emitRETURN(typ, frame))
    
    def visitCallStmt(self, ast, o: SubBody):
        frame = o.frame
        nenv = o.sym
        sym = next(filter(lambda x: ast.name == x.name, nenv), None)
        cname = sym.value.value
        mtype = sym.mtype
        in_ = ("", list())
        
        # handle io functions
        if cname == "io":
            if ast.name in ['readInteger', 'readFloat', 'readBoolean', 'readString']:
                funcName = "read"
                mtype = MType(list(), StringType())
                code = self.emit.emitINVOKESTATIC("io/read", MType([], StringType()), frame)
                in_ = (code, [])
                
            elif ast.name in ['printInteger', 'printFloat', 'printBoolean', 'printString']:
                funcName = "printStrLn"
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
    
    def genGlobalVarInit(self, env, frame, decls):
        returnType = VoidType()
        methodName = "<clinit>"
        intype = []
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, True, frame))
        
        frame.enterScope(True)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        for decl in decls:
            if type(decl) is VarDecl and decl.init:
                if type(decl.typ) is ArrayType:
                    typ = decl.typ
                    codeSize = self.emit.emitPUSHICONST(typ.dimensions[0], frame)
                    codeNew = self.emit.emitNEWARRAY(typ.typ, frame)
                    codeInit, initTyp = self.visit(decl.init, Access(frame, env, False))
                    self.emit.printout(
                        codeSize + 
                        codeNew + 
                        codeInit + 
                        self.emit.emitPUTSTATIC("MT22Class." + decl.name, typ, frame))
                    continue
                
                dummySubBody = SubBody(frame, env)
                codeInit, initTyp = self.visit(decl.init, dummySubBody)
                codeWrite = self.emit.emitPUTSTATIC("MT22Class." + decl.name, initTyp, frame)
                self.emit.printout(codeInit + codeWrite)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()