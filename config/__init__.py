"""
Configuration module for the application
"""
from pydantic import Field
from pydantic import BaseModel


class Config(BaseModel):
    """
    Configuration class for the application
    Args:
        BaseModel (): Pydantic BaseModel
    """
    api_url: str = Field(
        default="https://rickandmortyapi.com/api",
        min_length=1
    )
    character_endpoint: str = Field(
        default="character",
        min_length=1
    )
    episode_endpoint: str = Field(
        default="episode",
        min_length=1
    )
    location_endpoint: str = Field(
        default="location",
        min_length=1
    )
    workflows: list = Field(
        default=["character", "episode", "location"],
        min_items=1
    )
