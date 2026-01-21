from flask import Flask
import subprocess

def get_git_output(args, default="N/A"):
    try:
        return subprocess.check_output(args, stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return default

app = Flask(__name__)

@app.route("/")
def index():
    commit_id = get_git_output(["git", "rev-parse", "HEAD"])
    commit_message = get_git_output(["git", "log", "-1", "--pretty=%B"])

    return f"""
    <h1>Hello World</h1>
    <p><strong>Latest Git Commit ID:</strong> {commit_id}</p>
    <p><strong>Latest Git Commit Message:</strong></p>
    <pre>{commit_message}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

