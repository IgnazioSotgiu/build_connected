from lib import app
from flask import (
    flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import re

mongo = PyMongo(app)

contractor_type = ["main contractor", "sub contractor", "architect"]
contractor_type.sort()


construction_categories = ["electrician", "plumber",
                           "surveyor", "architect", "bathroom fitter",
                           "bedroom fitter", "bricklayer",
                           "building surveyor", "building technician",
                           "carpenter", "carpet fitter", "crane operator",
                           "floor layer", "interior designer", "joiner",
                           "kitchen fitter", "painter and decorator",
                           "risk manager", "project manager", "scaffolder",
                           "roofing operative", "site manager",
                           "stonemason", "wall and floor tyler",
                           "welder engineer", "technical coordinator",
                           "general contractor"]
construction_categories.sort()


COUNTIES = ["carlow", "cavan", "clare", "cork", "donegal", "dublin",
            "galway", "kerry", "kildare", "kilkenny", "laois",
            "leitrim", "limerick", "longford", "louth", "mayo",
            "meath", "monaghan", "offaly", "roscommon", "sligo",
            "tipperary", "waterford", "westmeath", "wexford",
            "wicklow"]
COUNTIES.sort()

regex = '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'


# validate email address function (stack overflow)
def check(email):
    if(re.search(regex, email)):
        return True

    else:
        return False


@app.route("/")
@app.route("/welcome_page")
def welcome_page():
    return render_template("welcome-page.html")


def get_users_company_names():
    return mongo.db.users.distinct("company_name")


def get_users_categories():
    return mongo.db.users.distinct("categories")


def get_users_counties():
    return mongo.db.users.distinct("county")


def get_jobs_company_names():
    return mongo.db.jobs.distinct("employer")


def get_jobs_categories():
    return mongo.db.jobs.distinct("category")


def get_jobs_counties():
    return mongo.db.jobs.distinct("county")


# get the last 10 jobs entered
def get_latest_jobs():
    return mongo.db.jobs.find().sort([['_id', -1]]).limit(10)


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        check_username = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        check_password = request.form.get("password")
        check_confirm_password = request.form.get("confirm_password")
        valid_email = check(request.form.get("email"))

        if check_username:
            flash(
                "Username already exists. Choose a different username",
                "error")
            return redirect(url_for('register'))

        elif check_password != check_confirm_password:
            flash(
                "Passwords don't match. Please re-enter passwords",
                "error")
            return redirect(url_for('register'))

        elif not valid_email:
            flash(
                "Invalid email address. Please enter a valid email address",
                "error")
            return redirect(url_for('register'))

        new_user = {
            "username": request.form.get("username").lower(),
            "company_name": request.form.get("company_name").lower(),
            "contractor_type": request.form.get("contractor_type").lower(),
            "categories": list(request.form.getlist("category")),
            "county": request.form.get("county").lower(),
            "country": request.form.get("country").lower(),
            "email": request.form.get("email"),
            "phone_number": request.form.get("phone"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        session["user"] = request.form.get("username").lower()
        flash("Welcome {}. Registration Successful".format(
            request.form.get("username")), "success")
        return redirect(url_for(
            "homepage_latest_jobs", username=session["user"]))

    return render_template("register.html",
                           construction_categories=construction_categories,
                           COUNTIES=COUNTIES, contractor_type=contractor_type)


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
                        request.form.get("username")), "success")
                return redirect(url_for(
                    "homepage_latest_jobs", username=session["user"]))

        else:
            flash("Incorrect username and/or password. Please try again.",
                  "error")
            return render_template('login.html')

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have logged out", "success")
    return redirect(url_for("welcome_page"))


@app.route("/homepage_latest_jobs/<username>", methods=["GET", "POST"])
def homepage_latest_jobs(username):
    jobs = get_latest_jobs()
    company_names = get_users_company_names()
    users_categories = get_users_categories()
    users_counties = get_users_counties()
    jobs_company_names = get_jobs_company_names()
    jobs_categories = get_jobs_categories()
    jobs_counties = get_jobs_counties()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "homepage_latest_jobs.html", username=username, jobs=jobs,
        users_categories=users_categories,
        users_counties=users_counties, company_names=company_names,
        jobs_company_names=jobs_company_names, jobs_categories=jobs_categories,
        jobs_counties=jobs_counties)


