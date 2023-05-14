import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


#config
st.set_page_config(page_title="Valerapp", page_icon="🤖", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
email_address ="emailcontact@gmail.com"

lottie_file ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"

with st.container():
    st.subheader("Hola, somos Valerapp :wave:")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de la tecnología y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos."
    )
    st.write("[Saber más >](https://valerapp.com/)")



# sobre nosotros
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Sobre nosotros")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
            Seguramente te vamos a poder ayudar si:

            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
            """
        )
        st.write("[Más sobre nosotros>](https://valerapp.com/about/)")
    with right_column:
        st_lottie(load_lottieurl(lottie_file), height=400)

# servicios
with st.container():
    st.write("---")
    st.header("Nuestros servicios")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/apps.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.    
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/automation.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Automatización de procesos")
        st.write(
            """
            Si realizas cualquier tipo de tarea repetitiva como por ejemplo introducir datos en excel u otras aplicaciones, gestión de facturas, envío de emails a proveedores etc Lo que quizás necesitas es una automatización de tareas para poder liberar recursos de esas actividades y poder emplearlos en otras tareas más productivas.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/visualizacion.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Visualización de datos")
        st.write(
            """
            Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una aplicación en la que puedas tener toda la información de interes de tu empresa.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

# contacto
with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros!")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
