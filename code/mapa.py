import streamlit as st
import streamlit.components.v1 as components

def ChangeButtonStyle(widget_label, background_color):
    htmlstr = f"""
        <style>
            .custom-button {{
                background-color: {background_color};
                color: white;
                height: 3em;
                width: 12em;
                border-radius: 10px;
                font-size: 20px;
                font-weight: bold;
                margin: auto;
                display: block;
                transition: background-color 0.3s ease; /* Adiciona uma transição suave */
            }}
            .custom-button:hover {{
                background-color: rgba({background_color.r}, {background_color.g}, {background_color.b}, 0.2);
            }}
        </style>
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].classList.add('custom-button');
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

# Defina a cor de fundo que você deseja para os botões
button_background_color = "#ce1126"  # Substitua pela cor desejada

# Create the buttons
cols = st.columns(2)

cols[0].button('second button', key='b2')
cols[1].button('fourth button', key='b4')

# Apply the custom style to all buttons (This will apply the style to all buttons initially)
ChangeButtonStyle('second button', button_background_color)
ChangeButtonStyle('fourth button', button_background_color)
