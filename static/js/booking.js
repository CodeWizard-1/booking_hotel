
const today = new Date();

// const isoDate = today.getDate().toString().padStart(2, '0') + '-' + (today.getMonth() + 1).toString().padStart(2, '0') + '-' + today.getFullYear();

const idcheckinInput = document.getElementById('id_checking_date');
const idcheckoutInput = document.getElementById('id_checkout_date');


idcheckinInput.addEventListener('changeDate', updateTotalPrice);
idcheckoutInput.addEventListener('changeDate', updateTotalPrice);

function updateTotalPrice() {
    const pricePerNight = parseFloat(document.getElementById('price').innerText);
    const checkInDate = new Date(idcheckinInput.value);
    const checkOutDate = new Date(idcheckoutInput.value);

    if (!isNaN(checkInDate.getTime()) && !isNaN(checkOutDate.getTime())) {
        const numberOfNights = Math.ceil((checkOutDate - checkInDate) / (1000 * 60 * 60 * 24));
        const totalPrice = pricePerNight * numberOfNights;
        document.getElementById('totalPrice').innerText = Math.max(0, totalPrice).toFixed(0);
    } else {
        document.getElementById('totalPrice').innerText = '0';
    }
}


updateTotalPrice();

// const startDatepicker = new Datepicker(idcheckinInput, {
//     minDate: new Date(),
//     autohide: true,
//     datesDisabled: bookedDates,
//     defaultViewDate: 'today', 
//     todayButton: true,
//     format: 'dd/mm/yyyy',
// });

// const endDatepicker = new Datepicker(idcheckoutInput, {
//     minDate: new Date(),
//     autohide: true,
//     datesDisabled: bookedDates,
//     defaultViewDate: 'today', 
//     todayButton: true,
//     format: 'dd/mm/yyyy',
// });



const startDatepicker = new flatpickr(idcheckinInput, {
    enableTime: false,
    altInput: true,
    altFormat: "d-m-Y",
    dateFormat: "Y-m-d",
    minDate: today,
    defaultDate: today,
    disable: bookedDates,
});

const endDatepicker = new flatpickr(idcheckoutInput, {
    enableTime: false,
    altInput: true,
    altFormat: "d-m-Y",
    dateFormat: "Y-m-d",
    minDate: today,
    defaultDate: today,
    disable: bookedDates,
});