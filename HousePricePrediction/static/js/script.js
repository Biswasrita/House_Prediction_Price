const form = document.getElementById('predictionForm');
const result = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const sqft = document.getElementById('sqft').value;
    const bedrooms = document.getElementById('bedrooms').value;
    const bathrooms = document.getElementById('bathrooms').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ sqft, bedrooms, bathrooms })
    });

    const data = await response.json();

    if(data.prediction){
        result.innerText = `Estimated Price: $${data.prediction}`;
    } else {
        result.innerText = `Error: ${data.error}`;
    }
});
