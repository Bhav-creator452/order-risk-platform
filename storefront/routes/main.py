from flask import Blueprint, render_template, request

from services.risk_service import score_order

from datetime import datetime

import logging

main_bp = Blueprint("main", __name__)
logger = logging.getLogger(__name__)

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

        except Exception:
            logger.exception("Prediction request failed.")
            error = (
                "Unable to connect to the prediction service. "
                "Please make sure the Order Risk API is running."
                    )
            
    return render_template(
        "index.html",
        result=result,
        error=error,
        prediction_time=prediction_time,
        form_data=request.form,
    )