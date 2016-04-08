from __future__ import absolute_import, print_function, unicode_literals

import ast
import re


__version__ = '0.1'


CODE = 'F481'


class CheckFutures(object):
    name = 'future'
    version = __version__

    default_expected_imports = set([
        'absolute_import',
        'print_function',
        'unicode_literals',
    ])

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    @classmethod
    def add_options(cls, parser):
        parser.add_option('--future-imports', action='store',
                          default=','.join(cls.default_expected_imports),
                          help='Comma-separated list of expected future '
                               'imports')
        parser.config_options.append('future-imports')

    @classmethod
    def parse_options(cls, options):
        if options.future_imports:
            cls.expected_imports = set(
                re.split('\s*,\s*', options.future_imports.strip()))
        else:
            cls.expected_imports = set()

    def run(self):
        imports = set()
        node = None
        for node in ast.walk(self.tree):
            if (isinstance(node, ast.ImportFrom) and
                    node.module == '__future__'):
                imports |= set(name.name for name in node.names)
            elif isinstance(node, ast.Expr):
                if not isinstance(node.value, ast.Str):
                    break
            elif not isinstance(node, ast.Module):
                break

        if isinstance(node, ast.Module):
            return

        if not (imports >= self.expected_imports):
            if imports:
                message = ('{code}: Expected these __future__ imports: '
                           '{0}; but only got: {1}'
                           .format(', '.join(self.expected_imports),
                                   ', '.join(imports),
                                   code=CODE))
            else:
                message = ('{code}: Expected these __future__ imports, '
                           'but got none: {0}'
                           .format(', '.join(self.expected_imports),
                                   code=CODE))

            yield node.lineno, node.col_offset, message, CheckFutures
