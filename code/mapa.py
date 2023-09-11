import streamlit as st

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #faecca;
    color: black;
    height: 3em;
    width: 12em;
    border-radius:10px;
    border:3px solid #faecca;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, #faecca 5%, #f0ede6 100%);
	background-color:##faecca;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}

</style>""", unsafe_allow_html=True)

st.button("Button 1")


st.markdown('<p></p>', unsafe_allow_html = True)
st.markdown('<p></p>', unsafe_allow_html = True)
st.markdown('<p></p>', unsafe_allow_html = True)

st.button("Button 2")