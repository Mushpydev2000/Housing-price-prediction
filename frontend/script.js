document.getElementById('predict-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    // All features with default values
    let data = {
        LotArea: 8000,
        GrLivArea: 1500,
        OverallQual: 5,
        TotalBsmtSF: 800,
        GarageCars: 1,
        YearBuilt: 2000,
        YearRemodAdd: 2000,
        HouseStyle: "1Story",
        SaleCondition: "Normal",
        Neighborhood: "CollgCr"
    };
    // Get selected features and values
    const f1 = document.getElementById('feature1').value;
    const v1 = document.getElementById('value1').value;
    const f2 = document.getElementById('feature2').value;
    const v2 = document.getElementById('value2').value;
    // Set the selected features to user input (parse numbers if needed)
    const numFeatures = ["LotArea","GrLivArea","OverallQual","TotalBsmtSF","GarageCars","YearBuilt","YearRemodAdd"];
    data[f1] = numFeatures.includes(f1) ? Number(v1) : v1;
    data[f2] = numFeatures.includes(f2) ? Number(v2) : v2;
    document.getElementById('result').textContent = 'Predicting...';
    try {
        const response = await fetch('http://localhost:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify([data])
        });
        if (!response.ok) throw new Error('Network response was not ok');
        const result = await response.json();
        document.getElementById('result').textContent = 'Predicted Price: $' + result.predictions[0].toLocaleString(undefined, {maximumFractionDigits: 2});
    } catch (err) {
        document.getElementById('result').textContent = 'Error: ' + err.message;
    }
});
