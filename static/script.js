// This function creates a new button element for each IP address and adds an event listener to it
function createButtonWithEventHandler(ipDetails) {
    let ipButton = document.createElement('button');
    // The button text shall be set as the hostname, or to the IP address if hostname is not available
    ipButton.textContent = ipDetails.hostname || ipDetails.ip;
    // Add a class to the button for styling
    ipButton.classList.add('button-spacing');

    // Add a click event listener to the button, which navigates the browser to a new URL - The ip
    ipButton.addEventListener('click', function () {
   console.log(`Button clicked, navigating to http://${ipDetails.ip}:5000/data_entry`);
   window.location.href = `http://${ipDetails.ip}:5000/data_entry`;
});;

    // The function returns the newly created button
    return ipButton;
}

// Add a click event listener to the Ping button
document.getElementById('pingButton').addEventListener('click', function () {
    // When the ping button is clicked, send a fetch request to the '/ping-ips' route on the server
    fetch('/ping-ips')
        .then(response => response.json()) // Parse the response as JSON
        .then(pingResults => {
            // Find the results div and clear it
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';

            // For each IP address in the ping results, create a new button and append it to the results div
            pingResults.forEach(ipDetails => {
                const ipButton = createButtonWithEventHandler(ipDetails);
                resultsDiv.appendChild(ipButton);
            });
        });
});