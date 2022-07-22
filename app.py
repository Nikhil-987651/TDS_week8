import streamlit as st

st.set_page_config(page_title="Number Multiplier")

st.header('Enter two numbers to multiply them')
st.write("")


def user_input():
    number_1 = st.number_input("Enter the First Number")
    st.write("")
    number_2 = st.number_input("Enter the Second Number")
    return number_1, number_2


st.write("")
st.write("")

numbers = user_input()

st.header(str(numbers[0]) + "  *  " + str(numbers[1]) + "  =  " + str(numbers[0]*numbers[1]))
#print(numbers)


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
