'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the minimumSwaps function below.
function minimumSwaps(arr) {
    var switchs = 0;
    var iterable = 0;

    for (var ii = 1; ii < arr.length; ii++){
        if(arr[ii - 1] == ii) {
            continue;
        }
        else {
            const memo = arr[ii - 1];
            const ii_index = arr.indexOf(ii);
            arr[ii - 1] = arr[ii_index];
            arr[ii_index] = memo;
            switchs++;
        }
    }

    return switchs
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    // const arr = [2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19]
    const res = minimumSwaps(arr);

    // console.log(res)
    ws.write(res + '\n');

    ws.end();
}

// main()
