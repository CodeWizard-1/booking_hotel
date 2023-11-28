document.addEventListener("DOMContentLoaded", function () {

    const today = new Date();

    const isoDate = today.getDate().toString().padStart(2, '0') + '-' + (today.getMonth() + 1).toString().padStart(2, '0') + '-' + today.getFullYear();
    const checkinInput = document.getElementById('checkin');
    const checkoutInput = document.getElementById('checkout');
    
    flatpickr(checkinInput, {
        enableTime: false,
        dateFormat: 'd-m-Y',
        minDate: today,
        defaultDate: today,
    });
    
    flatpickr(checkoutInput, {
        enableTime: false,
        dateFormat: 'd-m-Y',
        minDate: today,
        defaultDate: today,
    });
    
});