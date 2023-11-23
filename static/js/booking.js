const idcheckinInput = document.getElementById('id_checking_date');
    const idcheckoutInput = document.getElementById('id_checkout_date');

    const startDatepicker = new Datepicker(idcheckinInput, {
        minDate: new Date(),
        autohide: true,
        datesDisabled: bookedDates,
        format: "dd/mm/yyyy"
    })
    const endDatepicker = new Datepicker(idcheckoutInput, {
        minDate: new Date(),
        autohide: true,
        datesDisabled: bookedDates,
        format: "d/m/y"
    })
