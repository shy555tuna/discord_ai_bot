from flask import Flask, render_template, request, jsonify, Response
import threading
import subprocess
import os
import sys
import json
import queue
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

config = {
    "discord_token": "",
    "gemini_api_key": "",
    "ai_name": "Assistant",
    "system_instruction": ""
}

bot_process = None
bot_thread = None
bot_status = "stopped"
bot_logs = []
log_queue = queue.Queue()

def add_log(message, level="info"):
    entry = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "message": message,
        "level": level
    }
    bot_logs.append(entry)
    if len(bot_logs) > 200:
        bot_logs.pop(0)
    log_queue.put(entry)

def run_bot():
    global bot_process, bot_status

    env = os.environ.copy()
    env["DISCORD_BOT_TOKEN"] = config["discord_token"]
    env["GEMINI_API_KEY"] = config["gemini_api_key"]
    env["BOT_AI_NAME"] = config["ai_name"]
    env["BOT_SYSTEM_INSTRUCTION"] = config["system_instruction"]

    try:
        import certifi
        env["SSL_CERT_FILE"] = certifi.where()
        env["REQUESTS_CA_BUNDLE"] = certifi.where()
    except ImportError:
        pass

    bot_script = os.path.join(BASE_DIR, "bot.py")

    try:
        bot_status = "starting"
        add_log("Starting bot process...", "info")

        bot_process = subprocess.Popen(
            [sys.executable, bot_script],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            cwd=BASE_DIR
        )

        bot_status = "running"
        add_log(f"Bot process started (PID {bot_process.pid})", "success")

        for line in bot_process.stdout:
            line = line.rstrip()
            if line:
                level = "error" if "error" in line.lower() or "exception" in line.lower() or "traceback" in line.lower() else \
                        "success" if "logged on" in line.lower() or "ready" in line.lower() else "info"
                add_log(line, level)

        bot_process.wait()
        if bot_process.returncode != 0 and bot_status != "stopped":
            bot_status = "error"
            add_log(f"Bot exited with code {bot_process.returncode}", "error")
        else:
            bot_status = "stopped"
            add_log("Bot stopped.", "info")

    except Exception as e:
        bot_status = "error"
        add_log(f"Failed to start bot: {str(e)}", "error")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/config", methods=["GET"])
def get_config():
    return jsonify({
        "ai_name": config["ai_name"],
        "system_instruction": config["system_instruction"],
        "has_discord_token": bool(config["discord_token"]),
        "has_gemini_key": bool(config["gemini_api_key"]),
        "discord_token_preview": f"•••••{config['discord_token'][-4:]}" if config["discord_token"] else "",
        "gemini_key_preview": f"•••••{config['gemini_api_key'][-4:]}" if config["gemini_api_key"] else "",
    })

@app.route("/api/config", methods=["POST"])
def update_config():
    data = request.json
    if "discord_token" in data and data["discord_token"] and not data["discord_token"].startswith("•"):
        config["discord_token"] = data["discord_token"]
    if "gemini_api_key" in data and data["gemini_api_key"] and not data["gemini_api_key"].startswith("•"):
        config["gemini_api_key"] = data["gemini_api_key"]
    if "ai_name" in data:
        config["ai_name"] = data["ai_name"]
    if "system_instruction" in data:
        config["system_instruction"] = data["system_instruction"]
    return jsonify({"success": True})

@app.route("/api/status")
def get_status():
    return jsonify({
        "status": bot_status,
        "pid": bot_process.pid if bot_process and bot_process.poll() is None else None
    })

@app.route("/api/bot/start", methods=["POST"])
def start_bot():
    global bot_thread, bot_status

    if bot_status in ("running", "starting"):
        return jsonify({"success": False, "error": "Bot is already running"})
    if not config["discord_token"]:
        return jsonify({"success": False, "error": "Discord bot token is required"})
    if not config["gemini_api_key"]:
        return jsonify({"success": False, "error": "Gemini API key is required"})

    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    return jsonify({"success": True})

@app.route("/api/bot/stop", methods=["POST"])
def stop_bot():
    global bot_process, bot_status

    if bot_process and bot_process.poll() is None:
        bot_status = "stopped"
        bot_process.terminate()
        try:
            bot_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            bot_process.kill()
        add_log("Bot stopped by user.", "info")
        return jsonify({"success": True})

    bot_status = "stopped"
    return jsonify({"success": False, "error": "Bot is not running"})

@app.route("/api/logs")
def get_logs():
    return jsonify(bot_logs[-100:])

@app.route("/api/logs/stream")
def stream_logs():
    def generate():
        for entry in bot_logs[-50:]:
            yield f"data: {json.dumps(entry)}\n\n"
        while True:
            try:
                entry = log_queue.get(timeout=1)
                yield f"data: {json.dumps(entry)}\n\n"
            except queue.Empty:
                yield f"data: {json.dumps({'ping': True})}\n\n"

    return Response(generate(), mimetype="text/event-stream",
                    headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})

if __name__ == "__main__":
    print("🤖 ShyNet running at http://localhost:5000")
    app.run(debug=False, host="127.0.0.1", port=5000, threaded=True)
