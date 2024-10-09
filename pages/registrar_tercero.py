import streamlit as st

# Creo el formulario para registrar los terceros
form =  st.form(key='terceros', clear_on_submit=True, enter_to_submit=False, border=True)
form.title('Registar Tercero')
form.text_input('Nit')
form.text_input('nombre')

# aqui con whit form indico que la lista a seleccionar hace parte del formulario terceros
with form:  
    validar_certificado = st.selectbox('suministró certificación bajo gravedad de juramento?',['','si','no'])
    validar_deducciones = st.selectbox('se tomará o no costos y deducciones?',['','si','no','no suministro informacion'])
    validar_dependiente = st.selectbox('tiene dependientes economicos?',['','si','no'])
    validar_deducciones = st.selectbox('tiene medicina prepagada',['','si','no'])
# al final agrego el boton guardar
form.form_submit_button('guardar')