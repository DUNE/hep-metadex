import protodune_metadex.main as protodune
from fastapi import FastAPI

# TODO: Figure out how to include lifespan events from multiple FastAPI apps.
app = FastAPI(lifespan=protodune.lifespan)

app.mount("/protodune", protodune.app)
