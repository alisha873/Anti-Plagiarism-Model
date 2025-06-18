from tree_sitter import Language,Parser

LIB_PATH = "ast/build/my-languages.so"
SUPPORTED_LANGUAGES = {
    "python": "python",
    "cpp": "cpp",
    "java": "java"
}

def ast_token(code,language):
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Language '{language}' not supported.")
    
    lang = Language(LIB_PATH, SUPPORTED_LANGUAGES[language]) #loads specific library grammar
    parser=Parser()
    parser.set_language(lang)  #parser initialised and language set
    tree=parser.parse(bytes(code,"utf8")) #parses into ast, tree sitter expects input in utf-8 encoded bytes, so string is converted into byte object
    root_node=tree.root_node 
    tokens =[]

    def walk(node):  #list of each type of node
        tokens.append(node.type)
        for child in node.children:
            walk(child)  #for each child, it's type is appended and it's child is called again till leaf node is reached, ensures full tree exploration

    walk(root_node)
    return tokens


