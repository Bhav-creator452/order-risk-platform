from flask import Blueprint, render_template, request

from services.risk_service import score_order

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            result = score_order(request.form)

            print("\n===== PREDICTION RESULT =====")
            for key, value in result.items():
                print(f"{key:20}: {value}")
            print("=" * 35)

        except Exception as e:
            error = str(e)
            print(f"Error: {error}")

    return render_template(
        "index.html",
        result=result,
        error=error,
    )