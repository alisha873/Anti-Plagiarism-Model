import psycopg2
import random
import json

def get_random_question():
    allowed_qids = ['LC-1', 'LC-2', 'LC-3']

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="beaUxH%6ve_eM7R",
        host="db.jplzoeijacrqgzumqyts.supabase.co",
        port="5432"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT qid, title FROM questions WHERE qid = ANY(%s)", ([*allowed_qids],))
    questions = cursor.fetchall()

    cursor.close()
    conn.close()

    if not questions:
        raise ValueError("❌ No questions found for LC-1, LC-2, LC-3. Check your DB content.")

    return random.choice(questions)

def collect_user_input():
    qid, title = get_random_question()
    print(f"\n🧠 Your randomly selected question is: {qid} - {title}")

    language = input("💬 Enter language (python/java/cpp): ").strip().lower()

    print("🧑‍💻 Write your solution below (end input with a blank line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    user_code = "\n".join(lines)

    ext_map = {"python": "py", "cpp": "cpp", "java": "java"}
    ext = ext_map.get(language, "txt")  # fallback
    filename = f"user_code.{ext}"

    with open(filename, "w") as f:
       f.write(user_code)

    # Save metadata
    with open("session_meta.json", "w") as f:
        json.dump({"qid": qid, "language": language, "filename": filename}, f)


if __name__ == "__main__":
    collect_user_input()
