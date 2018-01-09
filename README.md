这是[stackoverflow上面的一个答案](https://stackoverflow.com/questions/9496101/protocol-buffer-over-socket-in-c)
给出的示例，感谢题主和答主。
整理了一下代码，方便和我一样需要简单使用socket + protobuf的人学习。

运行方法：
```
# let $dir be your working directory
git clone https://github.com/shinezyy/proto-buf-socket.git $dir
cd $dir
mkdir build
cd $dir/build
cmake ..
make
```
然后开两个窗口，先运行server：
```
cd $dir/build
./server
```
再运行client：
```
cd $dir/build
./client
```


新增加了python作为socket服务器的demo：
```
cd $dir/build && make
cd $dir
ln -s ./build/msg_pb2.py .
```
然后开两个窗口，先运行server：
```
cd $dir
python3 server.py
```
再运行client：
```
cd $dir/build
./client
```
