import StableDiffusion
import ChatGPT


article = 'bird'
enhanced_article = ChatGPT.enhance_article(article)
print('1',enhanced_article)
image_prompt = ChatGPT.generate_prompt_for_image_generation(
        enhanced_article)
print('2',image_prompt)
generated_image = StableDiffusion.generate_image(image_prompt)
print('3',generated_image)