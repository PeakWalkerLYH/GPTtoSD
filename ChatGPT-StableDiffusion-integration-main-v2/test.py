import requests
import json
import time

API_KEY = "GD3uiAVFyHgmwK55RCLo0OZH"
SECRET_KEY = "zMrk4TtjEnf74LdqlYfwHeax3rlGVacp"


def post_message(prompt):
    # post
    url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/txt2img?access_token=" + get_access_token()

    payload = json.dumps({
        "text": prompt,
        "resolution": "1024*1024",
        "style": "写实风格"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response1 = requests.request("POST", url, headers=headers, data=payload)
    # 使用 json() 方法获取 JSON 对象
    json_obj = response1.json()
    # 从 JSON 对象中取出 taskId 后的数字
    print(response1.text)
    task_id_number = json_obj['data']['taskId']

    # print(type(response1))  <class 'requests.models.Response'>
    return task_id_number


# request
def get_picture(prompt):
    t_id = post_message(prompt)
    url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/getImg?access_token=" + get_access_token()

    payload = json.dumps({"taskId": t_id})
    time.sleep(10)
    # print(payload)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response2 = requests.request("POST", url, headers=headers, data=payload)
    # 使用 json() 方法获取 JSON 对象
    json_obj = response2.json()
    # 从 JSON 对象中取出 taskId 后的数字
    image_url = json_obj['data']['imgUrls'][0]['image']

    # 返回图片url
    return image_url

# 获取access_token
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    get_picture('梵高')
