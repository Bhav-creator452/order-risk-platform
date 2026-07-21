from flask import Blueprint, render_template, request

main_bp = Blueprint("main", __name__)


@main_bp.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        print(request.form)
    
    return render_template("index.html")