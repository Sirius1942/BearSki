# BearSki 自动化测试框架

## 简介
BearSki 是一个自动化测试的基础框架。提供项目在自动化测试应用中遇到的一些通用问题的解决方案。降低测试用例编写难度，提升自动化测试用例的可维护性。


## 功能清单
#### 【已完成】
* 基于unittest编辑测试用例的编辑，提供基于关键字驱动的测试步骤书写方法 ；
* 封装 RobotFramework 的驱动调用方法，可以直接调用 rf 的驱动类执行相关测试；
* 提供命令行及配置文件的用例执行调用方式；
* 提供统一的日志输出；
* 提供基于Bootstrap-table 单文件测试报告。
#### 【待开发】
* 通用结果过滤器；
* 基于数据表的测试数据管理功能；
* 用例、关键字、测试数据测试执行监控功能。
## 快速开始
1、安装
```bash
pip install BearSki
```
2、生成测试项目
```bash
siriusdeMacBook:src sirius$ python
Python 3.6.0 |Anaconda 4.3.0 (x86_64)| (default, Dec 23 2016, 13:19:00) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from BearSki import Manager
>>> Manager.create_project('testproject')
[2019-12-05 11:34:42,731] [INFO] [BearSki.createproject] 开始创建测试项目
[2019-12-05 11:34:42,734] [INFO] [BearSki.createproject] 测试项目创建完成
>>> exit()
```
3、控制台输出模式执行用例
```bash
src sirius$ cd testproject
testproject sirius$ python runtest.py 
```
4、测试报告模式执行用例
```bash
testproject sirius$ python runtest.py -f config.json
```
5、查看测试报告

![](img/2019-12-05-12-11-34.png)


## 问题交流与反馈
邮箱：chen6_9@163.com 或在github上直接题问题单


