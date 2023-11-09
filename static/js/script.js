$(document).ready(function () {
    $(".datepicker").datepicker({
        dateFormat: "dd.mm.yy",
    });
});

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);