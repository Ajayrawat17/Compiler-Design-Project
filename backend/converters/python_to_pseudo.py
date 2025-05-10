import ast

class PseudoCodeGenerator(ast.NodeVisitor):
    def __init__(self):
        self.pseudo = []
        self.indent_level = 0

    def indent(self):
        return "    " * self.indent_level

    def visit_FunctionDef(self, node):
        args = ", ".join([arg.arg for arg in node.args.args])
        self.pseudo.append(f"{self.indent()}Define function {node.name}({args})")
        self.indent_level += 1
        self.generic_visit(node)
        self.indent_level -= 1

    def visit_Assign(self, node):
        targets = [ast.unparse(t) for t in node.targets]
        value = ast.unparse(node.value)
        self.pseudo.append(f"{self.indent()}{' = '.join(targets)} ← {value}")
        self.generic_visit(node)

    def visit_If(self, node):
        test = ast.unparse(node.test)
        self.pseudo.append(f"{self.indent()}If ({test}) then")
        self.indent_level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.indent_level -= 1
        if node.orelse:
            self.pseudo.append(f"{self.indent()}Else")
            self.indent_level += 1
            for stmt in node.orelse:
                self.visit(stmt)
            self.indent_level -= 1

    def visit_For(self, node):
        target = ast.unparse(node.target)
        iter_ = ast.unparse(node.iter)
        self.pseudo.append(f"{self.indent()}For {target} in {iter_}:")
        self.indent_level += 1
        self.generic_visit(node)
        self.indent_level -= 1

    def visit_While(self, node):
        test = ast.unparse(node.test)
        self.pseudo.append(f"{self.indent()}While ({test}) do")
        self.indent_level += 1
        self.generic_visit(node)
        self.indent_level -= 1

    def visit_Return(self, node):
        value = ast.unparse(node.value) if node.value else ""
        self.pseudo.append(f"{self.indent()}Return {value}")

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Call):
            self.visit_Call(node.value)

    def visit_Call(self, node):
        func = ast.unparse(node.func)
        args = ", ".join([ast.unparse(arg) for arg in node.args])
        if func == "print":
            self.pseudo.append(f"{self.indent()}Display({args})")
        elif func == "input":
            self.pseudo.append(f"{self.indent()}Get input")
        else:
            self.pseudo.append(f"{self.indent()}Call {func}({args})")

def convert_python_to_pseudocode(code: str) -> str:
    try:
        tree = ast.parse(code)
        generator = PseudoCodeGenerator()
        generator.visit(tree)
        return "\n".join(generator.pseudo)
    except Exception as e:
        return f"Error parsing Python code: {str(e)}"
