$(document).ready(function () {
    var demoColorPicker = new iro.ColorPicker("#color-picker-container", {
        // Set the size of the color picker UI
        width: 250,
        height: 250,
        // Set the initial color to red
        color: "#f00"
    });

    $('.field').click(function () {
        num = $(this).attr('id').replace('field-', '');
        $('#' + num).click();
        var rgb = demoColorPicker.color.rgbString;
        $(this).css('background-color', rgb);
    });

    $('.box-btn').click(function () {
        var rgb = demoColorPicker.color.rgbString;
        $(this).attr('name',rgb.replace('rgb', 'BOX ').replace('(', '').replace(')', '') + ', ' +  $(this).attr('id'));

    });
    $('#all').click(function () {
        var rgb = demoColorPicker.color.rgbString;
        $(this).attr('name' ,rgb.replace('rgb', 'RGB').replace('(', '').replace(')', ''))
    });

    $('#field-all').click(function () {
        var rgb = demoColorPicker.color.rgbString;
        $('.field').css('background-color', rgb);
    });

});
