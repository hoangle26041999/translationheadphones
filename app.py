from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Cấu hình Gmail
GMAIL_USER = 'vietanhtravel999@gmail.com'  # Địa chỉ Gmail của bạn
GMAIL_PASSWORD = 'wzfi esmx kvog chcg'  # Mật khẩu Gmail hoặc App Password


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Lấy thông tin từ form
        name = request.form["name"]
        phone = request.form["phone"]
        address = request.form["address"]
        quantity = request.form["quantity"]
        notes = request.form["notes"]

        # Gửi email thông báo
        send_email(name, phone, address, quantity, notes)
        return render_template("success.html")

    return render_template("index.html")


def send_email(name, phone, address, quantity, notes):
    # Tạo email
    subject = "New Order"
    body = f"New order received:\n\nName: {name}\nPhone: {phone}\nAddress: {address}\nQuantity: {quantity}\nNotes: {notes}"

    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = GMAIL_USER  # Gửi đến chính email của bạn
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Kết nối và gửi email qua Gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, GMAIL_USER, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)
