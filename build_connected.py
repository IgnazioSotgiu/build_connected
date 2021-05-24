import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
import datetime

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/welcome_page")
def welcome_page():
    return render_template("welcome-page.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        check_username = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        check_password = request.form.get("password")
        check_confirm_password = request.form.get("confirm_password")

        if check_username:
            flash("Username already exists")
            return redirect(url_for('register'))

        elif check_password != check_confirm_password:
            flash("Passwords don't match.")
            flash("Please re-enter passwords")
            return redirect(url_for('register'))

        new_user = {
            "username": request.form.get("username").lower(),
            "company_name": request.form.get("company_name").lower(),
            "contractor_type": request.form.get("contractor_type").lower(),
            "categories": request.form.get("category").lower(),
            "county": request.form.get("county").lower(),
            "country": request.form.get("country").lower(),
            "email": request.form.get("email"),
            "phone_number": request.form.get("phone"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        session["user"] = request.form.get("username").lower()
        flash("Welcome {}. Registration Successful".format(
            request.form.get("username")))
        return redirect(url_for("homepage", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        check_username = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if check_username:
            if check_password_hash(
                    check_username["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hello {}, you were successfully logged in".format(
                        request.form.get("username")))
                return redirect(url_for("homepage", username=session["user"]))

        else:
            flash("Incorrect username and/or password.")
            flash("Please try again.")
            return render_template('login.html')

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have logged out")
    return redirect(url_for("welcome_page"))


@app.route("/homepage/<username>", methods=["GET", "POST"])
def homepage(username):
    jobs = get_latest_jobs()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("homepage.html", username=username, jobs=jobs)


# get the last 10 jobs entered
def get_latest_jobs():
    latest_jobs = mongo.db.jobs.find().sort("date_job_created", -1).limit(10)
    return latest_jobs


@app.route("/add_job", methods=['GET', 'POST'])
def add_job():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if request.method == "POST":
        new_job = {
            "job_title": request.form.get("job_title").lower(),
            "category": request.form.get("job_category").lower(),
            "employer": mongo.db.users.find_one(
                {"username": session["user"]})["company_name"].lower(),
            "contact_phone_number": request.form.get("phone"),
            "contact_email": mongo.db.users.find_one(
                {"username": session["user"]})["email"],
            "county": request.form.get("county").lower(),
            "starting_date": request.form.get("starting_date"),
            "is_urgent": request.form.get("is_urgent"),
            "date_job_created": datetime.date.today().strftime("%d/%m/%Y"),
            "created_by": mongo.db.users.find_one(
                {"username": session["user"]})["username"]
        }
        mongo.db.jobs.insert_one(new_job)
        flash("New job successfully added")
        return redirect(url_for("homepage", username=username))

    return render_template("add-job.html")


@app.route("/my_jobs/<username>")
def my_jobs(username):
    my_jobs_list = mongo.db.jobs.find(
        {"created_by": session["user"]}).sort("date_job_created", -1)

    return render_template(
        "my-jobs.html", my_jobs_list=my_jobs_list, username=username)


@app.route("/profile/<username>")
def profile(username):
    my_profile = get_profile(username)
    return render_template(
        "profile-page.html", username=username, my_profile=my_profile)


def get_profile(username):
    my_profile = {
        "username": username,
        "company_name": mongo.db.users.find_one(
            {"username": username})["company_name"],
        "contractor_type": mongo.db.users.find_one(
            {"username": username})["contractor_type"],
        "categories": mongo.db.users.find_one(
            {"username": username})["categories"],
        "county": mongo.db.users.find_one(
            {"username": username})["county"],
        "country": mongo.db.users.find_one(
            {"username": username})["country"],
        "email": mongo.db.users.find_one(
            {"username": username})["email"],
        "phone_number": mongo.db.users.find_one(
            {"username": username})["phone_number"],
        "password": mongo.db.users.find_one({"username": username})["password"]
    }
    return my_profile


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    my_profile = get_profile(username)
    if request.method == "POST":
        update_user = {
            "username": username,
            "company_name": request.form.get("company_name").lower(),
            "contractor_type": request.form.get("contractor_type").lower(),
            "categories": request.form.get("categories").lower(),
            "county": request.form.get("county").lower(),
            "country": request.form.get("country").lower(),
            "email": request.form.get("email"),
            "phone_number": request.form.get("phone_number"),
            "password": my_profile["password"]
        }
        mongo.db.users.update({"username": username}, update_user)
        flash("Profile Successfully Updated")
        my_profile = get_profile(username)
        return render_template(
            'profile-page.html', username=username, my_profile=my_profile)

    return render_template(
        "edit-profile.html", username=username, my_profile=my_profile)


@app.route("/edit_password/<username>", methods=["GET", "POST"])
def edit_password(username):
    my_profile = get_profile(username)
    if request.method == "POST":
        # check old password match with the existing password
        old_password = mongo.db.users.find_one(
            {"username": username})["password"]
        if check_password_hash(old_password, request.form.get("password")):
            check_password = request.form.get("new_password")
            check_confirm_password = request.form.get("confirm_new_password")
            if check_password == check_confirm_password:
                new_password = generate_password_hash(check_password)
                mongo.db.users.update({"username": username},
                {"$set": {"password": new_password}})
                flash("Password Successfully Changed")
                return render_template(
                    'profile-page.html',
                    username=username, my_profile=my_profile) 

    return render_template("edit-password.html", username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
