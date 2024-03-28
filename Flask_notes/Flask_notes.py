from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # The "/" is an endpoint!
def hello_world():
    return render_template(
        "jinja_intro.html", name = "Bob Smith", template_name = "Django"
        )

@app.route("/expressions/")
def Jinja_function():

    #Interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    #Addition & Substraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    #String concatenation
    first_name = "Captain"
    last_name = "Marvel"

    # DO NOT DO THAT
    # return render_template(
    #     "expressions.html", color=color, 
    #     animal_one = animal_one, animal_two = animal_two, 
    #     orange_amount = orange_amount, apple_amount = apple_amount,
    #     donate_amount = donate_amount, first_name = first_name,
    #     last_name = last_name
    # )

    # DO THAT!
    kwargs = {
        "color": color, 
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
        }

    return render_template(
        "expressions.html", **kwargs
    )
