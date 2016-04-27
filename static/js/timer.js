var seconds = {{seconds}};
function timer() {
    var days        = Math.floor(seconds/24/60/60);
    var hoursLeft   = Math.floor((seconds) - (days*86400));
    var hours       = Math.floor(hoursLeft/3600);
    var minutesLeft = Math.floor((hoursLeft) - (hours*3600));
    var minutes     = Math.floor(minutesLeft/60);
    var remainingSeconds = seconds % 60;
    if (remainingSeconds < 10) {
        remainingSeconds = "0" + remainingSeconds; 
    }
    document.getElementById('timer').innerHTML = "Time Remaining: " + hours + ":" + minutes + ":" + remainingSeconds.toFixed(0);
    if (seconds == 0) {
        clearInterval(countdownTimer);
        document.getElementById('timer').innerHTML = "Done! Go get some rest!";
    } else {
        seconds--;
    }
}
var countdownTimer = setInterval('timer()', 1000);