from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    search_query = ""
    error = None

    if request.method == "POST":
        search_query = request.form.get("search", "").strip()

        if search_query:
            conn = None
            try:
                # ❗ Vulnerable query (intentional for SQL Injection demo)
                query = "SELECT * FROM products WHERE name LIKE '%" + search_query + "%'"

                conn = sqlite3.connect("products.db")
                cursor = conn.cursor()

                print("User Input:", search_query)
                print("Executed Query:", query)   # 🔥 shows injection in terminal

                cursor.execute(query)
                results = cursor.fetchall()

            except Exception as e:
                error = str(e)

            finally:
                if conn:
                    conn.close()

    return render_template(
        "index.html",
        results=results,
        search_query=search_query,
        error=error
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)