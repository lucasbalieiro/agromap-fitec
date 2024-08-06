SELECT 'CREATE DATABASE agromap'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'agromap')\gexec

SELECT 'CREATE DATABASE agromap'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'agromap_test')\gexec

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
