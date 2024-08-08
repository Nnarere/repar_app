
document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('addForm');

    formulario.addEventListener('submit', function(event) {
        event.preventDefault();

        alert('Vehicle information has been added');

        formulario.submit();
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const userSignIn = document.getElementById('register');

    userSignIn.addEventListener('submit', function(event) {
        event.preventDefault();

        alert('Registered successfully');

        userSignIn.submit();
    });
});
