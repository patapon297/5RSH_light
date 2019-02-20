$(document).ready(function () {
    var demoColorPicker = new iro.ColorPicker("#color-picker-container", {
        // Set the size of the color picker UI
        width: 320,
        height: 320,
        // Set the initial color to red
        color: "#f00"
    });

    $('.box-btn').click(function () {
        var rgb = demoColorPicker.color.rgbString;
        $(this).attr('name',rgb.replace('rgb', 'BOX ').replace('(', '').replace(')', '') + ', ' +  $(this).attr('id'));
        $(this).css('background-color', rgb);
    });
    $('#all').click(function () {
        var rgb = demoColorPicker.color.rgbString;
        $(this).attr('name' ,rgb.replace('rgb', 'RGB').replace('(', '').replace(')', ''))
    });

});
