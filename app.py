from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

CROP_DATA = {
    "Rice": {
        "soil": "Clayey / loamy soil with good water-holding capacity",
        "season": "Kharif",
        "water": "High",
        "fertilizer": "Nitrogen + phosphorus + potassium based on soil test",
        "tip": "Maintain shallow standing water during key growth stages and avoid prolonged waterlogging."
    },
    "Wheat": {
        "soil": "Well-drained loam or clay loam",
        "season": "Rabi",
        "water": "Medium",
        "fertilizer": "Balanced NPK with nitrogen split across growth stages",
        "tip": "Irrigate around crown-root initiation and other critical stages rather than on a fixed schedule."
    },
    "Cotton": {
        "soil": "Deep, well-drained black soil or suitable loam",
        "season": "Kharif",
        "water": "Medium",
        "fertilizer": "Balanced NPK with micronutrients where soil tests indicate deficiency",
        "tip": "Scout regularly for sucking pests and bollworm symptoms; use integrated pest management."
    },
    "Groundnut": {
        "soil": "Sandy loam / well-drained soil",
        "season": "Kharif",
        "water": "Medium",
        "fertilizer": "Phosphorus, potassium and calcium as recommended by soil test",
        "tip": "Avoid excess irrigation and keep the field weed-free during early crop growth."
    },
    "Tomato": {
        "soil": "Fertile, well-drained loamy soil",
        "season": "Year-round with suitable local conditions",
        "water": "Medium",
        "fertilizer": "Balanced NPK plus micronutrients based on soil test",
        "tip": "Use drip irrigation where possible and avoid wetting foliage frequently."
    },
    "Maize": {
        "soil": "Well-drained fertile loam",
        "season": "Kharif / Rabi depending on region",
        "water": "Medium",
        "fertilizer": "Nitrogen-rich balanced fertilizer program guided by soil test",
        "tip": "Protect the crop from moisture stress during flowering and grain filling."
    }
}

DISEASE_RULES = {
    "yellowing": ("Possible nutrient deficiency or root/water stress", "Check soil moisture and arrange a soil test before applying fertilizer."),
    "spots": ("Possible fungal or bacterial leaf disease", "Remove severely affected leaves where practical, improve airflow, and consult a local agriculture expert for diagnosis."),
    "wilting": ("Possible water stress, root disease, or vascular issue", "Check soil moisture, drainage, roots and recent weather before deciding treatment."),
    "holes": ("Possible insect feeding", "Inspect the underside of leaves and growing points; use integrated pest management and avoid unnecessary pesticide use."),
    "curling": ("Possible sucking-pest pressure, heat stress, or viral symptoms", "Inspect for insects and isolate severely affected plants if a viral disease is suspected.")
}

@app.route("/")
def index():
    return render_template("index.html", crops=list(CROP_DATA.keys()))

@app.route("/api/advice", methods=["POST"])
def advice():
    data = request.get_json(silent=True) or {}
    crop = data.get("crop", "Rice")
    soil = data.get("soil", "Loamy")
    stage = data.get("stage", "Vegetative")
    issue = data.get("issue", "No major issue")
    item = CROP_DATA.get(crop, CROP_DATA["Rice"])

    advice_text = (
        f"For {crop} at the {stage} stage on {soil.lower()} soil: "
        f"focus on {item['water'].lower()} water management and use a {item['fertilizer'].lower()} program. "
        f"{item['tip']} "
        f"Reported issue: {issue}. Verify the diagnosis locally before applying any pesticide or fertilizer."
    )
    return jsonify({
        "crop": crop,
        "season": item["season"],
        "soil": item["soil"],
        "water": item["water"],
        "fertilizer": item["fertilizer"],
        "advice": advice_text
    })

@app.route("/api/disease", methods=["POST"])
def disease():
    data = request.get_json(silent=True) or {}
    symptom = data.get("symptom", "yellowing")
    result = DISEASE_RULES.get(symptom, DISEASE_RULES["yellowing"])
    return jsonify({"finding": result[0], "action": result[1]})

@app.route("/api/market")
def market():
    # Demo values for the academic prototype; not live market prices.
    return jsonify([
        {"crop": "Wheat", "price": "₹2,650", "unit": "quintal", "change": "+2.1%"},
        {"crop": "Rice", "price": "₹2,380", "unit": "quintal", "change": "+1.4%"},
        {"crop": "Cotton", "price": "₹7,150", "unit": "quintal", "change": "-0.8%"},
        {"crop": "Groundnut", "price": "₹6,200", "unit": "quintal", "change": "+3.2%"}
    ])

if __name__ == "__main__":
    app.run(debug=True, port=5001)
