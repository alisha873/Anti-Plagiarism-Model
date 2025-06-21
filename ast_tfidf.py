from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def ast_tfidf_similarity(ai_ast_tokens_list, user_ast_tokens):
    corpus = [' '.join(tokens) for tokens in ai_ast_tokens_list] + [' '.join(user_ast_tokens)]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    scores = similarities.flatten().tolist()
    avg_score = sum(scores) / len(scores)

    return avg_score
