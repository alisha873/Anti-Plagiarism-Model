import json
from utils.embed import embed_code
from utils.similarity import cosine_similarity
from user_submissions.sub1 import user_embedding
from utils.ast_parser import ast_token
from ast_tfidf import ast_tfidf_similarity  

with open("ai_solutions/q1.json", "r") as f:
    ai_solutions = json.load(f)

ai_embeddings = [embed_code(entry["code"]) for entry in ai_solutions]

ai_ast_tokens_list = [ast_token(entry["code"], entry["language"]) for entry in ai_solutions]

user_code = input("Input the code:\n")
user_language = input("Language (python/java/cpp): ").strip().lower()

user_vec = embed_code(user_code)
user_ast_tokens = ast_token(user_code, user_language)

graphcodebert_scores = [cosine_similarity(user_vec, ai_vec) for ai_vec in ai_embeddings]
avg_graph_score = sum(graphcodebert_scores) / len(graphcodebert_scores)

avg_ast_score, ast_scores = ast_tfidf_similarity(ai_ast_tokens_list, user_ast_tokens)

final_similarity = (avg_graph_score + avg_ast_score) / 2

threshold = 0.90
print(f"\nGraphCodeBERT Avg Similarity: {avg_graph_score}")
print(f"AST-TFIDF Avg Similarity: {avg_ast_score}")
print(f"Final Combined Similarity: {final_similarity}")

if final_similarity >= threshold:
    print("Potential AI-generated code detected!")
else:
    print("Code appears original.")
