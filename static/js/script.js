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
    });;




    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2000);

    document.getElementById('id_check_in_date').addEventListener('change', updateTotalPrice);
    document.getElementById('id_check_out_date').addEventListener('change', updateTotalPrice);

    function updateTotalPrice() {
        const pricePerNight = parseFloat(document.getElementById('price').innerText);
        const checkInDate = new Date(document.getElementById('id_check_in_date').value);
        const checkOutDate = new Date(document.getElementById('id_check_out_date').value);

        if (!isNaN(checkInDate.getTime()) && !isNaN(checkOutDate.getTime())) {
            const numberOfNights = Math.ceil((checkOutDate - checkInDate) / (1000 * 60 * 60 * 24));
            const totalPrice = pricePerNight * numberOfNights;
            document.getElementById('totalPrice').innerText = Math.max(0, totalPrice).toFixed(0);
        } else {
            document.getElementById('totalPrice').innerText = '0';
        }
    }

    updateTotalPrice();

    

});