import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# صفحة للتأكد أن النظام يعمل
@app.route("/", methods=['GET'])
def home():
    return "نظام ذكاء اصطناعي السجاد يعمل بنجاح ومستعد لاستقبال طلبات المندوبين"

# محرك استقبال رسائل الواتساب
@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    sender_number = request.form.get('From')
    image_url = request.form.get('MediaUrl0')
    
    resp = MessagingResponse()
    msg = resp.message()

    if image_url:
        # رسالة تأكيد للمندوب عند استلام الصورة
        msg.body(f"مرحباً.. وصلت صورة السجادة من رقمك ({sender_number}). جاري عزل الخلفية ووضعها تحت الأثاث آلياً...")
    else:
        msg.body("من فضلك أرسل صورة السجادة لنقوم بمعالجتها لك فوراً.")

    return str(resp)

if __name__ == "__main__":
    # تشغيل النظام على المنصة السحابية
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

