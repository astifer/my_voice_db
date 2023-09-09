from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

from cluster.w2v import Vectors


app = FastAPI()


@app.post('/upload')
async def upload_json(file: UploadFile):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}

@app.get('/get_img')
async def show_result():
    return FileResponse("test.jpg")

@app.get('/vectors')
async def vectors():
    l = list()
    try:
        l = Vectors[:5]
    except Exception as e:
        return {'status': 'exc',
                'Exception': str(e)}
    finally:
        if l is not None:
            return {'list': l}