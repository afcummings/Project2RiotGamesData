<<<<<<< HEAD
import pandas as pd
from sodapy import Socrata
from flask import Flask, jsonify, render_template


client = Socrata("data.richmondgov.com",
                 "9YLbBPExr34rv8so3YWrgKlAM")
                #username and password obscured for security reasons
                 #userame="##########",
                 #password="###########")

results = client.get("rvtv-zgyc", limit=1000)


results_df = pd.DataFrame.from_records(results)
results_df

for row in results_df.iterrows():
    print(results_df.columns)
    #print(results_df.iloc[0]['location_1'])
    
results_df = results_df.drop(results_df.columns[[0,1,2,3,4,5,6,7,9]], axis=1)
results_df = results_df.dropna(subset=["location_1"])

lat_cor = []
long_cor = []

import json
results_df["location_1"]

for index, row in results_df.iterrows():
    
    str2 = "latitude"
    str3 = "longitude"
    str4 = "human"
    
    test1 = [row['location_1']]
    test2 = json.dumps(test1)
    
   # test2 = str(test2)
   # print(type(test2))
   # print(test2)
    
    intStart = test2.find(str2)+12
    intEnd = test2.find(str3)-4
    
    intStart1=intEnd+17
    intEnd1 = test2.find(str4)-4
    
    test3 = test2[intStart1:intStart1+(intEnd1-intStart1)]
    test2 = test2[intStart:intStart+(intEnd-intStart)]
    
    
    print(test2, test3)
    lat_cor.append(test2)
    long_cor.append(test3)
    #print(test2.find(str2))
    
results_df["lat"] = lat_cor
results_df['long'] = long_cor

#csv is converted to geojson through https://www.convertcsv.com/csv-to-geojson.html

results_df = results_df.drop(results_df.columns[[0]], axis=1)
results_df.to_csv("C:\\Users\\AFCummings\\git\\Project2RiotGamesData\\Resources\\deli.csv")

results_list = results_df.values.tolist()

crime_df = pd.read_csv("C:\\Users\\AFCummings\\git\\Project2RiotGamesData\\Resources\\Crime Information.csv")
column_list = list(crime_df)
column_list.remove("NEIGHBORHOOD_NAME")
column_list.remove("Lat")
column_list.remove("Long")
print(column_list)
crime_df["sum"] = crime_df[column_list].sum(axis=1)
crime_df

crime_df = crime_df.drop(crime_df.columns[[0,1,2,3,4,5,6,7,8,9]], axis = 1)
crime_df.dropna()

crime_list = crime_df.values.tolist()

crime_by_type = pd.read_csv("C:\\Users\\AFCummings\\git\\Project2RiotGamesData\\Resources\\Crime Information.csv")

crime_by_type = crime_by_type.drop(crime_by_type.columns[[0,10,11]], axis=1)
crime_by_type

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

crime_by_type
crime_by_type = crime_by_type[['homicide_tot','sex_off_total','rob_total','assault_tot','burglary_tot','vice_tot','theft_tot',
                              'veh_theft_tot','other_tot']]
crime_by_type = crime_by_type[:1]
crime_type_list = crime_by_type.values.tolist()

crime2017 = pd.read_csv("C:\\Users\\AFCummings\\git\\Project2RiotGamesData\\Resources\\Crime Information2017-2018.csv")

crime2017 = crime2017.drop(crime2017.columns[[0]], axis=1)
crime2017

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

=======
from flask import Flask, jsonify, render_template

### create a flask instance
app = Flask(__name__)

someWeeklyPerformanceData = [
    {"day": "Sunday", "value": 15339},
    {"day": "Monday", "value": 21345},
    {"day": "Tuesday", "value": 18483},
    {"day": "Wednesday", "value": 24003},
    {"day": "Thursday", "value": 23489},
    {"day": "Friday", "value": 24092},
    {"day": "Saturday", "value": 12034}
]

theDataForSalaries = [
        {'Salaries':1200000, 'Office':20000, 'Merchandise':80000, 'Legal':2000, 'Total':12120000},
        {'Salaries':1300000, 'Office':20000, 'Merchandise':70000, 'Legal':2000, 'Total':130902000},
        {'Salaries':1300000, 'Office':20000, 'Merchandise':120000, 'Legal':2000, 'Total':131222000},
        {'Salaries':1400000, 'Office':20000, 'Merchandise':90000, 'Legal':2000, 'Total':14102000},
]

### one of your APIs
@app.route("/api/weeklydata")
def the_Weekly_Data_Method():
    return jsonify(someWeeklyPerformanceData)

### another potential API
@app.route("/api/salarydata")
def the_Method_for_some_Salary_Data():
    return jsonify(theDataForSalaries)

### the 'home' route. 
### NOTE: This allows sending data to the HTML through templating
## But you'll likely not need it since most of what you're doing is AJAX APIs
>>>>>>> 2f3db2559b6431ebd59f1905aedd01c3c9b9ddf8
@app.route("/")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)
<<<<<<< HEAD
@app.route("/pie.html")
def pie_method():
    message = "Hello, World"
    return render_template('pie.html', message=message)
@app.route("/map.html")
def map_method():
    message = "Hello World"
    return render_template('map.html', message=message)

#ideally these would have been used for JS
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

### A required way of saying "Start the server"
if __name__ == "__main__":
    app.run(debug=True)
=======


### A required way of saying "Start the server"
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 2f3db2559b6431ebd59f1905aedd01c3c9b9ddf8
