function sendResponse(feedbackId) {
    const responseField = document.getElementById(`response-${feedbackId}`);
    const response = responseField.value;

    fetch(`/respond-to-feedback/${feedbackId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: `response=${response}`,
    })
        .then(response => response.json())
        .then(data => {
            alert('Réponse envoyée avec succès !');
            location.reload(); // Recharge la page pour afficher la réponse
        })
        .catch(error => console.error('Erreur:', error));
}
