from flask import Flask, render_template, request, redirect
import random, smtplib, pymongo

client = pymongo.MongoClient(
    "mongodb+srv://ams1234:ams1234@cluster0.ph4hzjn.mongodb.net/"
)
db = client["Hackit"]
col = db["users"]

app = Flask(__name__)


@app.route("/")
def landing_page():
    return render_template("landingpage.html")


@app.route("/home")
def return_home():
    return render_template("landingpage.html")


@app.route("/contactus")
def contact_us():
    return render_template("contactus.html")


@app.route("/login")
def login_page():
    return render_template("loginpage.html")


@app.route("/register")
def register_page():
    return render_template("registerpage.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/send_otp", methods=["POST"])
def send_otp():
    if request.method == "POST":
        data = request.get_json()
        email = data.get("email")

        global otp
        otp = "".join([str(random.randint(0, 9)) for i in range(4)])
        message = f"Subject: Password reset OTP\n\nHi!\n\nYour OTP is: {otp}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("budgetbuddy.chatbot@gmail.com", "kmcz lrhh qdhu gfvl")

        server.sendmail("budgetbuddy.chatbot@gmail.com", email, message)
        server.quit()

        return "OTP sent to your email!", 200
    return "Invalid request", 400


@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")

        if request.form["action"] == "reset_password":
            user_entered_otp = request.form.get("otp")
            new_password = request.form.get("password")
            confirm_password = request.form.get("conf-password")

            if user_entered_otp != otp:  # Verify the OTP
                return render_template("forgotpassword.html", message="Invalid OTP!")

            # If OTP is valid and new password matches the confirmation, proceed with password reset logic
            if new_password == confirm_password:
                # Implement the logic to update the user's password in the database
                return "Password successfully reset!"
            else:
                return "Passwords do not match!"

    return render_template("forgotpassword.html")


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


@app.route("/stockmain")
def stockmain():
    return render_template("stockmain.html")


@app.route("/btc")
def btcpage():
    return render_template("btc.html")


@app.route("/eth")
def ethpage():
    return render_template("eth.html")


@app.route("/xmr")
def xmrpage():
    return render_template("xmr.html")


@app.route("/hdb")
def hdfcpage():
    return render_template("hdb.html")


@app.route("/axis")
def axisbankpage():
    return render_template("axis.html")


@app.route("/adaniports")
def adaniports():
    return render_template("adaniports.html")


@app.route("/sunpharma")
def sunpharma():
    return render_template("sunpharma.html")


@app.route("/tvsmotors")
def tvsmotors():
    return render_template("tvsmotors.html")


@app.route("/infosys")
def infosys():
    return render_template("infosys.html")


@app.route("/sbi")
def sbi():
    return render_template("sbi.html")


@app.route("/maruti")
def maruti():
    return render_template("maruti.html")


@app.route("/cumminsind")
def cumminsindia():
    return render_template("cumminsind.html")


@app.route("/deepakntr")
def deepakntr():
    return render_template("deepakntr.html")


@app.route("/tcs")
def tcs():
    return render_template("tcs.html")


@app.route("/hcl")
def hcl():
    return render_template("hcl.html")


@app.route("/icici")
def icici():
    return render_template("icici.html")


@app.route("/amazon")
def amazon():
    return render_template("amazon.html")


@app.route("/dixon")
def dixon():
    return render_template("dixon.html")


if __name__ == "__main__":
    app.run(debug=True)
