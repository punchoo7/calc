import streamlit as st
def cal(num1,num2,operator):
    if operator == "+":
        return num1+num2
    elif operator =="-":
        return num1-num2
    elif operator =="*":
        return num1*num2
    else:
        if num2 !=0:
            return num1/num2
        else:
            print("invalid")

def main():
    st.title("calculator")
    number1=st.number_input("enter number")
    operator=st.selectbox("select operator",["+","-","*","/"])
    number2=st.number_input("enter the number")
    result=cal(number1,number2,operator)
    if st.button("calculate"):
        print(st.sucess)
    if __name__=="__main__":
        main()

        
            
