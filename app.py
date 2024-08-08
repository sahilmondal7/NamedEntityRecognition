import streamlit as st
import spacy
import subprocess
from spacy import displacy
from spacy.util import get_package_path


try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    st.info("Downloading the spaCy model. This will only happen once.")
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_lg"])
    nlp = spacy.load("en_core_web_lg")
    

st.set_page_config(page_title="Named Entity Recognition", page_icon="https://explosion.gallerycdn.vsassets.io/extensions/explosion/spacy-extension/1.0.1/1685718946744/Microsoft.VisualStudio.Services.Icons.Default")

with st.container():
    left_column, right_column = st.columns((2,1))

    with left_column:
        st.title("Named Entity Recognition with :blue[spaCy]")

    with right_column:
        st.image("https://explosion.gallerycdn.vsassets.io/extensions/explosion/spacy-extension/1.0.1/1685718946744/Microsoft.VisualStudio.Services.Icons.Default")

user_input = st.text_input("Enter a sentence or paragraph:")

doc = nlp(user_input)


if st.button("Click Me To Highlight The Entities In Your Input"):
    html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown("## Here's Your Result!!")
    st.markdown(html, unsafe_allow_html=True)
    st.markdown("###")
    st.write(":red[The model is not 100% accurate. Consider rechecking.]")


st.markdown("##")
st.write("### Reference For Named Entities:")
st.write("""**PERSON** - People, including fictional.

**NORP** - Nationalities or religious or political groups.

**FAC** - Buildings, airports, highways, bridges, etc.

**ORG** - Companies, agencies, institutions, etc.

**GPE** - Countries, cities, states.

**LOC** - Non-GPE locations, mountain ranges, bodies of water.

**PRODUCT** - Objects, vehicles, foods, etc. (Not services.)

**EVENT** - Named hurricanes, battles, wars, sports events, etc.

**WORK_OF_ART** - Titles of books, songs, etc.

**LAW** - Named documents made into laws.

**LANGUAGE** - Any named language.

**DATE** - Absolute or relative dates or periods.

**TIME** - Times smaller than a day.

**PERCENT** - Percentage, including "%".

**MONEY** - Monetary values, including unit.

**QUANTITY** - Measurements, as of weight or distance.

**ORDINAL** - "first", "second", etc.

**CARDINAL** - Numerals that do not fall under another type.""")
