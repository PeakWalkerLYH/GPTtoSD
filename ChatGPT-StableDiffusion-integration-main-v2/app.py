from flask import Flask, render_template, request
import ChatGLM
import WenXin


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def scrape():
    article = request.get_json()['article']
    # enhanced_article = ChatGPT.enhance_article(article)
    enhanced_article = ChatGLM.enhance_article(article)
    # image_prompt = ChatGPT.generate_prompt_for_image_generation(enhanced_article)
    image_prompt = ChatGLM.generate_prompt_for_image_generation(enhanced_article)
    # generated_image = StableDiffusion.generate_image(image_prompt)
    generated_image = WenXin.get_picture(image_prompt)
    return render_template('result.html', article=article, enhanced=enhanced_article, img_url=generated_image, image_prompt=image_prompt)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)