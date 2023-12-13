import os
import cv2
import numpy as np

def check_forgery(original_image_path, altered_image_path):
    # Load images
    original_image = cv2.imread(original_image_path)
    altered_image = cv2.imread(altered_image_path)

    # Convert to YCrCb color space
    original_ycc = cv2.cvtColor(original_image, cv2.COLOR_BGR2YCrCb)
    altered_ycc = cv2.cvtColor(altered_image, cv2.COLOR_BGR2YCrCb)

    # Calculate mean absolute differences
    original_y, original_cr, original_cb = cv2.split(original_ycc)
    altered_y, altered_cr, altered_cb = cv2.split(altered_ycc)

    # Apply a median filter to the luminance channel to reduce noise
    original_y = cv2.medianBlur(original_y, 5)
    altered_y = cv2.medianBlur(altered_y, 5)

    y_diff = np.abs(original_y.astype('int') - altered_y.astype('int'))
    cr_diff = np.abs(original_cr.astype('int') - altered_cr.astype('int'))
    cb_diff = np.abs(original_cb.astype('int') - altered_cb.astype('int'))

    avg_diff = np.mean(y_diff) + np.mean(cr_diff) + np.mean(cb_diff)

    # Print the average difference
    print("Average difference: ", avg_diff)

    # A difference greater than 100 indicates possible forgery
    if avg_diff > 50:
        print("The image might be a forgery.")
    else:
        print("The image is likely authentic.")

if __name__ == "__main__":
    # Provide paths to original and altered images
    original_image_path = "C:/Users/Imran/OneDrive/Desktop/affanX/32_original.jpg"
    altered_image_path = "C:/Users/Imran/OneDrive/Desktop/affanX/32_forged.jpg"

    check_forgery(original_image_path, altered_image_path)