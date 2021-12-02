const fs = require('fs')
const inputPath = '/Users/korbinianschleifer/desktop/advent-of-code-2021/inputs/'
const filename = 'day1.txt'

fs.readFile( inputPath + filename, 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  data = data.split("\n").map(Number);

  // Part 1
  numberOfSingleIncreases = countNumberOfIncreases(data)
  console.log("first solution: " + numberOfSingleIncreases)

  // Part 2
  threeMeasurements = []
  for (let i = 2; i < data.length; i++) {
      threeMeasurements.push(data[i-2] + data[i-1] + data[i])
  }

  secondSolution = countNumberOfIncreases(threeMeasurements)
  console.log("second solution: " + secondSolution)
})

function countNumberOfIncreases(arr) {
    result = 0
    for (let i = 1; i < arr.length; i++ ) {
        if (arr[i-1] < arr[i]) {
            result++
        }
    }
    return result
}
