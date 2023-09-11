import streamlit as st
import streamlit.components.v1 as components

def ChangeButtonStyle(widget_label, background_color, style):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.background = '{background_color}';
                    {style}
                }}
                    button:hover {{
                    background: '{background_color, 20%}';
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
    elements[i].style.fontSize = '20px';
    elements[i].style.fontWeight = 'bold';
    elements[i].style.margin = 'auto';
    elements[i].style.display = 'block';
    #elements[i].style.hover = '{background_color} 20%';
"""

# Create the buttons
cols = st.columns(2)

cols[0].button('second button', key='b2')
cols[1].button('fourth button', key='b4')

# Apply the global style to all buttons (This will apply the style to all buttons initially)
ChangeButtonStyle('second button', '#ce1126', global_button_style)
ChangeButtonStyle('fourth button', '#354b75', global_button_style)
