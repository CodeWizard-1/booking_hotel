document.addEventListener("DOMContentLoaded", function () {

    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2000);

    document.getElementById('id_check_in_date').addEventListener('change', updateTotalPrice);
            document.getElementById('id_check_out_date').addEventListener('change', updateTotalPrice);

            function updateTotalPrice() {
                var pricePerNight = parseFloat(document.getElementById('price').innerText);
                var checkInDate = new Date(document.getElementById('id_check_in_date').value);
                var checkOutDate = new Date(document.getElementById('id_check_out_date').value);

                if (!isNaN(checkInDate.getTime()) && !isNaN(checkOutDate.getTime())) {
                    var numberOfNights = Math.ceil((checkOutDate - checkInDate) / (1000 * 60 * 60 * 24));
                    var totalPrice = pricePerNight * numberOfNights;
                    document.getElementById('totalPrice').innerText = Math.max(0, totalPrice).toFixed(2);
                } else {
                    document.getElementById('totalPrice').innerText = '0';
                }
            }

    updateTotalPrice();

});