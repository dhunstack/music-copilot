import streamlit as st
import music21 as m21
import tempfile
from abcsonification.sonifyabc import sonify_all_files
import os
import subprocess
from enum import Enum, IntEnum
from pydantic import BaseModel, ValidationError


class KeyEnum(str, Enum):
    Aminor = 'Amin'
    banana = 'banana'


def get_transformer_prompt():
    with open('tunesformer/prompt.txt') as f:
        return f.read()
    
def get_generated_abc():
    with open('sounds_current/placeholder.abc') as f:
        return f.read()
    
def display_sheet_music(score):
    # Save the sheet music as an image
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as img_file:
        img_path = score.write('musicxml.png', fp=img_file.name)

    # Display the sheet music image
    st.image(str(img_path), caption="Sheet Music")

def run_transformer():
    ## Run the transformer
    os.chdir('./tunesformer')
    command1 = [
        'python',
        'generate.py'
    ]
    subprocess.run(command1)
    os.chdir('../')
    st.session_state.trans_prompt = get_transformer_prompt()
    st.session_state.gen_abc = get_generated_abc()

if ["inter_prompt", "abc_string", "old_score"]  not in st.session_state:
    st.session_state.trans_prompt = get_transformer_prompt()
    st.session_state.gen_abc = get_generated_abc()
    st.session_state.old_score = []

# Main page Headers
st.title("🔤 Irish Music Generator")



# Side Bar
nl_title = "Make me a song with three sections of bar length 4 each with sections being somewhat similar to each other. The metre of the song should be 4/4 and the key Dminor."
nl_prompt_box = st.sidebar.text_area("NL Prompt:", value=nl_title, height=300)
trans_prompt_box = st.sidebar.text_area("Transformer Prompt:", value=st.session_state.trans_prompt, height=300)
st.session_state.trans_prompt = trans_prompt_box
generate_music_button = st.sidebar.button("Generate Music", on_click=run_transformer)
with open('tunesformer/prompt.txt', 'w') as f:
    f.write(trans_prompt_box)



# Main Page
gen_abc_box = st.text_area("# Generated 🔤 notation:", value=st.session_state.gen_abc, height=300)
st.session_state.gen_abc = gen_abc_box
with open('sounds_current/placeholder.abc', 'w') as f:
    f.write(gen_abc_box)

## Display the sheet music
score = m21.converter.parse(gen_abc_box, format='abc')
if st.session_state.old_score!= score:
    sonify_all_files('sounds_current', 'sounds_current', 'sounds_current', './abcsonification/SGM-v2.01-NicePianosGuitarsBass-V1.2.sf2')
    st.session_state.old_score = score
display_sheet_music(score)
st.audio('sounds_current/placeholder.wav', format='audio/wav')

