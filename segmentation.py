# Python code for basic image segmentation without using standard libraries

def threshold_segmentation(image, threshold):
    """
        Segment the image based on a simple threshold.
        
        Parameters:
        - image (list of list of int): A 2D grayscale image where each value represents the pixel intensity.
        - threshold (int): The threshold value for segmentation.
        
        Returns:
        - segmented_image (list of list of int): A 2D binary image where pixels above the threshold are 1 and others are 0.
        """
    height = len(image)
    width = len(image[0]) if height > 0 else 0
    
    # Initialize the segmented image with zeros
    segmented_image = [[0 for _ in range(width)] for _ in range(height)]
    
    # Apply the threshold to each pixel
    for i in range(height):
        for j in range(width):
            if image[i][j] > threshold:
                segmented_image[i][j] = 1

return segmented_image

# Example usage:
# Let's create a simple 5x5 image with pixel values ranging from 0 to 255
example_image = [
                 [0, 30, 60, 120, 180],
                 [25, 50, 125, 190, 200],
                 [30, 80, 130, 200, 210],
                 [35, 90, 140, 210, 220],
                 [40, 100, 150, 220, 230]
                 ]

# We will use a threshold value of 100 for segmentation
threshold_value = 100
segmented = threshold_segmentation(example_image, threshold_value)