@app.route("/add_job", methods=['GET', 'POST'])
def add_job():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    defoult_email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    if request.method == "POST":
        valid_email = check(request.form.get("email"))
        if not valid_email:
            flash(
                "Invalid email address. Please enter a valid email address",
                "error")
            return redirect('add_job')

        new_job = {
            "job_title": request.form.get("job_title").lower(),
            "category": list(request.form.getlist("job_category")),
            "employer": mongo.db.users.find_one(
                {"username": session["user"]})["company_name"].lower(),
            "contact_phone_number": request.form.get("phone"),
            "contact_email": mongo.db.users.find_one(
                {"username": session["user"]})["email"],
            "county": request.form.get("county").lower(),
            "starting_date": request.form.get("starting_date"),
            "is_urgent": request.form.get("is_urgent"),
            "description": request.form.get("description"),
            "date_job_created": datetime.date.today().strftime("%d/%m/%Y"),
            "created_by": mongo.db.users.find_one(
                {"username": session["user"]})["username"]
        }
        mongo.db.jobs.insert_one(new_job)
        flash("New job successfully added", "success")
        return redirect(url_for("homepage_latest_jobs", username=username))

    return render_template("add-job.html",
                           construction_categories=construction_categories,
                           COUNTIES=COUNTIES, username=username,
                           defoult_email=defoult_email)


@app.route("/my_jobs/<username>")
def my_jobs(username):
    my_jobs_list = mongo.db.jobs.find(
        {"created_by": session["user"]}).sort([['_id', -1]])

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
            "categories": list(request.form.getlist("user_job_categories")),
            "county": request.form.get("user_county").lower(),
            "country": request.form.get("user_country").lower(),
            "email": request.form.get("email"),
            "phone_number": request.form.get("user_phone"),
            "password": my_profile["password"]
        }
        mongo.db.users.update({"username": username}, update_user)
        flash("Profile Successfully Updated", "success")
        my_profile = get_profile(username)
        return render_template(
            'profile-page.html', username=username, my_profile=my_profile)

    return render_template(
        "edit-profile.html", username=username, my_profile=my_profile,
        construction_categories=construction_categories, COUNTIES=COUNTIES,
        contractor_type=contractor_type)


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
                mongo.db.users.update(
                    {"username": username},
                    {"$set": {"password": new_password}})

                flash("Password Successfully Changed", "success")
                return render_template(
                    'profile-page.html',
                    username=username, my_profile=my_profile)

            flash(
                "Old Password incorrect or new password doesn't match",
                "error")
            return render_template("edit-password.html", username=username)

        flash("Old Password incorrect or new password doesn't match", "error")
        return render_template("edit-password.html", username=username)

    return render_template("edit-password.html", username=username)


@app.route("/edit_job/<job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    defoult_email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    username = session["user"]
    if request.method == "POST":
        valid_email = check(request.form.get("email"))
        if not valid_email:
            flash(
                "Invalid email address. Please enter a valid email address",
                "error")
            return render_template(url_for('edit_job', job_id=job_id))

        edit_job = {
            "job_title": request.form.get("job_title").lower(),
            "category": list(request.form.getlist("edit_job_category")),
            "employer": mongo.db.users.find_one(
                {"username": session["user"]})["company_name"].lower(),
            "contact_phone_number": request.form.get("phone"),
            "contact_email": request.form.get("email"),
            "county": request.form.get("county").lower(),
            "starting_date": request.form.get("starting_date"),
            "is_urgent": request.form.get("is_urgent"),
            "description": request.form.get("description"),
            "date_job_created": mongo.db.jobs.find_one(
                {"_id": ObjectId(job_id)})["date_job_created"],
            "created_by": mongo.db.users.find_one(
                {"username": session["user"]})["username"]
        }
        mongo.db.jobs.update({"_id": ObjectId(job_id)}, edit_job)
        flash("Job successfully edited", "success")
        return redirect(url_for("my_jobs", username=username))

    return render_template("edit-job.html", job=job,
                           construction_categories=construction_categories,
                           COUNTIES=COUNTIES, username=username,
                           defoult_email=defoult_email)


@app.route("/delete_job_check/<job_id>")
def delete_job_check(job_id):
    username = session["user"]
    job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})

    return render_template(
        "job-delete-page.html", job=job, job_id=job_id, username=username)


@app.route("/delete_job/<job_id>")
def delete_job(job_id):
    username = session["user"]
    mongo.db.jobs.remove({"_id": ObjectId(job_id)})
    flash("The job was successfully deleted", "success")

    return redirect(url_for("my_jobs", username=username))


@app.route("/info/<job_id>")
def info(job_id):
    job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    username = session["user"]
    return render_template("job-info-page.html", username=username, job=job)


@app.route("/my_job_info/<job_id>")
def my_job_info(job_id):
    job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    username = session["user"]
    return render_template("my-job-info-page.html", username=username, job=job)


