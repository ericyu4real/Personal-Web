var exec = require('child_process').exec;

exec('python3 python.py 15 7 100',
    function (error, stdout, stderr) {
        console.log('stdout: ' + stdout);
        console.log('stderr: ' + stderr);
        if (error !== null) {
             console.log('exec error: ' + error);
        }
    });


// const spawner = require('child_process').spawn;

// const data_to_pass_in = "send this to python script";

// console.log('Data sent to python script:', data_to_pass_in)

// const python_process = spawner('python', ['./python.py', data_to_pass_in]);

// python_process.stdout.on('data', (data) => {
//     console.log("Data received from python dscript:", data.toString());
// });