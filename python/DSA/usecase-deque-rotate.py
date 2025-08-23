from collections import deque

images = deque(["img1", "img2", "img3", "img4"])

print("Carousel has 4 images: ", images)

# Rotate Right:
images.rotate(1)
print("After first right rotation: ", images)

# Skippin 2 images forward
images.rotate(2)
print("After skipping 2 images forward: ", images)

# Left Roatate:
images.rotate(-1)
print("After first left rotation: ", images)

# Skippin 2 images backward
images.rotate(-2)
print("After skipping 2 images backward: ", images)