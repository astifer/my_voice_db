from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import uvicorn

# from cluster.create_csv_labeled_data import labeled_jsons_to_df
from cluster.create_all_data import file_2_df
from cluster.w2v import file_2_vectors
from cluster.generate_clusters import generate_k_means_clusters, clusters_2_df


app = FastAPI()


@app.post("/upload")
async def upload_json(file: UploadFile = File()):
    try:
        contents = file.file.read()
        file_location = "data/" + file.filename
        with open(file_location, "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": f"There was an error uploading the file {Exception}"}

    vectors, model = file_2_vectors(file_location)
    s_score, kmeans = generate_k_means_clusters(vectors)
    df_text = file_2_df(file_location)
    clustered = clusters_2_df(
        vectors,
        kmeans,
        model,
        df_text
    )

    return clustered.to_json()


@app.get("/get_img")
async def show_result():
    return FileResponse("test.jpg")


@app.get("/vectors")
async def vectors():
    l = [0] * 10

    try:
        l = l[:5]
    except Exception as e:
        return {"status": "exc", "Exception": str(e)}
    finally:
        if l is not None:
            return {"list": l}


if __name__ == "__main__":
    # Run server using given host and port
    uvicorn.run(app, host="localhost", port=8080)
