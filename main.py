import requests
import uuid
from flask import Flask,request
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

proxy = {
    "http":"http://username:password@ip:port", #هنا هتحط البروكسي بتاعك
    "https":"http://username:password@ip:port" #هنا هتحط البروكسي بتاعك
}

app = Flask(__name__)

@app.route("/send_vote",methods=['GET'])
def send():
    cap_resp = request.args.get('captcha')
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "origin":"https://vote.1billionsummit.com",
    }



    payload = {
        "voter_id": str(uuid.uuid4()),
        "turnstile_response":cap_resp

    }

    vote = requests.post(f"https://vote-api.1billionsummit.com/participants/89e340a5-e612-41b2-841a-0d3881d087c6/vote",headers=headers,json=payload) # هنا هتحط ,proxies=proxy قبل القوس لو عايز تستخدم البروكسي لو مش عايز سيبو مكانو
    # بالنسبه لل id الي قبل /vote دا بتاع الشخص بيتغير على حسب الشخص الي انت عايز تصوتلو 
    print(vote.text)
    return vote.text
if __name__ == "__main__":
    app.run(port=2000)
