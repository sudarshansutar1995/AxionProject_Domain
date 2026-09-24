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
<<<<<<< HEAD
       
    "DATABASE_URL",
    "postgresql://sudarshandb:Akkalkot%40413216@postgresudarshan.postgres.database.azure.com:5432/axion-db?sslmode=require"

=======
        "DATABASE_URL",
        #"postgresql://axion_user:P%40ssw01rd%40123@localhost:5432/axion_db",
         "postgresql://sudarshandb:Akkalkot%40413216@postgresudarshan.postgres.database.azure.com:5432/axiondb"
>>>>>>> github/main
    )

settings = Settings()
