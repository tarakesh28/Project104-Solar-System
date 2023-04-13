import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",                    #Text
            (90,75),                  #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            2.75,                      #Scale
            (255,255,255)             #RGB Color Value
            )

cv2.putText(img,
            "Mercury",                #Text
            (110,245),                #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            0.53,                     #Scale
            (255,255,255)             #RGB Color Value
            )

cv2.putText(img,
            "Venus",                  #Text
            (190,265),                #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            0.57,                     #Scale
            (255,255,255)             #RGB Color Value
            )

cv2.putText(img,
            "Earth",                    #Text
            (285,270),                #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            0.6,                        #Scale
            (255,250,0)             #RGB Color Value
            )

cv2.putText(img,
            "Mars",                    #Text
            (380,260),                #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            0.6,                        #Scale
            (255,255,255)             #RGB Color Value
            )

cv2.putText(img,
            "Jupiter",                    #Text
            (550,390),                #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            1,                        #Scale
            (255,255,255)             #RGB Color Value
            )

cv2.putText(img,
            "Saturn",                    #Text
            (745,320),                #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            0.9,                        #Scale
            (255,255,255)             #RGB Color Value
            )

cv2.putText(img,
            "Uranus",                    #Text
            (950,300),                #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            0.75,                        #Scale
            (255,255,255)             #RGB Color Value
            )

cv2.putText(img,
            "Neptune",                    #Text
            (1100,295),                #Position
            cv2.FONT_HERSHEY_TRIPLEX, #Font
            0.7,                        #Scale
            (255,255,255)             #RGB Color Value
            )

cv2.imshow("Solar System", img)
cv2.waitKey(0)

cv2.imwrite("named_solar_system.jpg", img)