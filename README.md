# file
文件上传，下载，分享，删除

# 运行步骤
先修改setting配置文件的数据库自己的ipV4地址， 数据库密码是：123456
1. 首先在电脑上安装docker，在终端输入：  docker-compose -v
2. 如果有显示类似于： docker-compose version 1.29.2, build 5becea4c， 则说明安装成功
3. 在终端进入项目所在目录， 找到docker-compose.yml，运行，docker-compose up -d
4. 即可启动项目，在docker的界面，可以看到相关的容器
5. 容器运行成功以后，需要重启一下wgjl容器
6. 如上述启动成功，浏览器访问：127.0.0.1:8000,  用户名：admin  密码：123456
