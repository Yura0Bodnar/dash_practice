import os
from flask import Flask, request, jsonify

server = Flask(__name__)

# Папка для збереження датасетів
UPLOAD_FOLDER = "datasets"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Створюємо папку, якщо її не існує


# 🔹 Ендпоінт для завантаження файлу
@server.route("/api/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "Файл не знайдено"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Файл не обрано"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)  # Збереження файлу

    return jsonify({"message": f"Файл '{file.filename}' завантажено", "filename": file.filename})
