var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e.target.innerHTML;
  var lis = document.getElementsByTagName("li");
}

var removeItem = function(e) {
  e.target.remove();
}

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
	lis[i].addEventListener('mouseover', changeHeading);
	lis[i].addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!"});
  lis[i].addEventListener('click', removeItem);
}

var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
	list.appendChild(item);
  lis[i].addEventListener('mouseover', changeHeading);
	lis[i].addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!"});
  lis[i].addEventListener('click', removeItem);
}

var button = document.getElementById("b");
button.addEventListener("click", addItem);

var fib = function(n) {
    if ( n < 2 ) {
	return 1;
    } else {
	return fib(n-1) + fib(n-2);
    }
}

var fib = function(n){
  if (n == 0){
    return 0;
  }
  else if (n == 1){
    return 1;
  }
  else{
    return fib(n-1) + fib(n-2);
  }
}

var addFib = function(e) {
  console.log(e);
  var list = document.getElementById("fiblist");
  var child = list.childNodes;
  var item = document.createElement("li");
  item.innerHTML = fib(child.length - 1);
  list.appendChild(item);
}

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
