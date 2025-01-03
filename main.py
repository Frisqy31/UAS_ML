import streamlit as st
import runpy

def main():

    # Main menu options
    menu = ["Random Forest", "Perceptron"]
    choice = st.sidebar.selectbox("Select Main Menu", menu)

    if choice == "Random Forest":
        rf_sub_menu()
    elif choice == "Perceptron":
        p_sub_menu()

def rf_sub_menu():
    st.subheader("Random Forest Menu")

    # Random Forest submenu options
    sub_menu = ["Fish", "Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fish":
        st.write("Kamu memilih Random Forest -> Fish.")
        runpy.run_path('app_RFfish.py')
    elif choice == "Fruit":
        st.write("Kamu memilih Random Forest -> Fruit.")
        runpy.run_path('app_RFfruit.py')

def p_sub_menu():
    st.subheader("Perceptron Menu")

    # Random Forest submenu options
    sub_menu = ["Fruit"]
    choice = st.sidebar.radio("Select Sub Menu", sub_menu)

    if choice == "Fruit":
        st.write("Perceptron -> Fruit.")
        runpy.run_path('app_percepfruit.py')

if __name__ == "__main__":
    main()
