"""Embedding generation module using OpenAI embedding"""

from functools import lru_cache
from langchain_openai import OpenAIEmbeddings
from app.config import get_settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


