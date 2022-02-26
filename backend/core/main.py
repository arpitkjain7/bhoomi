import uvicorn

from core.apis.api import app

from core.database.db_defaults import main

main()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
