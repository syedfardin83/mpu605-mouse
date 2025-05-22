import serial
from datetime import datetime

mpu = serial.Serial('COM3',115200)
log_file_name = f'logs/{str(datetime.now()).replace('.',';').replace(':',';')}.csv'
with open(log_file_name,'w') as f:
    f.write('AccelX,AccelY,AccelZ,GyroX,GyroY,GyroZ')

while True:
    line = mpu.readline().decode('utf-8')
    # print("here")
    # print(type(line))

    a = line.strip().split(',')
    b=[]
    for i in a:
        try:
            b.append(float(i))
        except Exception as e:
            print(e)
            pass
    print(b)
    with open(log_file_name,'a') as f:
        if b==[]:
            pass
        else:
            string = ""
            for i in b:
                if string=="":
                    string=str(i)
                else:
                    string=string+","+str(i)
            f.write('\n'+string)
