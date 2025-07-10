document.getElementById('predict-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = {
        LotArea: parseFloat(form.LotArea.value),
        GrLivArea: parseFloat(form.GrLivArea.value),
        OverallQual: parseInt(form.OverallQual.value),
        TotalBsmtSF: parseFloat(form.TotalBsmtSF.value),
        GarageCars: parseInt(form.GarageCars.value),
        YearBuilt: parseInt(form.YearBuilt.value),
        YearRemodAdd: parseInt(form.YearRemodAdd.value),
        HouseStyle: form.HouseStyle.value,
        SaleCondition: form.SaleCondition.value,
        Neighborhood: form.Neighborhood.value
    };
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
