import os
import zhipuai
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

zhipuai.api_key = os.getenv('CHATGLM_API_KEY')
CHATGLM_MODEL = "chatglm_turbo"


def enhance_article(article):
    print("第一阶段进行，优化文章中......")
    # 4. 如果出现了具体的人，那么需要着重对人物外貌细节的描写，以及动作的描写。
    response = zhipuai.model_api.sse_invoke(
        model=CHATGLM_MODEL,
        prompt=[
            {
                "role": "system",
                "content": f"""请将给定的文本进行优化改进而生成新的文本，遵循如下规则：
                1. 对文本进行扩写，保证语法的正确、句子的连贯性和文本整体可读性。
                2. 请不要对原文本的重要信息删除或更改。
                3. 尽量保持与原文的含义接近。
                4. 不超过100个字
                ```
                {article}
                ```
                """
            },
        ]
    )

    print("第一阶段完成！已生成短文！")
    result = ''
    for event in response.events():
        result += event.data

    return result


def generate_prompt_for_image_generation(article):
    print("第二阶段进行，文章总结中......")
    response = zhipuai.model_api.sse_invoke(
        model=CHATGLM_MODEL,
        prompt=[
            {
                "role": "system",
                "content": f"""将给定的文本进行提炼，输出适合 stable diffusion 软件的图像生成的prompt提示词，遵循如下规则：
                1. 以便于根据提示词能够生成相应文本的完整图像
                2. 生成提示词时，去掉'提示词'这三个字而直接显示提示词
                3. 生成提示词时，去掉包含'作品'这两个字的提示词
                4. 生成提示词时，请单独加入'全景'作为一个提示词
                5. 不超过100个字
                ```
                {article}
                ```
                """
            },
        ]
    )

    print("第二阶段完成！已提取出图像提示词")
    result = ''
    for event in response.events():
        result += event.data

    return result
