function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function myFunctionCount() {
          document.getElementById("demo").innerHTML = "Started Counting";
          console.log(new Date());
          console.log('Dude!');
          sleep(1000);
          console.log(new Date());
          document.getElementById("demo").innerHTML = "2570$";
}

function myFunctionStopCount() {
          document.getElementById("demo").innerHTML = "STOP counting";
}
