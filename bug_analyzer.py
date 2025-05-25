import ast
#AST = Abstract Syntax Tree
#It is a tree representation of the source code structure.
#Every language has its own grammar and thus its own AST format.
import builtins

class BugAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.defined_vars = set()
        self.used_vars = []
        self.bugs = []
        self.current_func_args = set()
        self.current_func_returns = False
        self.builtins = set(dir(builtins))
        self.defined_funcs = set()

    def visit_FunctionDef(self, node):
        self.defined_funcs.add(node.name)
        self.current_func_args = {arg.arg for arg in node.args.args}
        self.defined_vars.update(self.current_func_args)
        self.current_func_returns = False

        self.generic_visit(node)

        if not self.current_func_returns:
            self.bugs.append({
                "line": node.lineno,
                "issue": f"Function '{node.name}' may be missing a return statement.",
                "variable": node.name,
                "fix": "Ensure the function returns a value if needed.",
                "confidence": 0.9
            })

        unused_args = self.current_func_args - set(self.used_vars)
        for arg in unused_args:
            self.bugs.append({
                "line": node.lineno,
                "issue": f"Function argument '{arg}' is not used.",
                "variable": arg,
                "fix": f"Remove unused parameter '{arg}' if unnecessary.",
                "confidence": 0.85
            })

        self.current_func_args = set()
        self.used_vars = []

    def visit_Return(self, node):
        self.current_func_returns = True
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.defined_vars.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used_vars.append(node.id)
            if (
                node.id not in self.defined_vars
                and node.id not in self.current_func_args
                and node.id not in self.builtins
                and node.id not in self.defined_funcs
            ):
                self.bugs.append({
                    "line": node.lineno,
                    "issue": f"Variable '{node.id}' used before assignment.",
                    "variable": node.id,
                    "fix": f"Assign a value to '{node.id}' before using it.",
                    "confidence": 0.95
                })
        elif isinstance(node.ctx, ast.Store):
            self.defined_vars.add(node.id)

        self.generic_visit(node)

def analyze_code(code_text, file_name="example.py"):
    try:
        tree = ast.parse(code_text)
    except SyntaxError as e:
        return [{
            "file": file_name,
            "line": e.lineno,
            "issue": f"Syntax error: {e.msg}",
            "variable": "unknown",
            "fix": "Fix syntax error to proceed.",
            "confidence": 1.0
        }]

    analyzer = BugAnalyzer()
    analyzer.visit(tree)

    for bug in analyzer.bugs:
        bug["file"] = file_name

    return analyzer.bugs
