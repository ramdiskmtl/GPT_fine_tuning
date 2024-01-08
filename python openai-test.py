
# 导入OpenAI模块
from openai import OpenAI

# 创建OpenAI客户端
client = OpenAI()

# 创建聊天会话，使用GPT-3.5-turbo模型，并传入两个消息
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem in Chinese that explains the concept of recursion in programming."}
  ]
)

# 打印出第一个选择的消息
print(completion.choices[0].message)