const fs = require('fs')

const filename = 'day1.txt'

fs.readFile('/Users/korbinianschleifer/desktop/advent-of-code-2021/inputs/' + filename, 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  data = data.split("\n")
  increased_counter = 0
  for (let i = 1; i < data.length; i++ ) {
      if (data[i-1] > data[i]) {
          increased_counter++
      }
  }
  console.log("first solution:" increased_counter)
})
