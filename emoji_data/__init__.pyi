from typing import Dict, List, Any
from data_dict import *
from data_dict_retrieval import *

__all__ = ["get_emoji_unicode_dict", "get_aliases_unicode_dict", "EMOJI_DATA", "STATUS", "LANGUAGES", "CATEGORIES", "BASIC_EMOJIS"]

def get_emoji_unicode_dict(lang: str) -> Dict[str, str]: ...
def get_aliases_unicode_dict() -> Dict[str, str]: ...

def get_emoji_data_for_lang(lang: str) -> Dict: ...
def get_emoji_aliases_data() -> Dict: ...
def get_categories_data() -> Dict[Dict[str, int]]: ...
def categories_key_chain() -> Dict[Dict[str, int]]: ...
def emoji_data() -> Dict[Dict[str, int, Any]]: ...
def key_chain() -> Dict[Dict[str, Any]]: ...

 