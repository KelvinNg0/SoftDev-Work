var changeHeading = function(e) { // changes heading from Hello World! to what is mouseover
  var h = document.getElementById("h");
  h.innerHTML = e.target.innerHTML;
  var lis = document.getElementsByTagName("li");
}

var removeItem = function(e) { // removes item from list and changes heading
  e.target.remove();
  document.getElementById("h").innerHTML = "Hello World!";
}

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) { // for every item in list, it allows removal of item and change of heading
	lis[i].addEventListener('mouseover', changeHeading);
	lis[i].addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!"});
  lis[i].addEventListener('click', removeItem);
}

var addItem = function(e) { // adds an item to the list
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
	list.appendChild(item);
  item.addEventListener('mouseover', changeHeading);
	item.addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!"});
  item.addEventListener('click', removeItem);
}

var button = document.getElementById("b");
button.addEventListener("click", addItem);

var fib = function(n) { // calculates fib sequence
    if ( n < 2 ) {
	return 1;
    } else {
	return fib(n-1) + fib(n-2);
    }
}

var addFib = function(e) { // adds next fib # to list
  console.log(e);
  var list = document.getElementById("fiblist");
  var child = list.childNodes;
  var item = document.createElement("li");
  item.innerHTML = fib(child.length - 1);
  list.appendChild(item);
}

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
