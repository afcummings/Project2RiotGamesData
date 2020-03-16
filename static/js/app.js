// this function is run when the page loads
function main() {
    console.log("Beginning main()");
<<<<<<< HEAD
    console.log("test");    
=======
>>>>>>> 2f3db2559b6431ebd59f1905aedd01c3c9b9ddf8
    weeklyChart(); // draw the weeklyChart
    salaryTable(); // draw the salaryTable
}

// this function plots a chart of weekly data (called from main, above)
function weeklyChart() {
    d3.json("/api/weeklydata").then(rows => { // call the server.py api for weeklydata
        console.log(rows);
        let data = sqlToTrace(rows, "day", "value");
        let options = { margin: { t: 0 } };
        Plotly.newPlot("chartDiv", [data], options); // remember - plotly wants an array of data (one per trace)
    });
}

// this function plots a table of salary data (called from main, above)
function salaryTable() {
    d3.json("/api/salarydata").then(rows => { // call the server.py api for salarydata
        let tableData = [{
            type: 'table',
            header: {
                values: [["<b>EXPENSES</b>"], ["<b>Q1</b>"],
                ["<b>Q2</b>"], ["<b>Q3</b>"], ["<b>Q4</b>"]],
                align: "center",
                line: { width: 1, color: 'black' },
                fill: { color: "grey" },
                font: { family: "Arial", size: 12, color: "white" }
            },
            cells: {
                values: sqlToTable(rows),
                align: "center",
                line: { color: "black", width: 1 },
                font: { family: "Arial", size: 11, color: ["black"] }
            }
        }];

        Plotly.newPlot('tableDiv', tableData);
    });
}

// this is a utility function that rearranges the data from a SQL resultSet to x/y traces
// rows=data from sql
//   [{"age": 25, "name": "Willy"}, {"age": 57, "name": "Greg"}]
// xname=the name of the x data, ("name")
// yname = the name of the y data ("age")
// results: { x:["Willy", "Greg"], y:[25, 57] }
// NOTE: You can call this multiple times to create multiple traces
function sqlToTrace(rows, xname, yname) {  
    let x = [];
    let y = [];
    for (row of rows) {
        x.push(row[xname]);
        y.push(row[yname]);
    }
    return { x, y };
}

// this is a utility function that rearranges the data from a SQL resultSet tabular datas
// rows=data from sql, 
//   [{"age": 25, "name": "Willy"}, {"age": 57, "name": "Greg"}]
// returns a single row of HEADINGS
// and each subsequent row
//  results: [ ["name", "age"], ["Willy", 25], ["Greg", 57] ]

function sqlToTable(rows) {
    let header = [];
    let body = [];
    for (heading in rows[0]) {// getting the object keys
        header.push(heading);
    }
    body.push(header);
    for (row of rows) {
        body.push(Object.values(row))
    }
    return body;
}
<<<<<<< HEAD
new Chart(document.getElementById("donut-chart"), {
    type: 'doughnut',
    data: {
        labels: ["Homicide", "Sexual Assault", "Robbery", "Assault", "Burglary", "Vice", "Theft", "Vehicle Theft", "Other"],
        datasets: [
            {
                label: "Crime",
                backgroundColor: ["#000000", "#6495ed", "#8b008b", "#006400", "#ff1493", "#ffd700", "#8b4513", "#bdb76b", "#0000ff"],
                data: [57, 193, 426, 4099, 1102, 2132, 6598, 1337, 19693]
            }
        ]
    },
    options: {
        title: {
            display: true,
            text: 'Crime Distribution 2017-2018'
        }
    },
    centerText: {
        display: true,
        text: '980'
    }
});

new Chart(document.getElementById("doughnut-chart"), {
    type: 'doughnut',
    data: {
        labels: ["Homicide", "Sexual Assault", "Robbery", "Assault", "Burglary", "Vice", "Theft", "Vehicle Theft", "Other"],
        datasets: [
            {
                label: "Crime",
                backgroundColor: ["#000000", "#6495ed", "#8b008b", "#006400", "#ff1493", "#ffd700", "#8b4513", "#bdb76b", "#0000ff"],
                data: [62, 175, 442, 3932, 1030, 1882, 6509, 1226, 19550]
            }
        ]
    },
    options: {
        title: {
            display: true,
            text: 'Crime Distribution 2018-2019'
        }
    },
    centerText: {
        display: true,
        text: '980'
    }
});
=======
>>>>>>> 2f3db2559b6431ebd59f1905aedd01c3c9b9ddf8

main(); // initialize the page