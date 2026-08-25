from flask import Flask, render_template, request, jsonify

from interview_engine import (
    INTERVIEW_DATA,
    get_question,
    evaluate_answer
)


# =========================================================
# CREATE FLASK APPLICATION
# =========================================================

app = Flask(__name__)


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def index():

    return render_template(
        "index.html",
        roles=INTERVIEW_DATA.keys()
    )


# =========================================================
# GET INTERVIEW QUESTION
# =========================================================

@app.route("/question", methods=["POST"])
def question():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data received."
            }), 400


        role = data.get("role")

        used_questions = data.get(
            "used_questions",
            []
        )


        # Check job role

        if not role:

            return jsonify({
                "error": "Please select a job role."
            }), 400


        if role not in INTERVIEW_DATA:

            return jsonify({
                "error": "Invalid job role."
            }), 400


        # Get question

        question_data = get_question(
            role,
            used_questions
        )


        return jsonify({

            "success": True,

            "question":
                question_data["question"]

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "error":
                f"Unable to generate question: {str(e)}"

        }), 500


# =========================================================
# EVALUATE CANDIDATE ANSWER
# =========================================================

@app.route("/evaluate", methods=["POST"])
def evaluate():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "error":
                    "No answer data received."
            }), 400


        role = data.get("role")

        question = data.get("question")

        answer = data.get(
            "answer",
            ""
        ).strip()


        # -------------------------------------------------
        # Validate role
        # -------------------------------------------------

        if not role:

            return jsonify({
                "error":
                    "Job role is required."
            }), 400


        if role not in INTERVIEW_DATA:

            return jsonify({
                "error":
                    "Invalid job role."
            }), 400


        # -------------------------------------------------
        # Validate question
        # -------------------------------------------------

        if not question:

            return jsonify({
                "error":
                    "Interview question is required."
            }), 400


        # -------------------------------------------------
        # Validate answer
        # -------------------------------------------------

        if not answer:

            return jsonify({
                "error":
                    "Please enter your answer."
            }), 400


        # -------------------------------------------------
        # Find question
        # -------------------------------------------------

        question_data = None


        for item in INTERVIEW_DATA[role]:

            if item["question"] == question:

                question_data = item

                break


        if question_data is None:

            return jsonify({
                "error":
                    "Question not found."
            }), 404


        # -------------------------------------------------
        # Evaluate answer
        # -------------------------------------------------

        result = evaluate_answer(
            answer,
            question_data
        )


        # -------------------------------------------------
        # Return result
        # -------------------------------------------------

        return jsonify({

            "success": True,

            "score":
                result["score"],

            "keyword_score":
                result["keyword_score"],

            "similarity_score":
                result["similarity_score"],

            "length_score":
                result["length_score"],

            "matched_keywords":
                result["matched_keywords"],

            "strengths":
                result["strengths"],

            "weaknesses":
                result["weaknesses"],

            "feedback":
                result["feedback"]

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "error":
                f"Answer evaluation failed: {str(e)}"

        }), 500


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route("/health")
def health():

    return jsonify({

        "status": "running",

        "application":
            "AI Interview Coach",

        "version":
            "1.0",

        "message":
            "Interview Coach API is working."

    })


# =========================================================
# ERROR HANDLERS
# =========================================================

@app.errorhandler(404)
def page_not_found(error):

    return jsonify({

        "error":
            "Page not found."

    }), 404


@app.errorhandler(500)
def internal_server_error(error):

    return jsonify({

        "error":
            "Internal server error."

    }), 500


# =========================================================
# START APPLICATION
# =========================================================

if __name__ == "__main__":

    print("=" * 55)

    print(
        "🤖 AI INTERVIEW COACH"
    )

    print(
        "NLP-Based Mock Interview System"
    )

    print("=" * 55)

    print(
        "Available Job Roles:"
    )

    for role in INTERVIEW_DATA:

        print(
            f"  • {role}"
        )

    print("=" * 55)

    print(
        "🌐 Open: http://127.0.0.1:5000"
    )

    print("=" * 55)


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )