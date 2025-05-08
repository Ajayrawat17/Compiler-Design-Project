import ast

class PseudoCodeGenerator(ast.NodeVisitor):
    def __init__(self):
        self.pseudo = []
        self.indent_level = 0

    def indent(self):
        return "    " * self.indent_level

    def visit_Module(self, node):
        for stmt in node.body:
            self.visit(stmt)

    def visit_FunctionDef(self, node):
        args = [arg.arg for arg in node.args.args]
        self.pseudo.append(f"{self.indent()}FUNCTION {node.name}({', '.join(args)})")
        self.indent_level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.indent_level -= 1
        self.pseudo.append(f"{self.indent()}END FUNCTION\n")

    def visit_Return(self, node):
        value = self.visit(node.value)
        self.pseudo.append(f"{self.indent()}RETURN {value}")

    def visit_Assign(self, node):
        target = self.visit(node.targets[0])
        value = self.visit(node.value)
        self.pseudo.append(f"{self.indent()}{target} ← {value}")

    def visit_Expr(self, node):
        value = self.visit(node.value)
        self.pseudo.append(f"{self.indent()}{value}")

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            args = [self.visit(arg) for arg in node.args]
            if func_name == "print":
                return f"PRINT {', '.join(args)}"
            return f"{func_name}({', '.join(args)})"
        return "CALL"

    def visit_If(self, node):
        condition = self.visit(node.test)
        self.pseudo.append(f"{self.indent()}IF {condition} THEN")
        self.indent_level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.indent_level -= 1
        if node.orelse:
            self.pseudo.append(f"{self.indent()}ELSE")
            self.indent_level += 1
            for stmt in node.orelse:
                self.visit(stmt)
            self.indent_level -= 1
        self.pseudo.append(f"{self.indent()}END IF")

    def visit_For(self, node):
        target = self.visit(node.target)
        iter_ = self.visit(node.iter)
        self.pseudo.append(f"{self.indent()}FOR {target} IN {iter_}")
        self.indent_level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.indent_level -= 1
        self.pseudo.append(f"{self.indent()}END FOR")

    def visit_Compare(self, node):
        left = self.visit(node.left)
        op = self.visit(node.ops[0])
        right = self.visit(node.comparators[0])
        return f"{left} {op} {right}"

    def visit_BinOp(self, node):
        return f"{self.visit(node.left)} {self.visit(node.op)} {self.visit(node.right)}"

    def visit_Add(self, node): return "+"
    def visit_Sub(self, node): return "-"
    def visit_Mult(self, node): return "*"
    def visit_Div(self, node): return "/"
    def visit_Lt(self, node): return "<"
    def visit_Gt(self, node): return ">"
    def visit_LtE(self, node): return "<="
    def visit_GtE(self, node): return ">="
    def visit_Eq(self, node): return "=="
    def visit_NotEq(self, node): return "!="

    def visit_Name(self, node): return node.id
    def visit_Constant(self, node): return repr(node.value)

def convert_to_pseudocode(code: str) -> str:
    tree = ast.parse(code)
    generator = PseudoCodeGenerator()
    generator.visit(tree)
    return "\n".join(generator.pseudo)
