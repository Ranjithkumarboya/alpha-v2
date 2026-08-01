import streamlit as st
from auth import ZerodhaAuth


class KiteLogin:

    def __init__(self):
        self.auth = ZerodhaAuth()

    def login(self):

        st.subheader("🔐 Zerodha Login")

        # Already logged in
        if "access_token" in st.session_state:
            st.success("✅ Zerodha Connected")
            return

        # Login button
        login_url = self.auth.login_url()
        st.markdown(f"👉 [Click here to Login to Zerodha]({login_url})")

        # Read URL parameters
        query_params = st.query_params

        # DEBUG
        st.write("Query Params:", query_params)

        if "request_token" in query_params:

            request_token = query_params["request_token"]

            st.write("Request Token:", request_token)

            try:
                access_token = self.auth.generate_session(request_token)

                st.write("Access Token:", access_token)

                st.session_state["access_token"] = access_token

                st.success("✅ Login Successful")

                st.rerun()

            except Exception as e:
                import traceback

                st.error(f"Login Failed: {e}")
                st.code(traceback.format_exc())
