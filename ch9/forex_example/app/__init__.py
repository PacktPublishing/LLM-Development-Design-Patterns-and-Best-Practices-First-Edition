"""
Initialize the app package.
This file ensures the directory is treated as a Python package.
"""

from .chromadb_setup import get_chroma_collection
from .services import fetch_forex_data_alpha_vantage, generate_embedding, perform_inference_with_phi_model
from app import get_chroma_collection
