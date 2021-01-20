本文件夹包含两种实现的方式：

面向过程：
employee_system.py是一个单独的文件，且没有保存数据至文本（本地）。

面向对象：
employee.py、system.py、main.py是一个整体框架，且保存数据至本地，也可读取。
employee.py是一个定义员工对象的文件，单独出来；
system.py是框架操作系统文件，包含了主要的程序代码；
main.py内运行框架程序，也可在system.py内运行（最好不要）。
