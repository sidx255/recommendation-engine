// Requiring Modules
const express = require('express');
const bodyParser = require('body-parser');
const ejs = require('ejs');
const { spawn } = require('child_process');

// Declaring constants
const PORT = process.env.PORT || 3000;
const app = express();

//python------------
// var dataString='';
// pyProcess.stdout.on('data', function(data) {
//   dataString+=data.toString();
//   console.log(dataString);
// });
// pyProcess.stdout.on('end', function(data) {
//   var recom = dataString.split(/[,]+/);
//   console.log(recom);
// });

//-----------------


// App Configurations
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(express.static('public'));

// Home route
app.get('/', (req,res)=>{
  res.render('dashboard', {result: "", query: "", precision: "", recall:""});
});

app.post('/',(req,res)=>{
  var query = req.body.searchValue;
  // Sending input to python script
  const pyProcess = spawn('python', ['test.py']);
  pyProcess.stdin.write(JSON.stringify(query));
  pyProcess.stdin.end();

  // Getting result from python script
  var dataString='';
  pyProcess.stdout.on('data', function(data) {
    dataString+=data.toString();
  });
  pyProcess.stdout.on('end', function(data) {
    //converting result to array of strings
    var recom = dataString.split(/[,]+/);

    //passing result
    var result = {recommendations:recom};
    var precision = 0.8;
    var recall = 0.75;
    res.render('dashboard', {result: result, query: query, precision: precision, recall:recall});
  });
});

// Server Set-up
app.listen(PORT, ()=>{
  console.log("Server Running at Port: " + PORT);
});
