# Check request_token from URL
query_params = st.query_params

# DEBUG 1
st.write("Query Params:", query_params)

if "request_token" in query_params:

    request_token = query_params["request_token"]

    # DEBUG 2
    st.write("Request Token:", request_token)

    try:
        access_token = self.auth.generate_session(request_token)

        # DEBUG 3
        st.write("Access Token:", access_token)

        st.session_state["access_token"] = access_token

        st.success("✅ Login Successful")

        st.rerun()

    except Exception as e:
    import traceback
    st.code(traceback.format_exc())
