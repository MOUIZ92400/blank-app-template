import streamlit as st

st.set_page_config(page_title="ERP SASU", layout="centered")
st.title("📊 Mon ERP SASU Mobile")

menu = st.sidebar.selectbox("Menu", ["Stock", "Ventes", "Paramètres"])

if menu == "Stock":
    st.subheader("📦 Gestion du Stock")
    with st.form("ajout"):
        nom = st.text_input("Produit")
        qte = st.number_input("Quantité", min_value=0)
        prix = st.number_input("Prix d'achat (€)", min_value=0.0)
        if st.form_submit_button("Enregistrer"):
            st.success(f"Enregistré : {nom}")
