// Kelvin Ng
// SoftDev1 pd1
// K27 -- Sequential Progression
// 2019-12-10

function fib(n) {
  a = 1;
  b = 0;
  var temp;

  while (n-1 >= 0){
    temp = a;
    a = a + b;
    b = temp;
    n--;
  }

  return b;
}

function gcd(a,b) {
  while(b) {
    var x = b;
    b = a % b;
    a = x;
  }

  return a;
}

function randStu() {
  var students = ['bob', 'kelvin', 'hi', 'yeet', 'pepega'];
  return students[Math.floor(Math.random() * 1000 % students.length)];
}
