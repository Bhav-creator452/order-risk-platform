from flask import Blueprint, render_template, request

from services.risk_service import score_order

from datetime import datetime

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    prediction_time = None

    if request.method == "POST":
        try:
            result = score_order(request.form)

            # Prepare values for display in the template
            result["fraud_percentage"] = round(
                result["fraud_probability"] * 100,
                2
            )

            if result["fraud_percentage"] >= 80:
                result["confidence"] = "Very High"

            elif result["fraud_percentage"] >= 60:
                result["confidence"] = "High"

            elif result["fraud_percentage"] >= 40:
                result["confidence"] = "Medium"

            else:
                result["confidence"] = "Low"

            prediction_time = datetime.now().strftime(
            "%d %b %Y • %I:%M %p"
)

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
        prediction_time=prediction_time,
    )