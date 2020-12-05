import cv2 as cv


# Input Image
img = cv.imread("G:\Google\Madarek\Resume\CDRs\Pistachio Sorter By Ali\Basler images/3.jpg")

print(img.shape)
fromCenter = False

while True:
    Boundaries = []
    while 0xff != ord("q"):
        # Select ROI
        ROI_bounding = cv.selectROI("Image", img, fromCenter)
        Boundaries.append(ROI_bounding)
        print(ROI_bounding)
        # To Finish the selection process.
        if cv.waitKey(10) & 0xff == ord("q"):
            break

    print("Boundaries are: ", Boundaries)
    for ROI_bounding in Boundaries:
        ROI = img[int(ROI_bounding[1]):int(ROI_bounding[1] + ROI_bounding[3]), int(ROI_bounding[0]):int(ROI_bounding[0] + ROI_bounding[2])]
        cv.imshow("ROI"+str(ROI_bounding), ROI)
        cv.waitKey(10)

