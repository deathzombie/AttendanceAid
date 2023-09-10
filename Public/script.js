document.addEventListener('DOMContentLoaded', () => {
    const userForm = document.getElementById('userForm');

    userForm.addEventListener('submit', async(event) => {
        event.preventDefault(); // Prevent the default form submission

        const name = document.getElementById('name').value;
        const rollNumber = document.getElementById('rollNumber').value;
        const lmsId = document.getElementById('lmsId').value;
        const lmsPassword = document.getElementById('lmsPassword').value;
        const branch = document.getElementById('branch').value;
        const subgroup = document.getElementById('subgroup').value;

        const data = {
            name,
            rollNumber,
            lmsId,
            lmsPassword,
            branch,
            subgroup
            // Add more fields as needed
        };

        const response = await fetch('/store', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data), // Send data as JSON
        });

        if (response.ok) {
            window.location.href = '/thankyou.html'; // Redirect to the thank you page
        } else {
            alert('Error saving data');
        }
    });
});
