import os

def write_txt(data,filename):
    with open(filename,"w") as f:
        for i in range(len(data)):
            f.write(data[i])

datapath="/home/wq/桌面/python-code/rgb_scratch"
savepath="/home/wq/桌面/python-code/model/datas"

filedir=os.listdir(datapath)
for subdir in filedir:
    os.chdir(datapath)
    data=[]
    if subdir.endswith("w.prototxt"):
        with open(subdir) as f:
            lines=f.readlines()
            for line in lines:
                data.append(line)
        data.append("}\n")
        os.chdir(savepath)
        write_txt(data,subdir)
        data.clear()

