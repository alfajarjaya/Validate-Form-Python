const btnSubmit = document.getElementById('submit');
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
                text: 'Please enter email and password'
            });
            return;
        }

        const data = {
            email: email,
            password: password
        };

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/login', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                try {
                    const response = JSON.parse(xhr.responseText);
                    if (response.status === 'success' && xhr.status === 200) {
                        window.location.href = '/dashboard';
                    } else {
                        Swal.fire({
                            icon: 'error',
                            title: 'Error',
                            text: response.message
                        });
                    }
                } catch (e) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Error',
                        text: 'Error processing response'
                    });
                }
            }
        };
        xhr.send(JSON.stringify(data));
    });
};
