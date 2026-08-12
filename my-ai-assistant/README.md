# 🚀 你的第一个AI助手项目

## ⚠️ 重要：把项目移到D盘

我已经帮你在D盘创建了 `D:\Projects\my-ai-assistant` 文件夹，你现在只需要：
1. 打开文件夹：`C:\Users\李云豪\AppData\Roaming\TRAE SOLO CN\ModularData\ai-agent\work-mode-projects\6a7af8d5f8e908493d623f0e\my-ai-assistant`
2. 把里面的 `01_hello_ai.py` 和 `README.md` 两个文件**剪切**到 `D:\Projects\my-ai-assistant` 文件夹里
3. 之后所有操作都在D盘这个文件夹里进行就可以了！

---

## 第一步：安装Python（5分钟）

1. 打开浏览器，访问：https://www.python.org/downloads/release/python-3124/
2. 往下滑，找到 "Files" 部分，下载 **Windows installer (64-bit)**
3. 双击安装包！**重点：一定要勾选最下面的 "Add Python.exe to PATH"**，然后点 "Install Now"
4. 安装完之后，按Win+R，输入`cmd`打开命令提示符，输入`python --version`，如果显示`Python 3.12.x`就说明装好了

## 第二步：获取OpenAI API Key

1. 访问 https://platform.openai.com/ 注册/登录账号
2. 右上角头像 → View API Keys → Create new secret key
3. 复制保存好你的Key（只显示一次！）
4. 往账号里充5美元就够你用很久了（gpt-4o-mini非常便宜）

如果访问OpenAI有困难，可以用国内的中转服务，或者直接用Claude，我后面教你改。

## 第三步：安装依赖库

打开命令提示符（cmd），输入：
```bash
pip install openai
```

## 第四步：运行你的第一个AI程序！

1. 用记事本或者VS Code打开 `D:\Projects\my-ai-assistant\01_hello_ai.py`
2. 找到第14行，把`"你的API_KEY"`换成你刚才拿到的API Key
3. 在命令提示符里，进入D盘的项目文件夹：
   ```bash
   D:
   cd D:\Projects\my-ai-assistant
   ```
4. 运行程序：
   ```bash
   python 01_hello_ai.py
   ```

成功的话你就能看到欢迎界面，直接和AI聊天了！🎉

## 测试一下

你可以问它：
- "C语言里指针到底是什么？用大白话讲"
- "帮我看看这段代码有什么问题：#include <stdio.h> int main() { int a = 5; printf("%d", a); return 0; }"
- "给我出一道C语言for循环的练习题"

遇到任何问题随时问我！