@app.route("/search_users", methods=["GET", "POST"])
def search_users():
    username = session["user"]
    company_names = get_users_company_names()
    users_categories = get_users_categories()
    users_counties = get_users_counties()
    jobs_company_names = get_jobs_company_names()
    jobs_categories = get_jobs_categories()
    jobs_counties = get_jobs_counties()
    query_users_by_name = request.form.get("src_company_by_name")
    query_users_by_category = request.form.get("src_company_by_category")
    query_users_by_county = request.form.get("src_company_by_county")
    if query_users_by_name:
        query = query_users_by_name
        src_result = list(
            mongo.db.users.find({"company_name": query.lower()}))
    elif query_users_by_category:
        query = query_users_by_category
        src_result = list(
            mongo.db.users.find({"categories": query.lower()}))
    elif query_users_by_county:
        query = query_users_by_county
        src_result = list(
            mongo.db.users.find({"county": query.lower()}))
    else:
        flash("Search parameters error", "error")
        return redirect(url_for('homepage_latest_jobs', username=username))

    if src_result:
        return render_template(
            'search-users.html', username=username, src_result=src_result,
            users_categories=users_categories, users_counties=users_counties,
            company_names=company_names, jobs_company_names=jobs_company_names,
            jobs_categories=jobs_categories, jobs_counties=jobs_counties)
    else:
        flash("Company not found.{}".format(src_result), "error")
        return redirect(url_for('homepage_latest_jobs', username=username))


@app.route("/search_jobs", methods=["GET", "POST"])
def search_jobs():
    username = session["user"]
    company_names = get_users_company_names()
    users_categories = get_users_categories()
    users_counties = get_users_counties()
    jobs_company_names = get_jobs_company_names()
    jobs_categories = get_jobs_categories()
    jobs_counties = get_jobs_counties()
    query_jobs_by_name = request.form.get("src_job_by_company")
    query_jobs_by_category = request.form.get("src_job_by_category")
    query_jobs_by_county = request.form.get("src_job_by_county")
    if query_jobs_by_name:
        query = query_jobs_by_name
        src_result = list(
            mongo.db.jobs.find({"employer": query.lower()}))
    elif query_jobs_by_category:
        query = query_jobs_by_category
        src_result = list(
            mongo.db.jobs.find({"category": query.lower()}))
    elif query_jobs_by_county:
        query = query_jobs_by_county
        src_result = list(
            mongo.db.jobs.find({"county": query.lower()}))
    else:
        flash("Search parameters error", "error")
        return redirect(url_for('homepage_latest_jobs', username=username))

    if src_result:
        return render_template(
            'search-jobs.html', username=username, src_result=src_result,
            users_categories=users_categories, users_counties=users_counties,
            company_names=company_names, jobs_company_names=jobs_company_names,
            jobs_categories=jobs_categories, jobs_counties=jobs_counties)
    else:
        flash("Jobs not found.{}".format(src_result), "error")
        return redirect(url_for('homepage_latest_jobs', username=username))


@app.route("/contact/<job_id>", methods=["GET", "POST"])
def contact(job_id):
    username = session["user"]
    company_name = mongo.db.users.find_one(
            {"username": username})["company_name"]
    defoult_email_from = mongo.db.users.find_one(
            {"username": username})["email"]
    defoult_email_to = mongo.db.jobs.find_one(
            {"_id": ObjectId(job_id)})['contact_email']
    if request.method == "POST":
        email_from = request.form.get("email_from")
        email_to = request.form.get("email_to")
        valid_email_from = check(email_from)
        valid_email_to = check(email_to)
        if not (valid_email_from or valid_email_to):
            flash("Invalid email address. Please enter a valid email address",
                  "error")
            return redirect(url_for('homepage_latest_jobs',
                            username=username))
        elif email_from == email_to:
            flash("You Cannot Apply For Your Own Jobs", "error")
            return redirect(url_for('homepage_latest_jobs',
                            username=username))

    return render_template("contact.html", job_id=job_id,
                           username=username, company_name=company_name,
                           defoult_email_from=defoult_email_from,
                           defoult_email_to=defoult_email_to)


@app.route("/contact_company/<company_id>", methods=["GET", "POST"])
def contact_company(company_id):
    username = session["user"]
    company_name = mongo.db.users.find_one(
            {"username": username})["company_name"]
    defoult_email_from = mongo.db.users.find_one(
            {"username": username})["email"]
    company_to = mongo.db.users.find_one(
            {"_id": ObjectId(company_id)})['company_name']
    defoult_email_to = mongo.db.users.find_one(
            {"_id": ObjectId(company_id)})['email']
    if request.method == "POST":
        email_from = request.form.get("company_email_from")
        email_to = request.form.get("company_email_to")
        valid_email_from = check(email_from)
        valid_email_to = check(email_to)
        if not (valid_email_from or valid_email_to):
            flash("Invalid email address. Please enter a valid email address",
                  "error")
            return redirect(url_for('homepage_latest_jobs',
                            username=username))
        elif email_from == email_to:
            flash("You Cannot Contact Yourself", "error")
            return redirect(url_for('homepage_latest_jobs',
                            username=username))

    return render_template("contact_company.html", company_id=company_id,
                           username=username, company_name=company_name,
                           defoult_email_from=defoult_email_from,
                           defoult_email_to=defoult_email_to,
                           company_to=company_to)
