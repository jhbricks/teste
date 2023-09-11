import streamlit as st
import streamlit.components.v1 as components

def ChangeButtonStyle(widget_label, background_color, style):
    hover_transparency = 0.2  # Set the desired transparency (0.0 - 1.0)

    htmlstr = f"""
        <style>
            .button-{widget_label} {{
                background: {background_color};
                {style}
            }}
            .button-{widget_label}:hover {{
                background: rgba({int(background_color[1:3], 16)}, {int(background_color[3:5], 16)}, {int(background_color[5:], 16)}, {hover_transparency});
            }}
        </style>
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].classList.add('button-{widget_label}');
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

# Define the style you want to apply to all buttons
global_button_style = """
    color: white;
    height: 3em;
    width: 12em;
    border-radius: 10px;
    border: 3px solid #ce1126;
    font-size: 20px;
    font-weight: bold;
    margin: auto;
    display: block;
"""

# Create the buttons
cols = st.columns(2)

cols[0].button('second button', key='b2')
cols[1].button('fourth button', key='b4')

# Apply the global style to all buttons (This will apply the style to all buttons initially)
ChangeButtonStyle('second button', '#ce1126', global_button_style)
ChangeButtonStyle('fourth button', '#354b75', global_button_style)
