from tree_sitter import Language
import os

os.environ["CC"] = "clang"
os.environ["CFLAGS"] = "-std=c11"

Language.build_library(
    # Output path for the compiled shared object file
    'build/my-languages.so',

    # List of paths to the grammar repos
    [
        'ast/grammar/tree-sitter-python',
        'ast/grammar/tree-sitter-java',
        'ast/grammar/tree-sitter-cpp',
    ]
)