"""
Axion Ingestion Service - Configuration
Loads database connection string from environment variable.
"""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    # PostgreSQL connection string
    # Format: postgresql://<user>:<password>@<host>:<port>/<database>
    # Example: postgresql://postgres:postgres@localhost:5432/axiondb
    DATABASE_URL: str = os.getenv(
       
    "DATABASE_URL",
    "postgresql://sudarshandb:Akkalkot%40413216@postgresudarshan.postgres.database.azure.com:5432/axion-db?sslmode=require"

    )

settings = Settings()
