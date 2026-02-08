import streamlit as st
import requests
from PIL import Image
import io

st.title("Removedor de fundo")
st.write("Retire fundos de imagens. Remova o fundo de suas imagens JPG e PNG com uma qualidade excepcional.")

# URL do servidor FastAPI
FASTAPI_URL = "http://localhost:8000/remove-bg"

uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Exibe imagem original
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Imagem Original")
        st.image(uploaded_file)
    
    # Botão para processar
    if st.button("Remover Fundo"):
        st.write("Processando...")
        
        try:
            # Envia arquivo para o FastAPI
            files = {"file": (uploaded_file.name, uploaded_file.getbuffer(), uploaded_file.type)}
            response = requests.post(FASTAPI_URL, files=files)
            
            # Se sucesso, exibe imagem processada
            if response.status_code == 200:
                processed_image = Image.open(io.BytesIO(response.content))
                
                with col2:
                    st.subheader("Imagem Processada")
                    st.image(processed_image)
                
                # Botão para download
                st.download_button(
                    label="Download Imagem Processada",
                    data=response.content,
                    file_name="processed_image.png",
                    mime="image/png"
                )
                st.success("Fundo removido com sucesso!")
            else:
                st.error(f"Error: {response.status_code}")
        
        except requests.exceptions.ConnectionError:
            st.error("Não foi possível conectar ao servidor FastAPI. Certifique-se de que ele está rodando em http://localhost:8000")
        except Exception as e:
            st.error(f"Error: {str(e)}")