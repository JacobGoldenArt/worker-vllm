import os
from huggingface_hub import snapshot_download

# Get the hugging face token
HUGGING_FACE_HUB_TOKEN = os.environ['HUGGING_FACE_HUB_TOKEN']
#testing out ehartford/based-13b
HF_MODEL = "ehartford/based-13b"

# Download the 7B
if HUGGING_FACE_HUB_TOKEN:
    snapshot_download(
            HF_MODEL,
            local_dir="/model/ehartford/based-13b",
            token=HUGGING_FACE_HUB_TOKEN
    )