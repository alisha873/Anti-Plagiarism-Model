from utils.similarity import cosine_similarity
from utils.embed import embed_code
from utils.ast_parser import ast_token
from ast_tfidf import ast_tfidf_similarity
import psycopg2
import numpy as np 
import json
import ast

with open("session_meta.json", "r") as f:
    meta = json.load(f)

qid = meta["qid"]
language = meta["language"]
filename = meta["filename"]

#user code obtained
with open(filename, "r") as f:
    user_code = f.read()

#creating database connection
conn=psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="beaUxH%6ve_eM7R",
    host="db.jplzoeijacrqgzumqyts.supabase.co",
    port="5432"
)
cursor=conn.cursor()

#stage 1- producing ast tokens and applying tf-idf on them

user_ast_tokens = ast_token(user_code,language)
print(f"Extracted {len(user_ast_tokens)} AST tokens from user code.")

#runs an sql query
cursor.execute("""SELECT ast_tokens FROM ai_solutions              
    WHERE question_id = %s AND language = %s""",(qid,language))

#fetch allrows
rows=cursor.fetchall()
ai_ast_tokens_list = []
for row in rows:
    tokens = row[0]
    if isinstance(tokens, str):
        tokens = json.loads(tokens)
    ai_ast_tokens_list.append(tokens)

avg_score=ast_tfidf_similarity(ai_ast_tokens_list,user_ast_tokens)

threshold_1=0.85
if(avg_score<=threshold_1):
    print("not plagirised.")
else:
    #stage 2- producing embedding and applying cosine sim
    user_embeddings=embed_code(user_code)

    cursor.execute("""
    SELECT embedding FROM ai_solutions
    WHERE question_id = %s AND language = %s""",(qid, language))

    rows = cursor.fetchall()
    ai_embeddings = [np.array(ast.literal_eval(row[0])) for row in rows]

    similarities = [cosine_similarity(user_embeddings, ai_emb) for ai_emb in ai_embeddings]
    avg_cosine_sim = sum(similarities) / len(similarities)

    threshold_2 = 0.90
    if avg_cosine_sim > threshold_2:
        print("Potential plagiarism flagged!")
    else:
        print("Not plagiarised.")


cursor.close()
conn.close()