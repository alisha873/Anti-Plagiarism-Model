import json
from utils.embed import embed_code
from utils.ast_parser import ast_token 
import psycopg2
from datetime import datetime

conn=psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="beaUxH%6ve_eM7R",
    host="db.jplzoeijacrqgzumqyts.supabase.co",
    port="5432"
)

cursor=conn.cursor()

with open("q1_ai_solutions.json", "r") as f:
    ai_solutions = json.load(f)

ai_embeddings = [embed_code(entry["code"]) for entry in ai_solutions]

ai_ast_tokens_list = [ast_token(entry["code"], entry["language"]) for entry in ai_solutions]

for i,entry in enumerate(ai_solutions):
    print("working")
    ai_id = entry["id"]
    question_id = entry["question_id"]
    language = entry["language"]
    code = entry["code"]
    embedding = ai_embeddings[i].tolist()  
    ast_tokens = ai_ast_tokens_list[i]
    
    cursor.execute("""
            INSERT INTO ai_solutions (id, question_id, language, code, embedding, ast_tokens)
            VALUES (%s, %s, %s, %s, %s, %s)""", 
            (
            ai_id,
            question_id,
            language,
            code,
            embedding,
            ast_tokens,
            ))

conn.commit()
cursor.close()
conn.close()

print("done.")