from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine

def cosine_similarity(vec1,vec2):
    return sklearn_cosine([vec1],[vec2])[0][0] #getting row 0, col 0 out of 2d matrix that cosine_similarity return