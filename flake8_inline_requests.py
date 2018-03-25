import ast

__version__ = '0.0.1'


class InlineRequestsFinder(ast.NodeVisitor):
    MSG = 'SIR001 Missing handle_httpstatus_all in inline requests'

    def __init__(self, *args, **kwargs):
        super(InlineRequestsFinder, self).__init__(*args, **kwargs)
        self.issues = {}

    def get_meta_kw_arg(self, call):
        for kw in call.keywords:
            if kw.arg == 'meta' and isinstance(kw.value, ast.Dict):
                return kw

    def has_handle_httpstatus_all_true(self, meta_arg):
        for key, value in zip(meta_arg.value.keys, meta_arg.value.values):
            if key.s == 'handle_httpstatus_all' and ast.literal_eval(value):
                return True
        return False

    def visit_Assign(self, node):
        if not isinstance(node.value, ast.Yield):
            return

        yield_expr = node.value
        if not isinstance(yield_expr.value, ast.Call):
            return

        call = yield_expr.value
        if 'Request' not in call.func.id:
            return

        meta_arg = self.get_meta_kw_arg(call)
        if not meta_arg or not self.has_handle_httpstatus_all_true(meta_arg):
            self.issues[(call.lineno, call.col_offset)] = self.MSG


class InlineRequestsChecker(object):
    options = None
    name = 'flake8-inline-requests'
    version = __version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        parser = InlineRequestsFinder()
        parser.visit(self.tree)

        for (lineno, col), message in parser.issues.items():
            yield (lineno, col, message, InlineRequestsChecker)
