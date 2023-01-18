import os

import connexion
import imaginairy
from imaginairy import ImaginePrompt, LazyLoadingImage, imagine_image_files, WeightedPrompt, imagine
from swagger_server.models.image_info import ImageInfo  # noqa: E501


def generate_ai_image(body=None):
    if connexion.request.is_json:
        body = ImageInfo.from_dict(connexion.request.get_json())  # noqa: E501
        body = request_none_able(body)
        print("after body=", body)

    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Thomas_Cole_-_Architect%E2%80%99s_Dream_-_Google_Art_Project.jpg/540px-Thomas_Cole_-_Architect%E2%80%99s_Dream_-_Google_Art_Project.jpg"
    if body.weighted_prompt is None:
        prompts = [
            ImaginePrompt(prompt=body.prompt,
                          negative_prompt=body.negative_prompt,
                          prompt_strength=body.prompt_strength,
                          init_image=body.init_image,
                          init_image_strength=body.init_image_strength,
                          mask_prompt=body.mask_prompt,
                          mask_image=body.mask_image,
                          mask_mode=body.mask_mode,
                          mask_modify_original=body.mask_modify_original,
                          seed=body.seed,
                          steps=body.steps,
                          height=body.height,
                          width=body.width,
                          upscale=body.upscale,
                          fix_faces=body.fix_faces,
                          fix_faces_fidelity=body.fix_faces_fidelity,
                          sampler_type=body.sampler_type,
                          conditioning=body.conditioning,
                          tile_mode=body.tile_mode,
                          model=body.model
                          )
        ]
    else:
        weight_list = []  # list
        for i in body.weighted_prompt:
            weight_list.append(WeightedPrompt(i.name, i.weight))

        prompts = [ImaginePrompt(weight_list)]

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
    if request.height == 0:
        request.height = None
    if request.width == 0:
        request.width = None
    if request.conditioning == "None":
        request.conditioning = None
    if request.tile_mode == "":
        request.tile_mode = None

    if request.negative_prompt == "None":
        request.negative_prompt = imaginairy.schema.config.DEFAULT_NEGATIVE_PROMPT

    return request
