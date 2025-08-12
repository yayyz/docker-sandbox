from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def home():
    return """
    <h2>Hello from Flask + Redis!</h2>
    <p>Redis에 키=값을 다음과 같은 방법으로 저장해주세요: <code>/set?key=foo&value=bar</code></p>
    <p>조회는 이렇게!: <code>/get?key=foo</code></p>
    """

@app.route("/set")
def set_key():
    key = request.args.get("key")
    value = request.args.get("value")
    if not key or not value:
        return "'key','value'  파라미터를 입력해주세요.", 400
    r.set(key, value)
    return f"Key '{key}' set to '{value}'"

@app.route("/get")
def get_key():
    key = request.args.get("key")
    if not key:
        return "'key' 파라미터를 입력해주세요.", 400
    value = r.get(key)
    if value is None:
        return f"Key '{key}' not found", 404
    return f"Key '{key}' has value '{value}'"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
