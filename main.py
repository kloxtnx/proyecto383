import streamlit as st
from utils.page_funcion import menu_pages

paginas = menu_pages()
pg = st.navigation(paginas)
pg.run()

def main():
    pass

if __name__ == "__main__":
    main()
