from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

import os
import os.path


app = FastAPI()


@app.post('/upload')
async def upload_json(file: UploadFile):
    try:
        contents = file.file.read()
        with open('data/'+file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
#     l = file_2_vectors(file.filename)
    
    return {"message": f"Successfully uploaded {file.filename}",
            'embs': [0]}

@app.get('/get_img')
async def show_result(n=1):
    return FileResponse(f"test.jpg")


@app.get('/vectors')
async def vectors():
    
    address, dirs, files = os.walk('data')
            
    return {'list': str(files[0])}