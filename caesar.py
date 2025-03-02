import streamlit as st

def mahoa(banro, k):  
    ketqua = ""
    for char in banro:
        if 'A' <= char <= 'Z':
            so = ord(char) - ord('A')
            so_mahoa = (so + k) % 26
            ky_tu_mahoa = chr(so_mahoa + ord('A'))
            ketqua += ky_tu_mahoa
        elif 'a' <= char <= 'z':
            so = ord(char) - ord('a')
            so_mahoa = (so + k) % 26
            ky_tu_mahoa = chr(so_mahoa + ord('a'))
            ketqua += ky_tu_mahoa
        else:
            ketqua += char 
    return ketqua

def giaima(banma, k):
    ketqua = ""
    for char in banma:
        if 'A' <= char <= 'Z':
            so = ord(char) - ord('A')
            so_giaima = (so - k) % 26
            ky_tu_giaima = chr(so_giaima + ord('A'))
            ketqua += ky_tu_giaima
        elif 'a' <= char <= 'z':
            so = ord(char) - ord('a')
            so_giaima = (so - k) % 26
            ky_tu_giaima = chr(so_giaima + ord('a'))
            ketqua += ky_tu_giaima
        else:
            ketqua += char
    return ketqua

st.title("Mật mã Caesar")
option = st.radio("Chọn chế độ:", ("Mã hóa", "Giải mã"))

ban_text = st.text_area("Nhập văn bản:")
k = st.number_input("Nhập giá trị k:", min_value=0, step=1, format="%d")

if st.button("Thực hiện"):
    if not ban_text:
        st.warning("Vui lòng nhập văn bản!")
    else:
        if option == "Mã hóa":
            ketqua = mahoa(ban_text, k)
        else:
            ketqua = giaima(ban_text, k)
        st.success(f"Kết quả: {ketqua}")
