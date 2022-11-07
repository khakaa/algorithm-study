let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

const N = +input.shift();
input = input.map(Number);
input.unshift(0);

function solution() {
  let dp = new Array(N).fill(0);

  dp[1] = input[1];
  dp[2] = input[1] + input[2];

  for (let i = 3; i <= N; i++) {
    dp[i] = Math.max(dp[i - 2] + input[i], dp[i - 3] + input[i - 1] + input[i]);
  }

  return dp[N];
}

console.log(solution());
