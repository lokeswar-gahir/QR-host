import qrcode
import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO

st.title("QR code generator")
data = st.text_area("Enter some texts:")
with st.expander("Customization..."):
    fore_color = st.color_picker("Foreground Color","#000")
    back_color = st.color_picker("Background Color", "#FFF")
    border = st.number_input("Border", 0,4,1,step=1)


if(st.button("Generate",type="primary")):
    if data == "":
        st.info("Add some text to generate the QR-code.")
    else:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=15, border=border)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fore_color, back_color=back_color)
        
        im_arr = np.array(img)
        st.image(im_arr, width=250)

        output = BytesIO()
        img.save(output)

        st.download_button(label="Download QR",
                            data=output.getvalue(),
                            file_name="qr.png")