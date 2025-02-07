from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def station_date(station, date):
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


@app.route("/api/v1/<station>")
def station_all_data(station):
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result



@app.route("/api/v1/yearly/<station>/<year>")
def station_year(station, year):
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)

    df['    DATE'] = df['    DATE'].astype(str)
    filtered_data = df[df['    DATE'].str.startswith(str(year))]

    results = pd.DataFrame()
    results["Date"], results["Temperature"] = filtered_data['    DATE'], filtered_data['   TG'] / 10

    return results.to_dict(orient="records")


if __name__ == "__main__":
    app.run(debug=True)