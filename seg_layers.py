import os

def write_txt(data,filename):
    with open(filename,"w") as f:
        for i in range(len(data)):
            f.write(data[i])


prototxt="train.prototxt"
file="layer"
layer=[]
write=False
filename="1.txt"
with open(prototxt,'r') as f:
    lines=f.readlines()
    for line in lines:
        if "name" in line:
            _,name=line.split(":")
            filename=line.split('"')[1]
            filename="{}/{}.prototxt".format(file,filename)
        if "NdConvolution" in line:
            write=True
        if "layer" in line:
            if write:
                if "}" not in layer[-1]:
                    layer.pop()
                    layer.pop()
                else:
                    layer.pop()
                write_txt(layer,filename)
                write=False

            layer.clear()

        layer.append(line)