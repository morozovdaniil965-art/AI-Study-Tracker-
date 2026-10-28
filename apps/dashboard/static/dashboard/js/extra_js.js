const description = document.querySelector('#subject-description');
const counter = document.querySelector('#description-counter');
const defaultIcon = document.querySelector('#default-icon');
const customIcon = document.querySelector('#custom-icon');
const imageUpload = document.querySelector('#subject-icon');
const iconOptions = document.querySelectorAll(
    'input[name="image_icon"]'
);
iconOptions.forEach(function (icon) {
    icon.addEventListener('change', function () {
        defaultIcon.checked = true;
        customIcon.checked = false;
        imageUpload.value = '';
    });
});
imageUpload.addEventListener('change', function () {
    if (imageUpload.files.length) {
        customIcon.checked = true;
        defaultIcon.checked = false;

        iconOptions.forEach(function (icon) {
            icon.checked = false;
        });
    }
});


description.addEventListener('input', function () {
    counter.textContent = `${description.value.length} / 300`;
});