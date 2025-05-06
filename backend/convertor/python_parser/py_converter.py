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
        args = ", ".join(arg.arg for arg in node.args.args)
        self.pseudo.append(f"{self.indent()}Function {node.name}({args})")
        self.indent_level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.indent_level -= 1

    def visit_Assign(self, node):
        targets = [self.visit(t) for t in node.targets]
        value = self.visit(node.value)
        self.pseudo.append(f"{self.indent()}{' = '.join(targets)} = {value}")

    def visit_Name(self, node):
        return node.id

    def visit_Constant(self, node):
        return repr(node.value)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = self.visit(node.op)
        return f"({left} {op} {right})"

    def visit_Add(self, node):
        return "+"

    def visit_Sub(self, node):
        return "-"

    def visit_Mult(self, node):
        return "*"

    def visit_Div(self, node):
        return "/"

    def visit_If(self, node):
        test = self.visit(node.test)
        self.pseudo.append(f"{self.indent()}IF {test}")
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

    def visit_Compare(self, node):
        left = self.visit(node.left)
        ops = " ".join(self.visit(op) for op in node.ops)
        right = " ".join(self.visit(comp) for comp in node.comparators)
        return f"{left} {ops} {right}"

    def visit_Eq(self, node): return "=="
    def visit_NotEq(self, node): return "!="
    def visit_Lt(self, node): return "<"
    def visit_LtE(self, node): return "<="
    def visit_Gt(self, node): return ">"
    def visit_GtE(self, node): return ">="

    def visit_While(self, node):
        test = self.visit(node.test)
        self.pseudo.append(f"{self.indent()}WHILE {test}")
        self.indent_level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.indent_level -= 1

    def visit_For(self, node):
        target = self.visit(node.target)
        iter_ = self.visit(node.iter)
        self.pseudo.append(f"{self.indent()}FOR {target} in {iter_}")
        self.indent_level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.indent_level -= 1

    def visit_Call(self, node):
        func = self.visit(node.func)
        args = ", ".join(self.visit(arg) for arg in node.args)
        if func == 'print':
            return f"PRINT {args}"
        elif func == 'input':
            return f"INPUT({args})"
        return f"{func}({args})"

    def visit_Return(self, node):
        value = self.visit(node.value)
        self.pseudo.append(f"{self.indent()}RETURN {value}")

    def generic_visit(self, node):
        return f"<{type(node).__name__}>"

def convert_python_to_pseudo(code: str) -> str:
    try:
        tree = ast.parse(code)
        generator = PseudoCodeGenerator()
        generator.visit(tree)
        return "\n".join(generator.pseudo) if generator.pseudo else "No pseudo-code generated."
    except Exception as e:
        return f"Error: {str(e)}"
