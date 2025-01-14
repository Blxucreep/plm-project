function updateQuantity(supplierId, action) {
    const quantityElement = document.getElementById(`quantity-${supplierId}`);

    fetch(`/update-quantity/${supplierId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: `action=${action}`,
    })
        .then(response => response.json())
        .then(data => {
            quantityElement.textContent = data.quantity;
        })
        .catch(error => console.error('Erreur:', error));
}

function saveOrderDate(supplierId) {
    const dateInput = document.getElementById(`order-date-${supplierId}`);

    fetch(`/update-order-date/${supplierId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: `next_order_date=${dateInput.value}`,
    })
        .then(response => response.json())
        .then(data => {
            alert('Date mise à jour avec succès');
        })
        .catch(error => console.error('Erreur:', error));
}
