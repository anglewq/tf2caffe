cmake_minimum_required (VERSION 2.8) 
project (pt_test) 
add_executable(pt_test pt.cpp) 
include_directories ( /home/wq/video-caffe/include 
	/usr/local/include 
	/usr/local/cuda/include 
	/usr/include ) 
target_link_libraries(pt_test 
	/home/wq/video-caffe/build/lib/libcaffe.so 
	/usr/lib/x86_64-linux-gnu/libglog.so 
	/usr/lib/x86_64-linux-gnu/libboost_system.so )

