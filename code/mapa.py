import streamlit as st
import streamlit.components.v1 as components

import streamlit as st
import streamlit.components.v1 as components

def ChangeButtonStyle(widget_label, style):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    {style}
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

# Define the style you want to apply to all buttons
global_button_style = """
    elements[i].style.color = 'white';
    elements[i].style.height = '3em';
    elements[i].style.width = '12em';
    elements[i].style.borderRadius = '10px';
    elements[i].style.border = '3px solid #ce1126';
    elements[i].style.fontSize = '20px';
    elements[i].style.fontWeight = 'bold';
    elements[i].style.margin = 'auto';
    elements[i].style.display = 'block';
"""

# Apply the global style to all buttons
ChangeButtonStyle('first button', global_button_style)
ChangeButtonStyle('second button', global_button_style)
ChangeButtonStyle('third button', global_button_style)
ChangeButtonStyle('fourth button', global_button_style)

# Change the style of specific buttons
ChangeButtonStyle('second button', "elements[i].style.background = 'linear-gradient(to bottom, #ce1126 5%, #ff5a5a 100%)'; elements[i].style.backgroundColor = '#ce1126';")
ChangeButtonStyle('fourth button', "elements[i].style.background = '#354b75'; elements[i].style.color = '#c19af5'; elements[i].style.width = '15em'; elements[i].style.height = '4em';")

# Create the buttons
cols = st.columns(4)
cols[0].button('first button', key='b1')
cols[1].button('second button', key='b2')
cols[2].button('third button', key='b3')
cols[3].button('fourth button', key='b4')
