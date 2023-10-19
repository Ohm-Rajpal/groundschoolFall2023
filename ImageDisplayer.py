import cv2

# Custom function to reduce pain in the future
def show_img_custom(cv_img, name='cv_img'):
    cv2.imshow(name, cv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()