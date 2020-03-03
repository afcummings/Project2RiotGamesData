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
@app.route("/")
def home():
    message = "Hello, World"
    return render_template('index.html', message=message)


### A required way of saying "Start the server"
if __name__ == "__main__":
    app.run(debug=True)