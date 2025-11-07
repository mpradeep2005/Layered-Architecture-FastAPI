import os
import sys
import subprocess
from dotenv import load_dotenv

def main():
    env_file=".env.dev"
    load_dotenv(env_file)
    database_url = os.getenv("database_url")
    if not database_url:
        print(f"Error: {env_file} not found or DATABASE_URL not set.")
        sys.exit(1)

    command=f"sqlacodegen {database_url} > db/models.py "
    subprocess.run(command,shell=True)
    print("Models generated successfully in db/models.py")

if __name__ == "__main__":
    main()