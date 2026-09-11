import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def get_secret(name: str) -> str | None:
    """Read a Streamlit Cloud secret, falling back to the local environment."""
    try:
        return st.secrets.get(name, os.getenv(name))
    except FileNotFoundError:
        return os.getenv(name)