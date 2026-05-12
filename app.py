from flask import Flask, render_template, request
import sqlite3
import os

# ✅ Ensure database is created automatically
if not os.path.exists("products.db"):
    import init_db

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    results = []
    search_query = ""
    error = None
    mode = "vulnerable"

    if request.method == "POST":

        # 🔍 Get form values
        search_query = request.form.get("search", "").strip()
        mode = request.form.get("mode", "vulnerable")

        if search_query:

            conn = None

            try:
                # ✅ Connect to database
                conn = sqlite3.connect("products.db")
                cursor = conn.cursor()

                # 🔴 Vulnerable Mode
                if mode == "vulnerable":

                    query = (
                        "SELECT * FROM products WHERE name LIKE '%"
                        + search_query +
                        "%'"
                    )

                    print("\n🔴 Vulnerable Mode")
                    print("User Input:", search_query)
                    print("Executed Query:", query)

                    cursor.execute(query)

                # 🟢 Secure Mode
                else:

                    query = "SELECT * FROM products WHERE name LIKE ?"

                    safe_value = "%" + search_query + "%"

                    print("\n🟢 Secure Mode")
                    print("User Input:", search_query)
                    print("Executed Query:", query)
                    print("Parameter:", safe_value)

                    cursor.execute(query, (safe_value,))

                # ✅ Fetch results
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
        error=error,
        mode=mode
    )

if __name__ == "__main__":

    # ☁️ Required for Render deployment
    port = int(os.environ.get("PORT", 8000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )