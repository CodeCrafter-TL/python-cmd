<!-- Best_README_template -->

# Python cmd

A GUI terminal by Python3.

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />

<p align="center">
  <h3 align="center">最像 Windows 11 终端的整活项目</h3>
  <p align="center">
    您可以通过目录中的信息来使用它。
    <br />
    <br />
    <a href="https://github.com/codecrafter-tl/python-cmd">查看本仓库</a>
    ·
    <a href="https://github.com/codecrafter-tl/python-cmd/issues">报告 Bug 或提出特性</a>
    ·
    <a href="https://github.com/codecrafter-tl/python-cmd/pulls">提出拉取请求</a>
  </p>


## 目录

- [上手指南](#上手指南)
- [文件说明](#文件说明)
- [作者](#作者)

### 上手指南
1. 在 GitHub 中下载最新的 [Release](https://github.com/CodeCrafter-TL/python-cmd/releases) 。

2. 在工作目录中执行如下命令:
```bash
git clone https://github.com/CodeCrafter-TL/python-cmd.git
```
#### 安装必需包
在 clone 之后的工作目录中执行如下命令:
```bash
pip3 install -r requirements.txt
```
如果安装较慢，可以使用如下命令切换为阿里云镜像:
```bash
pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple
```
等待安装完成后，使用如下命令即可开始使用 Python cmd:
```bash
python3 main.py
```

#### 日志说明
日志存放位于`C:\users\你的用户名\.pcmd`下
#### Warning!
- 无法自定义日志位置
- cd 有部分问题 例子：
```bash
cd c:\
unterminated string literal (detected at line 1); perhaps you escaped the end quote? (<string>, line 1)
```
请使用
```bash
cd c:\\
```

### 文件说明

```
python-cmd-main
├── README.md
├── LICENSE.txt
├── ui.py
├── main.py
├── constants.py
```
> `README.md`: 您正在阅读的帮助文档

> `LICENSE.txt`: 关于此项目的 MIT License 信息

> `ui.py`: 由 PyQt5 UI code generator 生成的 UI 代码

> `main.py`: 主程序文件

> `constants.py`: 必需的程序字符串信息

### 作者

![mail-qq](https://img.shields.io/badge/email_qq-1825456084@qq.com-aqua)

![mail-163](https://img.shields.io/badge/email_163-CodeCrafterTL@163.com-red)

![github](https://img.shields.io/badge/GitHub-CodeCrafterTL-green?logo=github)

*您也可以在贡献者名单中参看所有**参与该项目的开发者**。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/codecrafter-tl/python-cmd//LICENSE.txt)

[project-path]:codecrafter-tl/python-cmd
[contributors-shield]: https://img.shields.io/github/contributors/codecrafter-tl/python-cmd.svg?style=square
[contributors-url]: https://github.com/codecrafter-tl/python-cmd/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/codecrafter-tl/python-cmd.svg?style=square
[forks-url]: https://github.com/codecrafter-tl/python-cmd/network/members
[stars-shield]: https://img.shields.io/github/stars/codecrafter-tl/python-cmd.svg?style=square
[stars-url]: https://github.com/codecrafter-tl/python-cmd/stargazers
[issues-shield]: https://img.shields.io/github/issues/codecrafter-tl/python-cmd.svg?style=square
[issues-url]: https://img.shields.io/github/issues/codecrafter-tl/python-cmd.svg
[license-shield]: https://img.shields.io/github/license/codecrafter-tl/python-cmd.svg?style=square
[license-url]: https://github.com/codecrafter-tl/python-cmd/blob/master/LICENSE.txt
