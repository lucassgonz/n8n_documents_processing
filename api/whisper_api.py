from fastapi import FastAPI, UploadFile, File, HTTPException
import whisper
import uvicorn
import os
from datetime import datetime
import shutil

app = FastAPI()
model = whisper.load_model("base")

TRANSCRIPTS_DIR = "transcripts"
os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    # Verifica se o arquivo tem extensão permitida
    allowed_extensions = ["wav", "mp3", "m4a"]
    filename = file.filename
    ext = filename.split(".")[-1].lower()

    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Unsupported audio format")

    # Salva o arquivo com o nome original na pasta temporária
    temp_path = f"temp.{ext}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Faz a transcrição com Whisper
    result = model.transcribe(temp_path)

    # Salva a transcrição em arquivo texto
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    transcript_filename = f"{now}.txt"
    transcript_path = os.path.join(TRANSCRIPTS_DIR, transcript_filename)

    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    # Remove o arquivo temporário
    os.remove(temp_path)

    return {
        "text": result["text"],
        "transcript_file": transcript_path
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
