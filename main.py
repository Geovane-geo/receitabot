import streamlit as st
from PIL import Image
import inteligencia
import time

st.set_page_config(layout = 'wide') # página
chave = st.secrets["GEMINI_CHAVE"]

head1, head2, head3 = st.columns([3,11,3], vertical_alignment="center")

with head1:
    st.image("arquivos/slogam.png", use_container_width=True)  
with head2: 
   st.markdown("<h1 style='text-align: center;'>RECEITA DA AI, Bom demais!</h1>", unsafe_allow_html=True)
   st.empty()
   st.markdown("<h2 style='text-align: center;'>O seu assistente virtual para criar receitas!</h2>", unsafe_allow_html=True)
with head3:
     st.image("arquivos/robo cozinhando.jpeg", use_container_width=True)

col1, col2 = st.columns([2, 2])

with col1:
    st.header("Faça o upload de uma foto com os ingredientes")
    arquivo_foto = st.file_uploader("",type = ["jpg","jpeg","png"])
    if arquivo_foto is not None: # que quer dizer se o arquivo foto não estiver vazio 
        imagem = Image.open(arquivo_foto)
        st.image(imagem)
        if st.button("Detectar Possíveis Receitas"):
            with st.spinner(" Aguarde... Geovane está Fazendo amor!"):
                time.sleep(1)
                st.session_state.ingredientes = inteligencia.detectar_ingridientes(chave,imagem)
                st.session_state.receitas = inteligencia.possiveis_receitas(chave,st.session_state.ingredientes)

        if 'ingredientes' in st.session_state: #### quer dizer se ele entrou aqui é porque ele tem algum valor
            st.write(f"Detectar Ingredientes: {st.session_state.ingredientes} ")
            st.write("Possíveis Receitas:")
            for id, receita in enumerate(st.session_state.receitas, start=1):
                        st.write(f"{id} . {receita}") ### ente as f" string se ligar e m ponto, virgula ou espaço 
            
with col2:
    if "receitas" in st.session_state: # se receitas estiver dentro de st.session_state quer dizer que ja foi criado
        st.header("Escolha uma Receita") 
        receita_selecionada = st.selectbox("", st.session_state.receitas )
        with st.spinner("Isso é ao vivo Valdez"):
            if st.button ("Ver Receita:"):
                st.session_state.receita_completa = inteligencia.receita_completa(chave, 
                                                                                st.session_state.ingredientes,
                                                                                receita_selecionada)
                st.write(st.session_state.receita_completa)
