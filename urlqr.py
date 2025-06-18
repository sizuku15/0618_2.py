
import streamlit as st
import qrcode
import io
st.title("URLをQRcodeに変換")

with st.form(key="url-input",clear_on_submit=True):
    url=st.text_input("URL:")
    button=st.form_submit_button("変換")
    
if url:
    img=qrcode.make(url)
    with io.BytesIO() as f:
        img.save(f,format="PNG")
        png=f.getvalue()
    st.write(url)
    st.image(png)
    st.download_button("Download",date=png,file_name="urlqr.png")