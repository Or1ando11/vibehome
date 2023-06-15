document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('contact-form');
    var successMessage = document.getElementById('success-message');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Zatrzymujemy domyślne działanie formularza
        
        var formData = new FormData(form);
        
        fetch(form.action, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                form.reset();  // Resetujemy zawartość formularza
                successMessage.textContent = data.message;
                successMessage.style.display = 'block';
                setTimeout(function() {
                    successMessage.style.display = 'none';
                }, 5000);  // Wyświetlamy wiadomość przez 5 sekund
            } else if (data.errors) {
                // Obsługa błędów, jeśli wystąpią
            }
        })
        .catch(error => {
            console.error('Wystąpił błąd:', error);
        });
    });
});