import freenect
import cv2
import numpy as np

def get_depth():
	depth, _ = freenect.sync_get_depth()
	depth = depth.astype(np.uint8)
	return depth
	
def normalize_depth(depth):
	depth = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
	depth = cv2.convertScaleAbs(depth)
	return depth
	
if __name__ == "__main__":
	while True:
		depth_frame = get_depth()
		normalized_depth = normalize_depth(depth_frame)
		cv2.imshow('Normalized Depth', normalized_depth)
		if cv2.waitKey(1) == 27:
			break
		
	cv2.destroyAllWindows()
	freenect.sync_stop()
