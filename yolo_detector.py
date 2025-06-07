from ultralytics import YOLO

# Load your trained YOLOv8 model
model = YOLO("best.pt")  # Make sure this file is in the same folder

def detect_cards_from_image(image_path):
    results = model(image_path)
    cards_detected = []

    for r in results:
        for box in r.boxes:
            class_id = int(box.cls)
            label = r.names[class_id]
            cards_detected.append(label)

    return cards_detected
