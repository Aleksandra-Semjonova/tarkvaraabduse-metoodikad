import streamlit as st
import random
import datetime

st.set_page_config(page_title="Uudistegeneraator", layout="centered")

st.title("Uudistegeneraator")

uudised = {
    "Tehnoloogia": [
        "Apple esitles uut Vision Pro mudelit.",
        "Eesti tudengid lõid isejuhtiva drooni.",
        "Tehisintellekt kirjutab ise luuletusi."
    ],
    "Spordiuudised": [
        "Ott Tänak tuli taas esikohale.",
        "Eesti korvpallikoondis pääses finaali.",
        "Noor maratonijooksja püstitas rekordi."
    ],
    "Majandus": [
        "Nafta hind langes 10% võrra.",
        "Eesti idufirma sai miljoni euro investeeringu.",
        "Töötuse määr püsib stabiilne."
    ]
}

if "kasutaja_uudised" not in st.session_state:
    st.session_state.kasutaja_uudised = {
        "Tehnoloogia": [],
        "Spordiuudised": [],
        "Majandus": []
    }


def genereeri_kuupaev():
    täna = datetime.date.today()
    juhuslik_paev = täna - datetime.timedelta(days=random.randint(0, 6))
    return juhuslik_paev.strftime("%d.%m.%Y")

kategooria = st.selectbox("Vali kategooria:", list(uudised.keys()))


if st.button("Genereerida"):
    st.subheader("Genereeritud uudised:")
    kogu_list = uudised[kategooria] + st.session_state.kasutaja_uudised[kategooria]
    valitud_uudised = random.sample(kogu_list, min(3, len(kogu_list)))
    for u in valitud_uudised:
        st.write(f"{genereeri_kuupaev()} - {u}")
