cmake_read:可以将一个caffemodel转换成txt文件；在caffe目录里 cmake .   make
camke_write:将prototxt转换成caffemodel
out_data.py:将tensorflowmodel数据按层写出
seg_layers.py:将train.prototxt按层写到各个文件里
data_mod.py:为了在数据文件最后一行添加 “}”
ss.sh:将layer和data写到一个model.prototxt