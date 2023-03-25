import os
import logging
import uvicorn
from src.api.rest import app

if __name__ == "__main__":
    logging.basicConfig(
        filename=f"{os.getcwd()}/log.txt",
        filemode="a",
        format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        level=logging.DEBUG,
    )
    uvicorn.run(app, host="localhost", port=8000)
