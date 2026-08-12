# 你的第一个AI程序！
# 每一行我都写了注释，看不懂没关系，先跑起来再说！

# 第一步：导入需要的工具库
from openai import OpenAI

# ======================
# 你需要改这里！
# 把下面的"你的API_KEY"换成你自己的OpenAI API Key
# 比如：api_key = "sk-abcdef123456....."
# ======================
client = OpenAI(
    api_key = "你的API_KEY",  # TODO: 换成你的Key
    base_url = "https://api.openai.com/v1"  # 如果你用代理或第三方中转，改这里
)

# 打印欢迎信息
print("=" * 50)
print("🎉 你的第一个AI程序启动成功！")
print("输入你想说的话，和AI聊天吧！")
print("输入 'quit' 退出程序")
print("=" * 50)

# 聊天历史记录，让AI记得之前说过什么
messages = [
    {"role": "system", "content": "你是一个友好的编程助手，专门帮助大一新生学习C语言和编程知识，回答要简单易懂，不要用太专业的术语。"}
]

# 无限循环，一直聊天直到用户输入quit
while True:
    # 获取用户输入
    user_input = input("\n你：")
    
    # 如果用户输入quit，退出
    if user_input.lower() == "quit":
        print("👋 再见！")
        break
    
    # 把用户的话加到历史记录里
    messages.append({"role": "user", "content": user_input})
    
    # 调用AI！这是最核心的一行
    print("\nAI正在思考...")
    response = client.chat.completions.create(
        model = "gpt-4o-mini",  # 用最便宜又好用的模型，足够你玩了
        messages = messages,
        temperature = 0.7
    )
    
    # 拿到AI的回复
    ai_reply = response.choices[0].message.content
    
    # 把AI的回复也加到历史记录里，这样它就能记得上下文了
    messages.append({"role": "assistant", "content": ai_reply})
    
    # 打印AI的回复
    print(f"\nAI：{ai_reply}")
