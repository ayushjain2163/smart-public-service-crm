import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="Smart Public Service CRM", layout="wide")

st.title("Smart Public Service CRM Dashboard")

# session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# sidebar menu
menu = st.sidebar.selectbox(
    "Menu",
    ["Signup", "Login", "Submit Complaint", "Admin Dashboard", "AI Co-Pilot"]
)

# ---------------- SIGNUP ---------------- #

if menu == "Signup":

    st.header("Admin Signup")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):

        try:

            res = requests.post(
                f"{API}/admin/signup",
                json={
                    "username": username,
                    "password": password
                }
            )

            if res.status_code == 200:
                st.success("Admin created successfully")

            else:
                try:
                    st.error(res.json())
                except:
                    st.error(res.text)

        except Exception as e:
            st.error(f"Connection error: {e}")

# ---------------- LOGIN ---------------- #

elif menu == "Login":

    st.header("Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        try:

            res = requests.post(
                f"{API}/admin/login",
                json={
                    "username": username,
                    "password": password
                }
            )

            if res.status_code == 200:

                try:

                    token = res.json()["access_token"]

                    st.session_state.logged_in = True
                    st.session_state.token = token

                    st.success("Login successful")

                except:
                    st.error("Invalid response from server")

            else:
                st.error("Invalid credentials")

        except Exception as e:
            st.error(f"Connection error: {e}")

# ---------------- SUBMIT COMPLAINT ---------------- #

elif menu == "Submit Complaint":

    st.header("Submit Citizen Complaint")

    text = st.text_area("Complaint")

    location = st.text_input("Location (Area / City)")

    if st.button("Submit Complaint"):

        if text == "" or location == "":
            st.warning("Please fill all fields")

        else:

            try:

                res = requests.post(
                    f"{API}/submit-complaint",
                    json={
                        "text": text,
                        "location": location
                    }
                )

                if res.status_code == 200:
                    st.success("Complaint submitted successfully")

                else:
                    st.error("Submission failed")

            except Exception as e:
                st.error(f"Connection error: {e}")

# ---------------- ADMIN DASHBOARD ---------------- #

elif menu == "Admin Dashboard":

    if not st.session_state.logged_in:
        st.warning("Please login first")
        st.stop()

    st.header("Complaint Analytics Dashboard")

    try:

        res = requests.get(f"{API}/complaints")

        data = res.json()

        df = pd.DataFrame(data)

        if df.empty:
            st.info("No complaints yet")
            st.stop()

        st.subheader("All Complaints")

        st.dataframe(df)

        col1, col2 = st.columns(2)

        with col1:

            sentiment_chart = px.pie(
                df,
                names="sentiment",
                title="Sentiment Distribution"
            )

            st.plotly_chart(sentiment_chart, use_container_width=True)

        with col2:

            category_chart = px.bar(
                df,
                x="category",
                title="Complaint Categories"
            )

            st.plotly_chart(category_chart, use_container_width=True)

    except Exception as e:
        st.error(f"Failed to load complaints: {e}")

# ---------------- AI COPILOT ---------------- #

elif menu == "AI Co-Pilot":

    if not st.session_state.logged_in:
        st.warning("Please login first")
        st.stop()

    st.header("AI Policy / Meeting Notes Summarizer")

    text = st.text_area("Paste meeting notes or policy document")

    if st.button("Generate Summary"):

        if text == "":
            st.warning("Enter text first")

        else:

            try:

                res = requests.post(
                    f"{API}/summarize",
                    json={"text": text}
                )

                if res.status_code == 200:

                    summary = res.json()["summary"]

                    st.subheader("AI Generated Summary")

                    st.write(summary)

                else:
                    st.error("AI processing failed")

            except Exception as e:
                st.error(f"Connection error: {e}")
