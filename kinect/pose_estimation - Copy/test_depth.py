import freenect

#Test to get the depth data from the Kinect

depth,_ = freenect.sync_get_depth()
print(depth)
