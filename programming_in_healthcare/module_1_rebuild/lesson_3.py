"""Lesson 3

If you have completed all of the other lessons, and would like another exercise,
try out the below.

Gotten stuck, look at the slides at:
https://letsdodigital.org/learn/learn-python/module-1/4-lets-build.html
"""

"""Exercise 1 - Create any clinical calculator you like
1. Go to your favourite search engine.
2. Type in "Clinical Calculator Equations"
3. Pick any clinical calculator you like. Make sure can find an equation associated with it.
4. Create your own web app using what you have already learnt
"""

"""Exercise 2 - Change the layout
1. Follow the guide at:
https://docs.streamlit.io/library/advanced-features/theming
2. Change the colours of your web app
3. Change the font
4. Change theme
"""
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