const btnSubmit = document.getElementById('regis-btn');
const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/sweetalert2@11';
document.body.appendChild(script);

script.onload = () => {
    btnSubmit.addEventListener('click', (event) => {
        event.preventDefault();

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        if (!email || !password) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Please enter email, username, and password'
            });
            return;
        }

        const data = {
            email: email,
            password: password
        };

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/register', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                const response = JSON.parse(xhr.responseText);
                if (response.status === 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'Success',
                        text: response.message,
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,
                        confirmButtonText: 'OK'
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location.href = '/login';
                        }
                    });
                } else {
                    Swal.fire({
                        icon: 'error',
                        title: 'Error',
                        text: response.message
                    });
                }
            }
        };
        xhr.send(JSON.stringify(data));
    })
}