const description = document.querySelector('#subject-description');
const counter = document.querySelector('#description-counter');

description.addEventListener('input', function () {
    counter.textContent = `${description.value.length} / 300`;
});