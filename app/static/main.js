$(document).ready(function() {
    /*var scene = document.getElementById('scene');
    var parallaxInstance = new Parallax(scene);*/

    $("#datepicker").datepicker({
        showOn: "both",
        buttonImageOnly: true,
        buttonImage: "calendar.gif",
        buttonText: "Calendar",
        minDate: new Date(),
        onSelect: date => {
            alert(date);
            $('#datepicker').datepicker('setDate', null);
        }
    });




});