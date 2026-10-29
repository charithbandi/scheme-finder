"""
Flask Application Backend for Scheme Finder.
Provides REST API endpoints for user profile evaluation, scheme browsing,
document checklist generation, and serves the responsive modern web UI.
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
from engine import EligibilityEngine
from schemes_data import get_all_schemes

# Initialize app with static and template configurations
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Load schemes database and initialize rule engine
schemes_list = get_all_schemes()
engine = EligibilityEngine(schemes=schemes_list)


@app.route("/")
def index():
    """Serves the main application UI."""
    return render_template("index.html")


@app.route("/api/health", methods=["GET"])
def health():
    """Health check and metadata endpoint."""
    return jsonify({
        "status": "online",
        "service": "Scheme Finder API",
        "total_schemes_loaded": len(schemes_list),
        "engine": "Boolean Threshold Rule-Based Matcher"
    })


@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    """
    Evaluates a user profile JSON against all schemes and returns ranked matches
    with transparent 'Why You Qualify' rules and required document checklists.
    """
    profile = request.get_json(force=True, silent=True)
    if not profile:
        return jsonify({"error": "Invalid request body. Expected JSON profile."}), 400

    # Clean & normalize profile fields
    sanitized_profile = {
        "income": float(profile.get("income", 0)) if profile.get("income") not in [None, ""] else 0,
        "marks": float(profile.get("marks", 0)) if profile.get("marks") not in [None, ""] else 0,
        "category": str(profile.get("category", "General")).strip(),
        "gender": str(profile.get("gender", "Any")).strip(),
        "state": str(profile.get("state", "Pan-India")).strip(),
        "course_level": str(profile.get("course_level", "UG")).strip(),
        "is_first_graduate": bool(profile.get("is_first_graduate", False)),
        "is_disabled": bool(profile.get("is_disabled", False)),
        "is_single_girl_child": bool(profile.get("is_single_girl_child", False)),
        "is_govt_school": bool(profile.get("is_govt_school", False)),
        "is_farmer": bool(profile.get("is_farmer", False)),
    }

    results = engine.evaluate_profile(sanitized_profile)

    return jsonify({
        "status": "success",
        "evaluated_profile": sanitized_profile,
        "total_matches": len(results),
        "eligible_schemes": results
    })


@app.route("/api/schemes", methods=["GET"])
def get_schemes():
    """Returns all available schemes with optional state, category or query filter."""
    category = request.args.get("category")
    state = request.args.get("state")
    query = request.args.get("q", "").strip().lower()

    filtered = []
    for s in schemes_list:
        if state and state.lower() != "all":
            if s.state.lower() != state.lower() and s.state.lower() not in ["all india", "pan-india", "central"]:
                continue
        if category and category.lower() != "all":
            if s.category_type.lower() != category.lower():
                continue
        if query and (query not in s.name.lower() and query not in s.department.lower() and query not in s.description.lower() and query not in s.state.lower()):
            continue
        filtered.append(s.to_dict())

    return jsonify({
        "total": len(filtered),
        "schemes": filtered
    })


@app.route("/api/scheme/<scheme_id>", methods=["GET"])
def get_scheme_detail(scheme_id):
    """Returns single scheme detailed checklist and metadata."""
    scheme = next((s for s in schemes_list if s.id == scheme_id), None)
    if not scheme:
        return jsonify({"error": "Scheme not found"}), 404

    return jsonify({
        "id": scheme.id,
        "name": scheme.name,
        "department": scheme.department,
        "category_type": scheme.category_type,
        "state": scheme.state,
        "description": scheme.description,
        "benefit": scheme.benefit,
        "official_portal_url": scheme.official_portal_url,
        "documents": scheme.documents,
        "rules": [
            {
                "attribute": r.attribute_name,
                "operator": r.operator,
                "target": r.target_value,
                "template": r.explanation_template
            }
            for r in scheme.rules
        ]
    })


if __name__ == "__main__":
    # Standard development server port
    port = int(os.environ.get("PORT", 5000))
    print(f"Scheme Finder server running at http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=False)
