import streamlit as st
import requests

# URL de l'API Flask
API_URL = "http://127.0.0.1:5000/calculate_price"

def main():
    st.title("Prédiction du Prix Moyen des Avocats 🥑")
    st.write("Entrez les informations nécessaires pour obtenir le prix moyen.")

    # Formulaire pour entrer les champs
    date = st.text_input("Date (ex: 2015-12-27) :", value="")
    total_volume = st.number_input("Total Volume :", min_value=0.0, step=0.1)
    vol_4046 = st.number_input("4046 :", min_value=0.0, step=0.1)
    vol_4225 = st.number_input("4225 :", min_value=0.0, step=0.1)
    vol_4770 = st.number_input("4770 :", min_value=0.0, step=0.1)
    total_bags = st.number_input("Total Bags :", min_value=0.0, step=0.1)
    small_bags = st.number_input("Small Bags :", min_value=0.0, step=0.1)
    large_bags = st.number_input("Large Bags :", min_value=0.0, step=0.1)
    xlarge_bags = st.number_input("XLarge Bags :", min_value=0.0, step=0.1)
    avocado_type = st.selectbox("Type d'avocat :", ["", "conventional", "organic"])
    year = st.number_input("Année :", min_value=2015, max_value=2022, step=1)
    region = st.text_input("Région :", value="")

    # Bouton pour calculer
    if st.button("Calculer le Prix Moyen"):
        # Préparer les données pour la requête POST
        payload = {
            "Date": date,
            "Total Volume": total_volume if total_volume else None,
            "4046": vol_4046 if vol_4046 else None,
            "4225": vol_4225 if vol_4225 else None,
            "4770": vol_4770 if vol_4770 else None,
            "Total Bags": total_bags if total_bags else None,
            "Small Bags": small_bags if small_bags else None,
            "Large Bags": large_bags if large_bags else None,
            "XLarge Bags": xlarge_bags if xlarge_bags else None,
            "type": avocado_type,
            "year": int(year) if year else None,
            "region": region,
        }

        # Envoi de la requête POST à l'API
        response = requests.post(API_URL, json=payload)

        # Affichage des résultats
        if response.status_code == 200:
            avg_price = response.json().get("average_price")
            st.success(f"Le prix moyen est : **{avg_price} $**")
        else:
            error_message = response.json().get("error")
            st.error(f"Erreur : {error_message}")

if __name__ == "__main__":
    main()
