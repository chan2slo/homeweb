from flask import Flask, request, session, redirect, url_for, render_template, flash
from wakeonlan import send_magic_packet
import os

USERNAME = os.environ.get("HOMEWEB_USER", "default_user")
PASSWORD = os.environ.get("HOMEWEB_PW", "default_pw")
app = Flask(__name__)
app.secret_key = os.environ.get("HOMEWEB_KEY", "default_key")

USERNAME = os.environ.get("HOMEWEB_USER", "default_user")
PASSWORD = os.environ.get("HOMEWEB_PW", "default_pw")
TARGET_MAC = "9C:6B:00:9C:27:71"
BROADCAST_IP = "10.0.0.255"

@app.route("/", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):   # 이미 로그인한 경우
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            flash("❌ 로그인 실패!", "error")   # 🔹 flash 메시지 추가
            return redirect(url_for("login"))  # 다시 로그인 페이지로
    return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    # 세션 초기화
    session.clear()
    # 메시지 띄우기
    flash("로그아웃 되었습니다.", "success")
    # 로그인 페이지로 리다이렉트
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/wake", methods=["POST"])
def wake():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    send_magic_packet(TARGET_MAC, ip_address=BROADCAST_IP, port=9)
    flash("✅ 매직패킷 전송 완료!", "success")
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5080)