const fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let input = fs.readFileSync("example.txt").toString().trim().split("\n");
const n = input.shift() * 1;
input = input.map((v) => v.split(""));

// 배열복사
let copyInput = JSON.parse(JSON.stringify(input));

const dxy = [
  [0, -1],
  [-1, 0],
  [0, 1],
  [1, 0],
];
let answer = [];

function BFS(input, a, b, rgb) {
  let queue = [];
  queue = [[a, b]];

  while (queue.length !== 0) {
    let [x, y] = queue.shift();
    input[x][y] = 0;

    for (let xy of dxy) {
      let dx = xy[0] + x;
      let dy = xy[1] + y;

      if (dx >= 0 && dx < n && dy >= 0 && dy < n && input[dx][dy] !== 0) {
        if (input[dx][dy] == rgb) {
          queue.push([dx, dy]);
          input[dx][dy] = 0;
        } else continue;
      }
    }
  }

  return 1;
}

// 정상
let count = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (input[i][j] !== 0) {
      count += BFS(input, i, j, input[i][j]);
    }
  }
}
answer.push(count);

// 적록색약
count = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (copyInput[i][j] == "R") {
      copyInput[i][j] = "G";
    }
  }
}

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (copyInput[i][j] !== 0) {
      count += BFS(copyInput, i, j, copyInput[i][j]);
    }
  }
}
answer.push(count);

console.log(`${answer[0]} ${answer[1]}`);
