import streamlit as st
import streamlit.components.v1 as components

def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                height: 3em;
                width: 12em;
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

cols = st.columns(4)
cols[0].button('first button', key='b1')
cols[1].button('second button', key='b2')
cols[2].button('third button', key='b3')
cols[3].button('fourth button', key='b4')

ChangeButtonColour('second button', 'red', 'blue') # button txt to find, colour to assign
ChangeButtonColour('fourth button', '#c19af5', '#354b75') # button txt to find, colour to assign