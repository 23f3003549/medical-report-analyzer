import os
import uuid
from flask import Blueprint, request, jsonify

upload_bp = Blueprint("upload", __name__)

UPLOAD_FOLDER = "uploads"

@upload_bp.route("/upload", methods=['POST'])
def upload_file():
    file = request.files.get("file")

    if not file:
        return jsonify({
            "error":"No file uploaded" 
        }), 400
    
    # get file extension
    ext = os.path.splitext(file.filename)[1]

    # generate unique filename
    unique_filename = str(uuid.uuid4()) + ext

    # save file
    filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
    file.save(filepath)

    return jsonify({
        "message": "File uploaded successfully",
        "original_filename": file.filename,
        "stored_filename": unique_f
    })
