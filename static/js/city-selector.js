function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateCities(regionId) {
    const citySelect = document.getElementById('city');
    citySelect.disabled = true;
    citySelect.innerHTML = '<option value="">-----</option>';

    if (!regionId) {
        return;
    }
    
    fetch(`/api/cities/${regionId}/`)
        .then(response => response.json())
        .then(cities => {
            cities.forEach(city => {
                const option = document.createElement('option');
                option.value = city.id;
                option.textContent = city.name;
                citySelect.appendChild(option);
            });
            citySelect.disabled = false;
        })
        .catch(error => {
            console.error('Error fetching cities:', error);
        });
    }