from flask import Flask, jsonify, render_template
import pandas as pd
from sodapy import Socrata

### create a flask instance
app = Flask(__name__)
# Example authenticated client (needed for non-public datasets):
client = Socrata("data.richmondgov.com",
                 "9YLbBPExr34rv8so3YWrgKlAM")
                 #userame="afcummings7@gmail.com.com",
                 #password="Deepshrub860")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("rvtv-zgyc", limit=1000)
#print(results)


# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
#results_df

results_df = results_df.drop(results_df.columns[[0,1,2,3]], axis=1)
results_df = results_df.dropna(subset=["location_1"])
#results_df

results_list = results_df.values.tolist()

crime_df = pd.read_csv("C:\\Users\\AFCummings\\git\\Project2RiotGamesData\\Resources\\Crime Information.csv")
column_list = list(crime_df)
column_list.remove("NEIGHBORHOOD_NAME")
column_list.remove("Lat")
column_list.remove("Long")
print(column_list)
crime_df["sum"] = crime_df[column_list].sum(axis=1)
#crime_df

crime_df = crime_df.drop(crime_df.columns[[0,1,2,3,4,5,6,7,8,9]], axis = 1)
crime_df.dropna()
crime_list = crime_df.values.tolist()

@app.route("/api/crimedata")
def crime_data_method():
    return jsonify(crime_list)

@app.route("/api/delinquencydata")
def delinquency_data_method():
    return jsonify(results_list)

@app.route("/")
def home():
    message = "This is a placeholder"
    #return render_template here

if __name__ == "__main__":
    app.run(debug=True)
