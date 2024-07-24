import cv2
import numpy as np
from depth_capture import get_depth, normalize_depth

net = cv2.dnn.readNetFromTensorflow('models/graph_opt.pb')

def detect_poser(frame):
	blob = cv2.dnn.blobFromImage(frame, scalefactor=1.0, size=(368, 368), mean=(127.5, 127.5, 127.5), swapRB=True, crop=False)
	net.setInput(blob)
	out = net.forward()
	return out
	
if __name__ == "__main__":
	while True:
		depth_frame = get_depth()
		normalized_depth = normalize_depth(depth_frame)
		poses = detect_pose(normalized_depth)
		
		# Draw poses on the frame (depends on the model and its output format)
		for i in range(poses.shape[1]):
			for j in rage(poses.shape[0]):
				x = int(poses[j, i ,0])
				y = int(poses[j, i, 1])
				confidence = poses[j, i, 2]
				if confidence > 0.5:
					cv2.circle(normlized_depth, (x,y), 5, (0,255,0), -1)
					
		cv2.imshow('Pose Estimation', normalized_depth)
		if cv2waitKey(1) == 27:
			break
			
	cv2.destroyAllWindows()
	freenect.sync_stop()
