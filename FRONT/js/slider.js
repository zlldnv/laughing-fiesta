$('#ex1').slider({
    formatter: function (value) {
        return 'Current value: ' + value;
    }
});


var mySlider = $("#ex1").slider();
var value = mySlider.slider('getValue');