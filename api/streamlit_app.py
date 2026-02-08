import streamlit as st
from PIL import Image
from rembg import remove
import io

st.title("Removedor de fundo")
st.write("Retire fundos de imagens. Remova o fundo de suas imagens JPG e PNG com uma qualidade excepcional.")

uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Exibe imagem original
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Imagem Original")
        st.image(image)
    
    # Botão para processar
    if st.button("Remover Fundo"):
        st.write("Processando...")
        
        try:
            # Processamento direto (sem chamar API externa)
            processed_image = remove(image)
            
            with col2:
                st.subheader("Imagem Processada")
                st.image(processed_image)
            
            # Prepara o buffer para download
            buf = io.BytesIO()
            processed_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            # Botão para download
            st.download_button(
                label="Download Imagem Processada",
                data=byte_im,
                file_name="processed_image.png",
                mime="image/png"
            )
            st.success("Fundo removido com sucesso!")
        
        except Exception as e:
            st.error(f"Ocorreu um erro: {str(e)}")
