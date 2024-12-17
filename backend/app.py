import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Charger les données
def load_data():    
    data_path = "backend/data/avocado.csv"
    df = pd.read_csv(data_path)
    return df

# Route API pour calculer le prix moyen
@app.route('/calculate_price', methods=['POST'])
def calculate_price():
    # Charger les données
    df = load_data()    

    # Récupérer les données envoyées par l'utilisateur
    data = request.get_json()
    
    # Extraire les champs requis
    filters = {
        "Date": data.get("Date"),
        "Total Volume": data.get("Total Volume"),
        "4046": data.get("4046"),
        "4225": data.get("4225"),
        "4770": data.get("4770"),
        "Total Bags": data.get("Total Bags"),
        "Small Bags": data.get("Small Bags"),
        "Large Bags": data.get("Large Bags"),
        "XLarge Bags": data.get("XLarge Bags"),
        "type": data.get("type"),
        "year": data.get("year"),
        "region": data.get("region"),
    }
    
    # Filtrer les données
    filtered_df = df.copy()
    for key, value in filters.items():
        if value is not None:  # Appliquer le filtre uniquement si une valeur est fournie
            if isinstance(value, str):
                filtered_df = filtered_df[filtered_df[key].str.lower() == value.lower()]
            else:
                filtered_df = filtered_df[filtered_df[key] == value]

    if filtered_df.empty:
        return jsonify({"error": "Aucune donnée trouvée pour les critères fournis."}), 400
    
    # Calculer le prix moyen
    avg_price = filtered_df["AveragePrice"].mean()
    return jsonify({"average_price": round(avg_price, 2)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
