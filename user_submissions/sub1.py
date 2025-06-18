from utils.embed import embed_code

def user_embedding():
    user_code=input("Input the code:\n")
    return embed_code(user_code)