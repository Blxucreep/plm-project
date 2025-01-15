function prepareChart() {
    const xAxis = document.getElementById('x-axis').value;
    const yAxis = document.getElementById('y-axis').value;

    // combinations that are valid
    const validCombinations = [
        { x: 'time', y: 'ventes' },
        { x: 'time', y: 'prix_moyen' },
        { x: 'status', y: 'number' },
    ];

    const isValidCombination = validCombinations.some(combination => 
        combination.x === xAxis && combination.y === yAxis
    );

    if (isValidCombination) {
        alert(`Generating chart for X: ${xAxis} and Y: ${yAxis}`);
        window.location.href = `/dashboard/?x-axis=${xAxis}&y-axis=${yAxis}`;
    } else {
        alert('Invalid combination');
    }
}
