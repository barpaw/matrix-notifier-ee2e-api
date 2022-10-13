from nio import AsyncClient, AsyncClientConfig
from fastapi import FastAPI
from pydantic import BaseModel


class Notify(BaseModel):
    matrixHomeserverURL: str
    matrixHomeserverUser: str
    matrixHomeserverPasswd: str
    matrixHomeserverRoom: str
    message: str


app = FastAPI()


@app.get("/")
def root():
    return {"Status": "200"}

@app.get("/health")
def health():
    return {"Status": "200"}

@app.post("/send-message")
async def send_message(notify: Notify):

    await send_message_to_ee2e_room(notify.matrixHomeserverURL, notify.matrixHomeserverUser, notify.matrixHomeserverPasswd, notify.matrixHomeserverRoom, notify.message)
    return {"Status": "200"}


async def send_message_to_ee2e_room(matrixHomeserverURL, matrixHomeserverUser, matrixHomeserverPasswd, matrixHomeserverRoom, message):

    client_config = AsyncClientConfig(
        max_limit_exceeded=0,
        max_timeouts=0,
        store_sync_tokens=True,
        encryption_enabled=True,)

    client = AsyncClient(matrixHomeserverURL, matrixHomeserverUser)
    await client.login(matrixHomeserverPasswd)

    if client.should_upload_keys:
        await client.keys_upload()

    await client.sync(timeout=30000, full_state=True)

    await client.room_send(
        room_id=matrixHomeserverRoom,
        message_type="m.room.message",
        content={
            "msgtype": "m.text",
            "body": message
        },
        ignore_unverified_devices=True,
    )
    await client.close()
