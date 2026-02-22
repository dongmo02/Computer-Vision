🎯 ArUco Marker Pose Estimation mit OpenCV

Dieses Projekt demonstriert die Erkennung und Positionsbestimmung (Pose Estimation) eines ArUco-Markers mithilfe von OpenCV und NumPy.

Das Programm:

Lädt ein Bild

Erkennt ArUco-Marker

Schätzt die 3D-Pose eines bestimmten Markers

Berechnet die 3D-Koordinaten eines Punktes im Marker-Koordinatensystem

Visualisiert die erkannten Marker im Bild

🚀 Funktionen

Kamerakalibrierungsmatrix und Verzerrungskoeffizienten

ArUco Marker Detection (DICT_4X4_1000)

Pose-Schätzung eines Markers

Transformation eines Punktes vom Marker-Koordinatensystem ins Kamerakoordinatensystem

Anzeige des Bildes mit eingezeichneten Markern

🛠 Verwendete Technologien

Python 3

OpenCV (cv2)

OpenCV ArUco Modul

NumPy

▶ Installation

Installiere die benötigten Pakete:

pip install opencv-python opencv-contrib-python numpy

Wichtig:
Für das ArUco-Modul wird opencv-contrib-python benötigt.

▶ Anwendung starten

Lege dein Bild (z.B. imagee.jpg) in denselben Ordner.

Passe ggf. den Bildpfad im Code an.

Starte das Skript:

python main.py
🧠 Funktionsweise
1️⃣ Kamerakalibrierung

Das Programm verwendet eine vorgegebene:

Kamera-Matrix (camera_matrix)

Verzerrungskoeffizienten (dist_coeffs)

Diese Werte stammen aus einer vorherigen Kamerakalibrierung.

2️⃣ Marker-Erkennung

Das Bild wird geladen und mit:

cv2.aruco.detectMarkers()

nach Markern des Typs DICT_4X4_1000 durchsucht.

3️⃣ Pose Estimation

Wenn Marker mit ID 52 gefunden wird:

Rotation (rvec)

Translation (tvec)

werden berechnet mit:

cv2.aruco.estimatePoseSingleMarkers()
4️⃣ 3D-Koordinatenberechnung

Ein Punkt im Marker-Koordinatensystem wird:

Mit der Rodrigues-Transformation rotiert

Mit dem Translationsvektor verschoben

Ergebnis:

→ Position des Punktes im Kamerakoordinatensystem

📊 Beispielausgabe
Koordinaten des Punkts für Marker 52: [x y z]
🎓 Lernziele

Dieses Projekt demonstriert Kenntnisse in:

Kamerakalibrierung

Computer Vision

3D-Transformationen

Pose Estimation

Verwendung des OpenCV ArUco-Moduls

Lineare Algebra (Rotation + Translation)
