import pandas as pd
import streamlit as st

# Chargement des données
@st.cache_data  # Mise en cache pour optimiser la lecture
def load_data():
    data_path = "data/avocado.csv"
    try:
        df = pd.read_csv(data_path)
        return df
    except FileNotFoundError:
        st.error("Fichier non trouvé. Veuillez vérifier le chemin vers 'avocado.csv'.")
        return None

# Fonction pour calculer le prix moyen
def calculate_avg_price(df, region, total_volume, avocado_type, year):
    filtered_df = df[
        (df["region"].str.lower() == region.lower()) &
        (df["type"].str.lower() == avocado_type.lower()) &
        (df["year"] == year)
    ]
    if filtered_df.empty:
        st.warning("Aucune donnée trouvée pour les critères sélectionnés.")
        return None
    else:
        avg_price = filtered_df["AveragePrice"].mean()
        return avg_price

# Interface Streamlit
def main():
    st.title("Prédiction du Prix Moyen des Avocats 🥑")
    st.write("Veuillez entrer les informations nécessaires pour obtenir le prix moyen.")

    # Chargement des données
    df = load_data()
    if df is not None:
        # Entrées utilisateur
        region = st.text_input("Région :", value="Albany")
        total_volume = st.number_input("Total Volume :", min_value=0.0, step=0.1)
        avocado_type = st.selectbox("Type d'avocat :", options=["conventional", "organic"])
        year = st.number_input("Année :", min_value=2015, max_value=2022, step=1, value=2015)

        # Bouton de soumission
        if st.button("Calculer le Prix Moyen"):
            avg_price = calculate_avg_price(df, region, total_volume, avocado_type, year)
            if avg_price is not None:
                st.success(f"Le prix moyen pour les critères sélectionnés est de : **{avg_price:.2f} $**")

        # Affichage des données pour vérification
        if st.checkbox("Afficher les données brutes"):
            st.dataframe(df)

if __name__ == "__main__":
    main()
