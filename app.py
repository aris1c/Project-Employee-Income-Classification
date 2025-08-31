import streamlit as st
from ml_app import run_ml_app

def main():
    st.set_page_config(
        page_title="Project by Aris Candra",
        page_icon="💼",
        layout="wide"
    )

    # Sidebar menu
    with st.sidebar:
        st.title("Menu")
        menu = ['Home', 'Machine Learning']
        choice = st.selectbox('', menu)

    if choice == 'Home':
        # Header
        st.markdown(
            """
            <h1 style='text-align: center; color: #4B8BBE;'>
                Employee Income Classification
            </h1>
            """,
            unsafe_allow_html=True
        )

        # Gambar di bagian atas
        st.image(
            'https://img.freepik.com/premium-vector/salary-vector-concept-male-worker-female-looking-his-salary-while-standing-with-big-calendar_199064-209.jpg',
            use_column_width=True,
            caption="Prediksi Pendapatan"
        )

        # Deskripsi
        st.markdown(
            """
            <div style="max-width: 900px; margin: auto; font-size:18px; line-height:1.6; text-align: justify;">
                Ini adalah website deploy by Aris Candra untuk mengklasifikasikan pendapatan seseorang ke dalam dua kategori, yaitu pendapatan kurang dari atau sama dengan 50 ribu dolar (<=50K) dan lebih dari 50 ribu dolar (>50K). Prediksi ini didasarkan pada berbagai atribut demografis dan pekerjaan seperti usia, jenis pekerjaan, tingkat pendidikan, status pernikahan, ras, jenis kelamin, jam kerja per minggu, serta informasi finansial seperti keuntungan atau kerugian modal. Dengan menggunakan data tersebut, model dapat membantu memperkirakan tingkat pendapatan seseorang berdasarkan karakteristik individu tersebut.
            </div>
            """,
            unsafe_allow_html=True
        )

    elif choice == 'Machine Learning':
        run_ml_app()


if __name__ == '__main__':
    main()

