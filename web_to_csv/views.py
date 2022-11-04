from time import sleep

from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlite3 import IntegrityError, OperationalError

from .database.database import Database
from .config import DATABASE_PATH

view = Blueprint("views", __name__)


@view.route("/", methods=("GET", "POST"))
def index():
    # Vars fot html select options.
    options = ["Good", "Bad", "Indifferent"]

    if request.method != "POST":
        # Render empty web form.
        return render_template("index.html", options=options)
    else:
        # Submitted answer
        q1_answer = request.form["q1"]
        q2_answer = request.form["q2"]
        q3_answer = request.form["q3"]

        # Check that all questions have been answered.
        all_questions_answered = True
        answers = [q1_answer, q2_answer, q3_answer]
        for answer in answers:
            if not answer or answer == "":
                all_questions_answered = False
                flash("An answer must be given for all questions")
                break

        if all_questions_answered:
            # Init connection to db and commit.
            try:
                db = Database(DATABASE_PATH)
                db.cursor.execute(
                    f"""
                    INSERT INTO opinion_poll (q1, q2, q3)
                    VALUES ('{q1_answer}', '{q2_answer}', '{q3_answer}');
                    """
                )  # TODO: Find better way to get table, and column names.
                db.connection.commit()
            except OperationalError:
                # Try committing again after 1 second.
                sleep(1)
                db.connection.commit()  # TODO: Find better alternative.
            else:
                db.connection.close()
                return redirect(url_for("views.thankyou"))

        # Rerender form if not fully answered.
        return render_template("index.html", options=options)


@view.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
