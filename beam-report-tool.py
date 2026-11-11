count=0
zongtiji=0
def save_summary(count,zongtiji):
    with open("summary.txt","w",encoding="utf-8") as file:
        file.write("无效梁数量：")
        file.write(str(count))
        file.write("\n")
        file.write("有效梁总体积：")
        file.write(str(zongtiji))
        file.write("立方米")
        file.write("\n")
try:
    with open("beam_data.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip()=="":
                continue
            parts = line.strip().split(",")
        
            if len(parts) == 4:
                print("资料数量正确")
                try:
                    chang=float(parts[1])
                    kuan=float(parts[2])
                    gao=float(parts[3])
                    if chang>0 and kuan>0 and gao>0:
                        tiji=chang*kuan*gao
                        print("梁编号：",parts[0],"梁体积：",tiji,"立方米")
                        zongtiji=zongtiji+tiji
                    else:
                        print("梁编号：",parts[0],"尺寸无效")
                        count=count+1
                except ValueError:
                    print(parts[0],"尺寸必须为数字")
                    count=count+1
            else:
                print(parts[0],"资料应有4项，实际有：", len(parts))
                count=count+1
except FileNotFoundError:
    print("找不到输入文件")
else:
    print("读取成功，可以继续处理")
    save_summary(count,zongtiji)
    print("文件已保存")    
    print("无效梁数量：",count)
    print("有效梁总体积：",zongtiji,"立方米")
    print("读取结束")
