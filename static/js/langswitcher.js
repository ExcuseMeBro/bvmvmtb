document.addEventListener('DOMContentLoaded', function () {
    const dropdownLinks = document.querySelectorAll('.langswitcher');
    const form = document.querySelector('.language-form');
    const languageInput = document.getElementById('language-input');
    const toggleText = document.querySelector('.nav-menu');

    dropdownLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault(); // Prevent default anchor behavior
            const languageCode = this.getAttribute('data-language');
            const languageName = this.textContent.trim();

            // Update hidden input with selected language code
            languageInput.value = languageCode;

            // Optionally update toggle text to reflect selection (visual feedback)
            toggleText.textContent = languageName;

            // Submit the form to change the language
            form.submit();
        });
    });
});