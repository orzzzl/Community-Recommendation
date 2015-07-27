/**
 * Created by zelengzhuang on 7/26/15.
 */
$("#eating").slider({
	tooltip: 'always'
});
$("#eating").on("slide", function (slideEvt) {
    $("#eatingSliderVal").text(slideEvt.value);
});

$("#shopping").slider({
	tooltip: 'always'
});
$("#shopping").on("slide", function (slideEvt) {
    $("#eatingSliderVal").text(slideEvt.value);
});
$("#health").slider({
	tooltip: 'always'
});
$("#health").on("slide", function (slideEvt) {
    $("#eatingSliderVal").text(slideEvt.value);
});

$("#school").slider({
	tooltip: 'always'
});
$("#school").on("slide", function (slideEvt) {
    $("#eatingSliderVal").text(slideEvt.value);
});

$("#security").slider({
	tooltip: 'always'
});
$("#security").on("slide", function (slideEvt) {
    $("#eatingSliderVal").text(slideEvt.value);
});

$("#transportation").slider({
	tooltip: 'always'
});
$("#transportation").on("slide", function (slideEvt) {
    $("#eatingSliderVal").text(slideEvt.value);
});
