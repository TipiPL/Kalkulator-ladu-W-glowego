from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ obsługa przecinka i kropki
def safe_float(value):
    try:
        return float(str(value).replace(",", "."))
    except:
        return 0

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    advice = None

    if request.method == "POST":

        #  TRANSPORT
        car = safe_float(request.form.get("car"))
        bus = safe_float(request.form.get("bus"))
        bike = safe_float(request.form.get("bike"))
        train = safe_float(request.form.get("train"))
        flight = safe_float(request.form.get("flight"))

        # DIETA
        meat = safe_float(request.form.get("meat"))
        dairy = safe_float(request.form.get("dairy"))
        waste_food = safe_float(request.form.get("waste_food"))

        #  ENERGIA
        power = safe_float(request.form.get("power"))
        heating = safe_float(request.form.get("heating"))

        #  STYL ŻYCIA
        clothes = safe_float(request.form.get("clothes"))
        electronics = safe_float(request.form.get("electronics"))

        # 🗑ODPADY
        recycling = safe_float(request.form.get("recycling"))

        #  WODA
        water = safe_float(request.form.get("water"))

        #  OBLICZENIA
        transport = (
            car * 0.2 * 365 +
            bus * 0.05 * 365 +
            bike * 0.01 * 365 +
            train * 0.03 * 12 +
            flight * 90
        )

        diet = (
            meat * 5 * 52 +
            dairy * 1.2 * 365 +
            waste_food * 2 * 52
        )

        energy = (
            power * 0.5 * 12 +
            heating * 200
        )

        lifestyle = (
            clothes * 5 +
            electronics * 20
        )

        waste = (100 - recycling) * 2
        water_emission = water * 0.01 * 365

        result = transport + diet + energy + lifestyle + waste + water_emission

        #  PORADA
        if result < 5000:
            advice = "Świetnie  masz niski ślad CO₂!"
        elif result < 10000:
            advice = "Dobrze  ale możesz ograniczyć mięso i transport autem."
        else:
            advice = " Twój ślad CO₂ jest wysoki — spróbuj żyć bardziej ekologicznie."

    return render_template("index.html", result=result, advice=advice)


if __name__ == "__main__":
    app.run(debug=True)