filename="data.txt"
myfile=open(filename)
myfile.seek(0)
data=[]

x=myfile.readline()
while x != '':
    ll = []
    for i in x.split(): # split(' ') split(',') ...
        if i<='': continue
        ll.append( float(i) )
    data.append( ll )
    x=myfile.readline()

print data



# cat data.txt
#   3.0    3.0    3.0    3.0    3.0    3.0   35.0   45.0
#  53.0   55.0   58.0  113.0  113.0   86.0   67.0   90.0
#   3.5    3.5    4.0    4.0    4.5    4.5   46.0   59.0
#  63.0   58.0   58.0  125.0  126.0  110.0   78.0   97.0
#   4.0    4.0    4.5    4.5    5.0    5.0   48.0   60.0
#  68.0   65.0   65.0  123.0  123.0  117.0   87.0  108.0
#   5.0    5.0    5.0    5.5    5.5    5.5   46.0   63.0
#  70.0   64.0   63.0  116.0  119.0  115.0   97.0  112.0
#   6.0    6.0    6.0    6.0    6.5    6.5   51.0   69.0
#  77.0   70.0   71.0  120.0  122.0  122.0   96.0  123.0
#  11.0   11.0   11.0   11.0   11.0   11.0   64.0   75.0
#  81.0   79.0   79.0  112.0  114.0  113.0   98.0  115.0
#  20.0   20.0   20.0   20.0   20.0   20.0   76.0   86.0
#  93.0   92.0   91.0  104.0  104.5  107.0   97.5  104.0
#  30.0   30.0   30.0   30.0   30.1   30.2   84.0   96.0
#  98.0   99.0   96.0  101.0  102.0   99.0   94.0   99.0
#  30.0   33.4   36.8   40.0   43.0   45.6  100.0  106.0
# 106.0  108.0  101.0   99.0   98.0   99.0   95.0   95.0
#  42.0   44.0   46.0   48.0   50.0   51.0  109.0  111.0
# 110.0  110.0  103.0   95.5   95.5   95.0   92.5   92.0
#  60.0   61.7   63.5   65.5   67.3   69.2  122.0  124.0
# 124.0  121.0  103.0   93.2   92.5   92.2   90.0   90.8
#  70.0   70.1   70.2   70.3   70.4   70.5  137.0  132.0
# 134.0  128.0  101.0   91.7   90.2   88.8   87.3   85.8
#  78.0   77.6   77.2   76.8   76.4   76.0  167.0  159.0
# 152.0  144.0  103.0   89.8   87.7   85.7   83.7   81.8
#  98.9   97.8   96.7   95.5   94.3   93.2  183.0  172.0
# 162.0  152.0  102.0   87.5   85.3   83.3   81.3   79.3
# 160.0  157.0  155.0  152.0  149.0  147.0  186.0  175.0
# 165.0  156.0  120.0   87.0   84.9   82.8   80.8   79.0
# 272.0  266.0  260.0  254.0  248.0  242.0  192.0  182.0
# 170.0  159.0  131.0   88.0   85.8   83.7   81.6   79.6
# 382.0  372.0  362.0  352.0  343.0  333.0  205.0  192.0
# 178.0  166.0  138.0   86.2   84.0   82.0   79.8   77.5
# 770.0  740.0  710.0  680.0  650.0  618.0  226.0  207.0
# 195.0  180.0  160.0   82.9   80.2   77.7   75.2   72.7
