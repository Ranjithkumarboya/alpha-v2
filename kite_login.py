import streamlit as st
from auth import ZerodhaAuth


class KiteLogin:

    def __init__(self):
        self.auth = ZerodhaAuth()

    def login(self):
        st.subheader("🔐 Zerodha Login")

        login_url = self.auth.login_url()

        st.markdown(
            f"[👉 Click here to Login to Zerodha]({login_url})",
            unsafe_allow_html=True,
        )

        request_token = st.text_input(
            "Paste Request Token after login"
        )

        if st.button("Generate Access Token"):

            if request_token:

                try:
                    data = self.auth.generate_session(request_token)

                    st.session_state["ACCESS_TOKEN"] = data["access_token"]

                    st.success("✅ Login Successful")

                except Exception as e:
                    st.error(str(e))
