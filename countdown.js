var countDownDate = init.start * 1000;
var x = setInterval(function() {
  var now = new Date().getTime();
  if (distance < 0) {
    countDownDate = init.end * 1000;
    document.getElementById("main_text").innerHTML = "The Victoria University 2021 CTF Will end in... ";
  }
  var distance = countDownDate - now;
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  document.getElementById("demo").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
}, 1000);