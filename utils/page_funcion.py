import streamlit as st

# En esta funcion creo el menu con las rutas denavegacion

def menu_pages():
    pages = {
        'Home':[st.Page(r'C:\Users\magudelo\OneDrive\Proyectos python\streamlit_first\pages\home.py', title='Informacion')],

        'Administrar tercero': [
            st.Page(r'C:\Users\magudelo\OneDrive\Proyectos python\streamlit_first\pages\registrar_tercero.py', title='Registrar'),
        ]
    }

    return pages 

