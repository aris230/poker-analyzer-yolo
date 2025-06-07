from flask import Flask, request, render_template
from yolo_detector import detect_cards_from_image
from logic import evaluate_hand
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    uploaded_file = request.files['image']
    image_path = os.path.join("temp", uploaded_file.filename)
    os.makedirs("temp", exist_ok=True)
    uploaded_file.save(image_path)

    detected_cards = detect_cards_from_image(image_path)

    # Basic logic: first 2 = hole cards, rest = board
    hole_cards = detected_cards[:2] if len(detected_cards) >= 2 else ["??", "??"]
    board_cards = detected_cards[2:7] if len(detected_cards) >= 5 else ["??"] * 5

    recommendation = evaluate_hand(hole_cards, board_cards)

    return render_template("result.html",
                           hole_cards=hole_cards,
                           board_cards=board_cards,
                           recommendation=recommendation,
                           ocr_debug=", ".join(detected_cards))

if __name__ == '__main__':
    app.run(debug=True)
