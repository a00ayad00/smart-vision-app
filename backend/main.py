import uvicorn
import cv2
import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, StreamingResponse
from PIL import Image
from io import BytesIO
from model import fetch_model
from ultralytics import YOLO

# Initialize FastAPI app
app = FastAPI()

# Load the YOLO model
if not os.path.exists(os.path.join('app_temp', 'model', 'best.pt')):
    model = fetch_model()  # Load YOLO model
else:
    model = YOLO(os.path.join('app_temp', 'model', 'best.pt'))

def preprocess_image(image_bytes):
    """Convert image bytes to a PIL Image."""
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    return image


@app.post("/process/image")
async def predict_image(file: UploadFile = File(...)):
    """Predicting objects in images."""

    # Process as image
    image_bytes = await file.read()
    image = preprocess_image(image_bytes)

    # Perform inference
    results = model(image)[0]

    # Get the plotted result (image with bounding boxes)
    result_image = results.plot()

    # Convert numpy array to bytes for response
    is_success, buffer = cv2.imencode(".jpg", result_image)
    io_buf = BytesIO(buffer)
    io_buf.seek(0)

    # Return the image file
    return StreamingResponse(io_buf, media_type="image/jpeg")
    
@app.post("/process/video")
async def predict_video(file: UploadFile = File(...)):
    temp_input = "temp_input.mp4"
    temp_output = "temp_output.mp4"

    with open(temp_input, "wb") as f:
        f.write(await file.read())

    # Open the video
    cap = cv2.VideoCapture(temp_input)

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(temp_output, fourcc, fps, (width, height))

    # Process each frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to RGB for YOLO
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Run YOLO prediction
        results = model(rgb_frame)[0]

        # Get frame with detection boxes
        result_frame = results.plot()

        # Convert back to BGR for OpenCV
        result_frame_bgr = cv2.cvtColor(result_frame, cv2.COLOR_RGB2BGR)

        # Write to output video
        out.write(result_frame_bgr)

    # Release resources
    cap.release()
    out.release()

    # Return the video file as response
    return FileResponse(temp_output, media_type="video/mp4", filename="result.mp4")

# @app.post("/process/video")
# async def predict_video(file: UploadFile = File(...)):
#     """Predict objects in a video file."""
#     video_bytes = await file.read()
#     with open("video.mp4", "wb") as f:
#         f.write(video_bytes)

#     # Perform inference on the video
#     # model.predict(video_path, save = True, device = 'cuda', project = os.path.join('app_temp', 'results'), name = 'avi', verbose = False, exist_ok = True)
#     model.predict("video.mp4", device = 'cuda', verbose = False)

#     # Return the video file
#     return FileResponse(os.path.join('app_temp', 'result', "vid.avi"), filename="result.mp4")


# if __name__ == "__main__":
#     uvicorn.run("main:app", port=5000, reload=True)