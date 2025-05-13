from pycparser import c_parser, c_ast

class CCodeVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.pseudo = []
        self.indent_level = 0

    def indent(self):
        return "    " * self.indent_level

    def visit_FuncDef(self, node):
        name = node.decl.name
        args = []
        if isinstance(node.decl.type.args, c_ast.ParamList):
            for param in node.decl.type.args.params:
                if isinstance(param, c_ast.Decl):
                    args.append(param.name)
        self.pseudo.append(f"{self.indent()}Define function {name}({', '.join(args)})")
        self.indent_level += 1
        self.visit(node.body)
        self.indent_level -= 1

    def visit_Compound(self, node):
        for stmt in node.block_items or []:
            self.visit(stmt)

    def visit_Decl(self, node):
        if isinstance(node.type, c_ast.TypeDecl):
            if node.init:
                self.pseudo.append(f"{self.indent()}Declare {node.name} ← {self._expr(node.init)}")
            else:
                self.pseudo.append(f"{self.indent()}Declare {node.name}")
        self.generic_visit(node)

    def visit_Assignment(self, node):
        lval = self._expr(node.lvalue)
        rval = self._expr(node.rvalue)
        self.pseudo.append(f"{self.indent()}{lval} ← {rval}")

    def visit_If(self, node):
        cond = self._expr(node.cond)
        self.pseudo.append(f"{self.indent()}If ({cond}) then")
        self.indent_level += 1
        self.visit(node.iftrue)
        self.indent_level -= 1
        if node.iffalse:
            self.pseudo.append(f"{self.indent()}Else")
            self.indent_level += 1
            self.visit(node.iffalse)
            self.indent_level -= 1

    def visit_For(self, node):
        init = self._expr(node.init)
        cond = self._expr(node.cond)
        next_ = self._expr(node.next)
        self.pseudo.append(f"{self.indent()}For ({init}; {cond}; {next_}) do")
        self.indent_level += 1
        self.visit(node.stmt)
        self.indent_level -= 1

    def visit_While(self, node):
        cond = self._expr(node.cond)
        self.pseudo.append(f"{self.indent()}While ({cond}) do")
        self.indent_level += 1
        self.visit(node.stmt)
        self.indent_level -= 1

    def visit_Return(self, node):
        expr = self._expr(node.expr) if node.expr else ""
        self.pseudo.append(f"{self.indent()}Return {expr}")

    def _expr(self, node):
        if node is None:
            return ""
        try:
            from pycparser.c_generator import CGenerator
            return CGenerator().visit(node)
        except Exception:
            return str(node)

def convert_c_to_pseudocode(code: str) -> str:
    try:
        parser = c_parser.CParser()
        ast_tree = parser.parse(code)
        visitor = CCodeVisitor()
        visitor.visit(ast_tree)
        return "\n".join(visitor.pseudo)
    except Exception as e:
        return f"Error parsing C code: {str(e)}"
