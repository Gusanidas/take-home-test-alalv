from flask import Flask, render_template, request
from typing import Callable
import calculator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prefix_output, infix_output = "", ""
        if "prefix_input" in request.form:
            prefix_input = request.form["prefix_input"]
            prefix_output = compute(prefix_input, calculator.eval_prefix_expr)
        if "infix_input" in request.form:
            infix_input = request.form["infix_input"]
            infix_output = compute(infix_input, calculator.eval_infix_expr)
        return render_template("home.html", prefix_output = prefix_output, infix_output = infix_output)
    else:
        return render_template("home.html")

def compute(expr: str, func: Callable) -> str:
    try:
        output = func(expr)
        return str(output)
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    app.run()