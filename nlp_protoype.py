import streamlit as st
import spacy
from spacy import displacy


#load model
@st.cache_resource
def load_nlp():
    return spacy.load("de_core_news_lg")


nlp = load_nlp()

st.title("Prototype NLP")
st.markdown("Gib einen einfachen Text ein und erhalte eine Kategorisierung in Personen und Organisationen.")

#input
cv_text = st.text_area("Gib deinen Text hier ein:",
                       "Maurice studiert in Oldenburg. Max arbeitet seit vier Jahren bei Tesla in den USA. Margarete arbeitet bei der ARD in Hamburg. ",
                       height=200)

if st.button("Analysieren"):

    doc = nlp(cv_text)

    st.subheader("Ergbenisse:")

    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.write(ent_html, unsafe_allow_html=True)

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Personen:**")
        names = [ent.text for ent in doc.ents if ent.label_ == "PER"]
        st.write(names if names else "Keine gefunden")

    with col2:
        st.write("**Organisationen:**")
        orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
        st.write(orgs if orgs else "Keine gefunden")