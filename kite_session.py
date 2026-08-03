from kiteconnect import KiteConnect
import streamlit as st


class KiteSession:

    _kite = None

    @classmethod
    def get_kite(cls):

        if cls._kite is None:

            cls._kite = KiteConnect(
                api_key=st.secrets["API_KEY"]
            )

        if "access_token" in st.session_state:

            cls._kite.set_access_token(
                st.session_state["access_token"]
            )

        return cls._kite
