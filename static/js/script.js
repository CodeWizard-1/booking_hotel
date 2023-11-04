$(document).ready(function () {
    $(".datepicker").datepicker({
        dateFormat: "dd.mm.yy",
    });
    $(".confirm-cancel-booking").on("click", function () {
        const confirmation = confirm("Are you sure you want to cancel this booking?");
        if (confirmation) {
            const cancelButtonForm = $(this).closest(".card-body").find(".cancel-booking-form");
            if (cancelButtonForm) {
                cancelButtonForm.submit();
            }
        }
    });

    // Нажатие на кнопку "Edit Booking"
    $(".edit-booking-button").on("click", function () {
        // Откройте модальное окно для редактирования бронирования
        const bookingId = $(this).data("bookingId");
        const editModal = new bootstrap.Modal($(`#editModal${bookingId}`)[0]);
        editModal.show();
    });
});
