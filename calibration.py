from cv2 import aruco
import cv2
import numpy as np

# Schritt 1: Kamerakalibrierung
camera_matrix = np.array([
    [2.27108614e+04, 0.00000000e+00, 1.38875055e+02],
    [0.00000000e+00, 1.15328251e+03, 2.59073501e+02],
    [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]
], dtype=np.float64)

dist_coeffs = np.array([
    [-2.59322330e+01, 2.78808401e+03, 1.43732793e-01, 2.92133930e-01, -1.11934064e+05]
], dtype=np.float64)

# Schritt 2: Bild laden und ArUco-Marker erkennen
image = cv2.imread('imagee.jpg')  # Pfad zum Bild anpassen
if image is None:
    print("Fehler: Bild konnte nicht geladen werden.")
    exit()

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000)
parameters = cv2.aruco.DetectorParameters()
corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)

# Schritt 3: Pose des Markers schätzen
if ids is not None and 52 in ids:
    index = np.where(ids == 52)[0][0]  # Index des Markers mit ID 52
    rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
        corners[index], 0.05, camera_matrix, dist_coeffs
    )

    # Schritt 4: Koordinaten eines Punktes im Marker-Koordinatensystem
    point = np.array([[0], [0], [0]], dtype=np.float64)  # Punkt im Marker (z.B. Zentrum)
    rotated_point = cv2.Rodrigues(rvecs[0])[0] @ point + tvecs[0].reshape(3, 1)

    print(f"Koordinaten des Punkts für Marker {ids[index][0]}: {rotated_point.flatten()}")

# Marker-Konturen zeichnen
cv2.aruco.drawDetectedMarkers(image, corners, ids)

# Bild anzeigen
cv2.imshow('Bild mit ArUco-Markern', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

