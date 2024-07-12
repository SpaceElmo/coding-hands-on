
import streamlit as st

def calc_kh(knee_ht):
    ht=(2.69*knee_ht)+24.2
    return ht

def main():
    st.title("Knee Height calculator")

    knee_ht=st.number_input("Knee height in cm",step=1)
    age = st.number_input("Age:", step=1)
    gender = st.selectbox("Gender:", ["Other", "Male", "Female"])
    try:
        ht=calc_kh(knee_ht)
    except:
        st.write("Awaiting inputs")    
    st.write(f"The calculated height is {ht:.1f} cm")    

if __name__ == "__main__":
    main()