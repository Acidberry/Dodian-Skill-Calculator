from flask import Flask, render_template, request
from skills import SKILLS
import logic

app = Flask(__name__)

@app.route("/")
def index():
    # Tu musíme poslať 'skills' (množné číslo), lebo index.html to tak vyžaduje
    return render_template("index.html", skills=SKILLS)

@app.route("/skill/<skill_name>", methods=["GET", "POST"])
def skill_detail(skill_name):
    skill_data = SKILLS[skill_name]
    result = None
    zipped_actions = None

    if request.method == "POST":
        try:
            current_level = request.form.get("current_level", "")
            target_level = request.form.get("target_level", "")
            current_xp = request.form.get("current_xp", "")
            target_xp = request.form.get("target_xp", "")
            active_pair = request.form.get("active_pair")

            if active_pair == '1':
                current_level = int(current_level)
                target_level = int(target_level)

                # do calculations here
                result = logic.calculate(
                    active_pair,
                    skill_data,
                    current_level,
                    current_xp,
                    target_level,
                    target_xp
                )
                zipped_actions = list(zip(skill_data['actions'], result['resultActions']))
            elif active_pair == '2':
                current_xp = int(current_xp)
                target_xp = int(target_xp)
                # do calculations here
                result = logic.calculate(
                    active_pair,
                    skill_data,
                    current_level,
                    current_xp,
                    target_level,
                    target_xp
                )
                zipped_actions = list(zip(skill_data['actions'], result['resultActions']))
        except ValueError:
            result = {"error": "You need to write numbers!"}

    return render_template("skill.html", skill=skill_data, skill_key=skill_name, result=result, zipped=zipped_actions)

if __name__ == "__main__":
    app.run(debug=True)
