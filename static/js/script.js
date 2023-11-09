document.addEventListener("DOMContentLoaded", function () {
    const checkingDateInput = document.querySelector("#id_checking_date");
    const checkoutDateInput = document.querySelector("#id_checkout_date");

    checkingDateInput.addEventListener("change", function () {
        const selectedDate = new Date(checkingDateInput.value);
        const minDate = new Date(selectedDate);
        minDate.setDate(minDate.getDate() + 1); 

        const minDateStr = minDate.toISOString().split("T")[0];
        checkoutDateInput.min = minDateStr;
    });
});

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);