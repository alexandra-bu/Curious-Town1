import streamlit as st
from random import choice

st.set_page_config(page_title="Curioustown Compass - Demo", layout="centered")

st.title("Curioustown Compass — Demo (Python / Streamlit)")
st.caption("Aplicație de learning intercultural — prototip")


with st.sidebar:
    st.header("Profil utilizator")
    name = st.text_input("Nume", "Vizitator")

tabs = st.tabs(["Istoria orașului", "Cultura actuală", "Limba universală", "Quiz rapid"])


with tabs[0]:
    st.header("Istoria Curioustown")
    st.write(
        "Lecții interactive pe hartă (demo):\n\n"
        "- Fundarea orașului\n\n"
        "- Evoluția cartierelor\n\n"
        "- Povești ale localnicilor"
    )
    if st.button("Începe lecția: ‘Povestea cartierului vechi’"):
        st.info("Deschidem lecția: poveste, hartă interactivă (simulare).")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Map_marker.svg/120px-Map_marker.svg.png", width=80)


with tabs[1]:
    st.header("Cultura orașului aplicată")
    st.write("Reguli practice pentru turiști și exemple de comportamente nedorite.")
    st.markdown("- Respectă zonele rezidențiale după ora 22:00\n- Sortează deșeurile în containerele corecte\n- Nu hrăni păsările în piețele istorice")
    st.write("Modalități de îmbunătățire:")
    st.markdown("1. Respect\n2. Înțelegere\n3. Adaptare")
    if st.checkbox("Vreau sfaturi exprimate în pași simpli"):
        st.success("Sfat: Salută localnicii în limba locală și întreabă înainte de a fotografia persoane.")


with tabs[2]:
    st.header("Limba universală — scriere & conversație")
    st.write("Modul 1: Scriere & Citire (exerciții scurte)\nModul 2: Expresii uzuale pentru conversații")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Exercițiu scriere")
        txt = st.text_area("Transcrie: 'Bună ziua, unde este gara?'", "Bună ziua, unde este gara?")
        if st.button("Verifică scrierea"):
            if "gara" in txt.lower():
                st.success("Felicitari!")
            else:
                st.error("Încearcă din nou.")
    with col2:
        st.subheader("Expresii practice")
        phrase = st.selectbox("Alege o situație", ["Salut", "Mulțumesc", "Unde e toaleta?"])
        if phrase:
            translations = {
                "Salut": "Hello / Bună",
                "Mulțumesc": "Thank you / Mulțumesc",
                "Unde e toaleta?": "Where is the restroom? / Unde e toaleta?"
            }
            st.info(translations[phrase])


with tabs[3]:
    st.header("Quiz rapid — 1 întrebare")
    q = "Ce faci dacă vezi un coș de gunoi pentru reciclare etichetat 'PLASTIC'?"
    st.write(q)
    ans = st.radio("Alege răspunsul corect:", ["Arunc hârtia acolo", "Arunc plasticul acolo", "Ignor"])
    if st.button("Verifică"):
        if ans == "Arunc plasticul acolo":
            st.success("Corect — felicitări! 🎉")
        else:
            st.error("Încearcă din nou — gândește-te ce se potrivește label-ului.")


st.markdown("---")
st.subheader("Expresia zilei (simulare widget)")
daily = [
    ("Salut!", "Hello!"),
    ("Mulțumesc!", "Thank you!"),
    ("Te rog", "Please"),
    ("Scuzați-mă", "Excuse me")
]
expr_ro, expr_en = choice(daily)
st.info(f"🇷🇴 {expr_ro}  —  🇬🇧 {expr_en}")


st.markdown("---")
st.write("Gamificare (demo):")
col_a, col_b = st.columns([3,1])
with col_a:
    st.progress(0.60)
with col_b:
    if st.button("Câștigă +10 puncte"):
        st.success("Ai primit 10 puncte! 🎖️")

st.caption("Acesta este un prototip Streamlit — pentru demo local sau testare rapidă.")
