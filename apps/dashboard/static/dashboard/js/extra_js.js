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

defaultIcon.addEventListener('change', function () {
    if (!defaultIcon.checked) {
        return;
    }

    customIcon.checked = false;
    imageUpload.value = '';
});

customIcon.addEventListener('change', function () {
    if (!customIcon.checked) {
        return;
    }

    defaultIcon.checked = false;
    iconOptions.forEach(function (icon) {
        icon.checked = false;
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


function updateDescriptionCounter() {
    counter.textContent = `${description.value.length} / 300`;
}

description.addEventListener('input', updateDescriptionCounter);
updateDescriptionCounter();
