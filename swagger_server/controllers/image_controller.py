import os

import connexion
import imaginairy
from imaginairy import ImaginePrompt, LazyLoadingImage, imagine_image_files, WeightedPrompt, imagine

from swagger_server.models.image_info import ImageInfo  # noqa: E501


def generate_ai_image(body=None):
    if connexion.request.is_json:
        body = ImageInfo.from_dict(connexion.request.get_json())  # noqa: E501
        print("before body=", body)
        body = request_none_able(body)
        print("after body=", body)

    print("#1 prompt=", body.prompt)

    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Thomas_Cole_-_Architect%E2%80%99s_Dream_-_Google_Art_Project.jpg/540px-Thomas_Cole_-_Architect%E2%80%99s_Dream_-_Google_Art_Project.jpg"
    prompts = [
        ImaginePrompt(body.prompt, seed=1, upscale=True),
        #ImaginePrompt("a scenic landscape", seed=1, upscale=True),
        # ImaginePrompt("a bowl of fruit"),
        #ImaginePrompt([
        #    WeightedPrompt("cat", weight=1),
        #    WeightedPrompt("rabbit", weight=1),
        #]),
        #ImaginePrompt(
        #    "a spacious building",
        #    init_image=LazyLoadingImage(url=url)
        #),
        # ImaginePrompt(
        #     "a bowl of strawberries",
        #     init_image=LazyLoadingImage(filepath="mypath/to/bowl_of_fruit.jpg"),
        #     mask_prompt="fruit OR stem{*2}",  # amplify the stem mask x2
        #     mask_mode="replace",
        #     mask_modify_original=True,
        # ),
        # ImaginePrompt("strawberries", tile_mode=True),
    ]

    for result in imagine(prompts):
        generated_imgs_path = os.path.join("./generatedImages", "generated")
        os.makedirs(generated_imgs_path, exist_ok=True)
        base_count = len(os.listdir(generated_imgs_path))

        filename = f"{base_count:08}_S{body.seed}_step{body.steps}_{body.prompt}.jpg"
        print("save to ", filename)
        result.save(filename)
        f = open(filename, 'rb')
        cont = f.read()
        f.close()

    # or
    # imagine_image_files(prompts, outdir="./my-art2")

    return cont


def request_none_able(request):
    if request.model == "None":
        request.model = None
    if request.prompt == "None":
        request.prompt = None
    if request.init_image == "None":
        request.init_image = None
    if request.mask_prompt == "None":
        request.mask_prompt = None
    if request.mask_image == "None":
        request.mask_image = None
    if request.seed == 0:
        request.seed = None
    if request.steps == 0:
        request.steps = None
    if request.height == "None":
        request.height = None
    if request.width == "None":
        request.width = None
    if request.conditioning == "None":
        request.conditioning = None
    if request.tile_mode == "":
        request.tile_mode = None

    if request.negative_prompt == "None":
        request.negative_prompt = imaginairy.schema.config.DEFAULT_NEGATIVE_PROMPT

    return request
