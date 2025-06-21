
🛡️ AI-Based Code Plagiarism Detection
====================================

A multi-stage AI-powered system to detect code plagiarism across Python, Java, and C++. Built to support competitive coding platforms, this project combines structural, semantic, and behavioral analysis for high accuracy.

🚀 Features
-----------

- 🔍 AST-Based Structural Similarity  
  Uses Tree-sitter to extract AST tokens and compute TF-IDF-based similarity.

- 🧠 GraphCodeBERT Semantic Embeddings  
  Leverages Microsoft's GraphCodeBERT to compare the semantic meaning of code via cosine similarity.

- 📦 Custom AI Solution Database  
  AI-generated solutions (3–5 per language) stored in PostgreSQL along with precomputed AST tokens and embeddings.

- ⚙️ Multi-Language Support  
  Compatible with Python, Java, and C++.

- 📉 Plagiarism Thresholding  
  Separate thresholds for AST (structural) and BERT (semantic) similarity allow fine-tuned decision making.

🛠️ Technologies Used
---------------------

- Python 3.12
- PostgreSQL (Supabase hosted)
- Tree-sitter (for AST generation)
- GraphCodeBERT via Hugging Face
- Scikit-learn (TF-IDF, cosine similarity)
- psycopg2 (PostgreSQL client)

🧪 How it Works
----------------

1. User submits code via CLI (`testinput.py`)
2. AST tokens are extracted and compared using TF-IDF cosine similarity
3. If similarity exceeds threshold, semantic comparison is done using GraphCodeBERT embeddings
4. Final decision: "Not Plagiarised" or "Potential Plagiarism Flagged"

📥 Setup Instructions
----------------------

1. Clone the repo  
   `git clone https://github.com/your-username/your-repo.git && cd anticheat-model`

2. Install requirements  
   `pip install -r requirements.txt`

3. Build Tree-sitter languages  
   `cd ast/ && bash build.sh`

4. Run  
   `python testinput.py`  
   `python check.py`
