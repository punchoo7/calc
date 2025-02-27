import streamlit as st
import mysql.connector
import hashlib

# Database connection
def create_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",  # Change this
        password="root",  # Change this
        database="user_db"
    )

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register user
def register_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        return True
    except mysql.connector.IntegrityError:
        return False
    finally:
        cursor.close()
        conn.close()

# Function to check login credentials
def login_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return user is not None

# Streamlit UI
st.title("User Authentication System")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

if menu == "Register":
    st.subheader("Create a New Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    
    if st.button("Register"):
        if new_user and new_pass:
            if register_user(new_user, new_pass):
                st.success("Registration successful! You can now log in.")
            else:
                st.error("Username already exists. Try a different one.")
        else:
            st.warning("Please fill in both fields.")

elif menu == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if login_user(username, password):
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")
