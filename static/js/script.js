const travellersInput = document.getElementById('hotelsTravellersClass');
const travellersDropdown = document.querySelector('.travellers-dropdown');
const doneButton = document.querySelector('.submit-done');

travellersInput.addEventListener('focus', function () {
    travellersDropdown.style.display = 'block';
});

doneButton.addEventListener('click', function () {
    travellersDropdown.style.display = 'none';
});


const roomsInput = document.getElementById('hotels-rooms');
const adultInput = document.getElementById('adult-travellers');
const childrenInput = document.getElementById('children-travellers');
const decreaseRoomsButton = document.querySelector('button[data-target="#hotels-rooms"][data-value="decrease"]');
const increaseRoomsButton = document.querySelector('button[data-target="#hotels-rooms"][data-value="increase"]');
const decreaseAdultButton = document.querySelector('button[data-target="#adult-travellers"][data-value="decrease"]');
const increaseAdultButton = document.querySelector('button[data-target="#adult-travellers"][data-value="increase"]');
const decreaseChildrenButton = document.querySelector('button[data-target="#children-travellers"][data-value="decrease"]');
const increaseChildrenButton = document.querySelector('button[data-target="#children-travellers"][data-value="increase"]');

decreaseRoomsButton.addEventListener('click', function () {
    updateValue(roomsInput, -1); 
});

increaseRoomsButton.addEventListener('click', function () {
    updateValue(roomsInput, 1);
});

decreaseAdultButton.addEventListener('click', function () {
    updateValue(adultInput, -1);
});

increaseAdultButton.addEventListener('click', function () {
    updateValue(adultInput, 1);
});

decreaseChildrenButton.addEventListener('click', function () {
    updateValue(childrenInput, -1);
});

increaseChildrenButton.addEventListener('click', function () {
    updateValue(childrenInput, 1);
});


function updateValue(input, change) {
    const currentValue = parseInt(input.value);
    const newValue = currentValue + change;

    if (newValue >= 0) {
        input.value = newValue; 
    }
}