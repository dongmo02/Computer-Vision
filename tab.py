from cv2 import aruco
import cv2
import numpy as np

# Schritt 1: Kamerakalibrierung
camera_matrix = np.array([
    [1.54429299e+04, 0.00000000e+00, 5.6400632e+02],
    [0.00000000e+00, 2.56855332e+03, 3.32656835e+02],
    [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]
], dtype=np.float64)

dist_coeffs = np.array([
    [7.93648166e-01, -4.14613979e+03, -9.80305307e-02,
     -6.18697326e-01, 1.64442322e+05]
], dtype=np.float64)

# Schritt 2: Bild laden
image = cv2.imread('tab.jpg')  # Pfad zum Bild anpassen

if image is None:
    print("Fehler: Bild konnte nicht geladen werden.")
    exit()

# ArUco-Dictionary und Parameter
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000)
parameters = cv2.aruco.DetectorParameters()

# Schritt 3: ArUco-Marker erkennen
corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(
    image, aruco_dict, parameters=parameters
)

# Schritt 4: Pose-Schätzung
if ids is not None:
    positions = []  # Speichert die 3D-Positionen (tvec) der Marker

    for i in range(len(ids)):
        # Pose für EINEN Marker schätzen
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
            corners[i], 0.05, camera_matrix, dist_coeffs
        )

        tvec = tvecs[0]
        rvec = rvecs[0]

        # Distanz Kamera ↔ Marker berechnen
        distance = np.linalg.norm(tvec)
        coordinates = tvec.flatten()
        positions.append(coordinates)

        print(
            f"Marker ID {ids[i][0]}: "
            f"Koordinaten {coordinates}, "
            f"Distanz {distance:.2f} m"
        )

        # Achsen des Markers zeichnen
        cv2.drawFrameAxes(
            image, camera_matrix, dist_coeffs, rvec, tvec, 0.03
        )

        # Text vorbereiten
        text = f"ID: {ids[i][0]} | Dist: {distance:.2f} m"
        text_position = (
            int(corners[i][0][0][0]),
            int(corners[i][0][0][1] - 10)
        )

        # Halbtransparentes Rechteck hinter dem Text
        overlay = image.copy()
        cv2.rectangle(
            overlay,
            (text_position[0] - 5, text_position[1] - 20),
            (text_position[0] + 170, text_position[1]),
            (255, 255, 255),
            -1
        )
        cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)

        # Text auf das Bild schreiben
        cv2.putText(
            image,
            text,
            text_position,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2
        )

    # Pfeil zwischen zwei Markern (in Bildkoordinaten)
    if len(corners) >= 2:
        def center(corner):
            return np.mean(corner[0], axis=0).astype(int)

        p1 = center(corners[0])
        p2 = center(corners[1])

        cv2.arrowedLine(
            image,
            tuple(p1),
            tuple(p2),
            (0, 255, 0),
            3
        )

else:
    print("Keine ArUco-Marker erkannt.")

# Marker-Konturen zeichnen
cv2.aruco.drawDetectedMarkers(image, corners, ids)

# Ergebnis anzeigen
cv2.imshow("Bild mit ArUco-Markern", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

