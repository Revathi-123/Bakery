/**
 * Created by suhasjadhav on 17/6/15.
 */
var red = [0, 100, 63];
var orange = [40, 100, 60];
var green = [75, 100, 40];
var blue = [196, 77, 55];
var purple = [280, 50, 60];

var myName = "rEc$corE";
letterColors = [red, black,purple,green  ]


//if(15 > 3) {
//    bubbleShap = "square";
//}
//else {
    bubbleShape = "circle   ";
//}

drawName(myName, letterColors);
bounceBubbles()

$(document).ready(function(){
    $('.collapsible').collapsible({
      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });
  });