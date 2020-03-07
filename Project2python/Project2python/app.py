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

results_df = results_df.drop(results_df.columns[[0,1,2,3,4,5,6,7,9]], axis=1)
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

crime_by_type = pd.read_csv("C:\\Users\\AFCummings\\git\\Project2RiotGamesData\\Resources\\Crime Information.csv")
crime_by_type = crime_by_type.drop(crime_by_type.columns[[0,10,11]], axis=1)
#crime_by_type

#def sum_columns(column_name):
    #crime_by_type.loc['Total'] = pd.Series(crime_by_type[f"{column_name}"].sum(), index = [f"{column_name}"])
#sum_columns('HOMICIDE')
#sum_columns('SEX_OFFENSE')
#sum_columns('ROBBERY')
#sum_columns('ASSAULT')
#sum_columns('BURGLARY')
#sum_columns('VICE')
#sum_columns('THEFT')
#sum_columns('VEH_THEFT')
#sum_columns('OTHER')
def crime_sum_type(column_name, new_column):
    crime_by_type[f"{new_column}"] = crime_by_type[f"{column_name}"].sum(axis=0)
crime_sum_type('HOMICIDE', 'homicide_tot')
crime_sum_type('SEX_OFFENSE', 'sex_off_total')
crime_sum_type('ROBBERY', 'rob_total')
crime_sum_type('ASSAULT', 'assault_tot')
crime_sum_type('BURGLARY', 'burglary_tot')
crime_sum_type('VICE', 'vice_tot')
crime_sum_type('THEFT', 'theft_tot')
crime_sum_type('VEH_THEFT', 'veh_theft_tot')
crime_sum_type('OTHER', 'other_tot')    

crime_by_type = crime_by_type[['homicide_tot','sex_off_total','rob_total','assault_tot','burglary_tot','vice_tot','theft_tot',
                              'veh_theft_tot','other_tot']]

crime_by_type = crime_by_type[:1]
crime_type_list = crime_by_type.values.tolist()

crime2017 = pd.read_csv("C:\\Users\\AFCummings\\git\\Project2RiotGamesData\\Resources\\Crime Information2017-2018.csv")
crime2017 = crime2017.drop(crime2017.columns[[0]], axis=1)

def crime_2017_type(column_name, new_column):
    crime2017[f"{new_column}"] = crime2017[f"{column_name}"].sum(axis=0)
crime_2017_type('HOMICIDE', 'homicide_tot')
crime_2017_type('SEX_OFFENSE', 'sex_off_total')
crime_2017_type('ROBBERY', 'rob_total')
crime_2017_type('ASSAULT', 'assault_tot')
crime_2017_type('BURGLARY', 'burglary_tot')
crime_2017_type('VICE', 'vice_tot')
crime_2017_type('THEFT', 'theft_tot')
crime_2017_type('VEH_THEFT', 'veh_theft_tot')
crime_2017_type('OTHER', 'other_tot')    

crime2017 = crime2017[['homicide_tot','sex_off_total','rob_total','assault_tot','burglary_tot','vice_tot','theft_tot',
                              'veh_theft_tot','other_tot']]
crime2017 = crime2017[:1]
crime_2017_list = crime2017.values.tolist()

@app.route("/api/crimedata")
def crime_data_method():
    return jsonify(crime_list)

@app.route("/api/delinquencydata")
def delinquency_data_method():
    return jsonify(results_list)

@app.route("/api/crimePlot")
def crime_pie_method():
    return jsonify(crime_type_list)

@app.route("/api/crime2017")
def crime_2017_method():
    return jsonify(crime_2017_list)

@app.route("/")
def home():
    message = "This is a placeholder"
    #return render_template here

if __name__ == "__main__":
    app.run(debug=True)
