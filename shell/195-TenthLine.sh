#文件不足10行时应该不显示

#思路一 head获取前10行再输出最后一行,但是这种方法不足10行时会显示最后一行
# head -n 10 file.txt|tail -n 1

#思路二 awk
awk 'NR==10' file.txt

#思路三 sed
sed -n '10{p;q}' file.txt