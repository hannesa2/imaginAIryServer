# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.weighted_prompt import WeightedPrompt  # noqa: F401,E501
from swagger_server import util


class ImageInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, prompt: str=None, negative_prompt: str=None, prompt_strength: float=None, init_image: str=None, init_image_strength: float=None, mask_prompt: str=None, mask_image: str=None, mask_mode: str=None, mask_modify_original: bool=None, steps: int=None, height: str=None, width: str=None, fix_faces: bool=None, fix_faces_fidelity: str=None, sampler_type: str=None, conditioning: str=None, model: str=None, seed: int=None, upscale: bool=None, tile_mode: bool=None, weighted_prompt: List[WeightedPrompt]=None):  # noqa: E501
        """ImageInfo - a model defined in Swagger

        :param prompt: The prompt of this ImageInfo.  # noqa: E501
        :type prompt: str
        :param negative_prompt: The negative_prompt of this ImageInfo.  # noqa: E501
        :type negative_prompt: str
        :param prompt_strength: The prompt_strength of this ImageInfo.  # noqa: E501
        :type prompt_strength: float
        :param init_image: The init_image of this ImageInfo.  # noqa: E501
        :type init_image: str
        :param init_image_strength: The init_image_strength of this ImageInfo.  # noqa: E501
        :type init_image_strength: float
        :param mask_prompt: The mask_prompt of this ImageInfo.  # noqa: E501
        :type mask_prompt: str
        :param mask_image: The mask_image of this ImageInfo.  # noqa: E501
        :type mask_image: str
        :param mask_mode: The mask_mode of this ImageInfo.  # noqa: E501
        :type mask_mode: str
        :param mask_modify_original: The mask_modify_original of this ImageInfo.  # noqa: E501
        :type mask_modify_original: bool
        :param steps: The steps of this ImageInfo.  # noqa: E501
        :type steps: int
        :param height: The height of this ImageInfo.  # noqa: E501
        :type height: str
        :param width: The width of this ImageInfo.  # noqa: E501
        :type width: str
        :param fix_faces: The fix_faces of this ImageInfo.  # noqa: E501
        :type fix_faces: bool
        :param fix_faces_fidelity: The fix_faces_fidelity of this ImageInfo.  # noqa: E501
        :type fix_faces_fidelity: str
        :param sampler_type: The sampler_type of this ImageInfo.  # noqa: E501
        :type sampler_type: str
        :param conditioning: The conditioning of this ImageInfo.  # noqa: E501
        :type conditioning: str
        :param model: The model of this ImageInfo.  # noqa: E501
        :type model: str
        :param seed: The seed of this ImageInfo.  # noqa: E501
        :type seed: int
        :param upscale: The upscale of this ImageInfo.  # noqa: E501
        :type upscale: bool
        :param tile_mode: The tile_mode of this ImageInfo.  # noqa: E501
        :type tile_mode: bool
        :param weighted_prompt: The weighted_prompt of this ImageInfo.  # noqa: E501
        :type weighted_prompt: List[WeightedPrompt]
        """
        self.swagger_types = {
            'prompt': str,
            'negative_prompt': str,
            'prompt_strength': float,
            'init_image': str,
            'init_image_strength': float,
            'mask_prompt': str,
            'mask_image': str,
            'mask_mode': str,
            'mask_modify_original': bool,
            'steps': int,
            'height': str,
            'width': str,
            'fix_faces': bool,
            'fix_faces_fidelity': str,
            'sampler_type': str,
            'conditioning': str,
            'model': str,
            'seed': int,
            'upscale': bool,
            'tile_mode': bool,
            'weighted_prompt': List[WeightedPrompt]
        }

        self.attribute_map = {
            'prompt': 'prompt',
            'negative_prompt': 'negative_prompt',
            'prompt_strength': 'prompt_strength',
            'init_image': 'init_image',
            'init_image_strength': 'init_image_strength',
            'mask_prompt': 'mask_prompt',
            'mask_image': 'mask_image',
            'mask_mode': 'mask_mode',
            'mask_modify_original': 'mask_modify_original',
            'steps': 'steps',
            'height': 'height',
            'width': 'width',
            'fix_faces': 'fix_faces',
            'fix_faces_fidelity': 'fix_faces_fidelity',
            'sampler_type': 'sampler_type',
            'conditioning': 'conditioning',
            'model': 'model',
            'seed': 'seed',
            'upscale': 'upscale',
            'tile_mode': 'tile_mode',
            'weighted_prompt': 'weightedPrompt'
        }
        self._prompt = prompt
        self._negative_prompt = negative_prompt
        self._prompt_strength = prompt_strength
        self._init_image = init_image
        self._init_image_strength = init_image_strength
        self._mask_prompt = mask_prompt
        self._mask_image = mask_image
        self._mask_mode = mask_mode
        self._mask_modify_original = mask_modify_original
        self._steps = steps
        self._height = height
        self._width = width
        self._fix_faces = fix_faces
        self._fix_faces_fidelity = fix_faces_fidelity
        self._sampler_type = sampler_type
        self._conditioning = conditioning
        self._model = model
        self._seed = seed
        self._upscale = upscale
        self._tile_mode = tile_mode
        self._weighted_prompt = weighted_prompt

    @classmethod
    def from_dict(cls, dikt) -> 'ImageInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ImageInfo of this ImageInfo.  # noqa: E501
        :rtype: ImageInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def prompt(self) -> str:
        """Gets the prompt of this ImageInfo.


        :return: The prompt of this ImageInfo.
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt: str):
        """Sets the prompt of this ImageInfo.


        :param prompt: The prompt of this ImageInfo.
        :type prompt: str
        """

        self._prompt = prompt

    @property
    def negative_prompt(self) -> str:
        """Gets the negative_prompt of this ImageInfo.


        :return: The negative_prompt of this ImageInfo.
        :rtype: str
        """
        return self._negative_prompt

    @negative_prompt.setter
    def negative_prompt(self, negative_prompt: str):
        """Sets the negative_prompt of this ImageInfo.


        :param negative_prompt: The negative_prompt of this ImageInfo.
        :type negative_prompt: str
        """

        self._negative_prompt = negative_prompt

    @property
    def prompt_strength(self) -> float:
        """Gets the prompt_strength of this ImageInfo.


        :return: The prompt_strength of this ImageInfo.
        :rtype: float
        """
        return self._prompt_strength

    @prompt_strength.setter
    def prompt_strength(self, prompt_strength: float):
        """Sets the prompt_strength of this ImageInfo.


        :param prompt_strength: The prompt_strength of this ImageInfo.
        :type prompt_strength: float
        """

        self._prompt_strength = prompt_strength

    @property
    def init_image(self) -> str:
        """Gets the init_image of this ImageInfo.


        :return: The init_image of this ImageInfo.
        :rtype: str
        """
        return self._init_image

    @init_image.setter
    def init_image(self, init_image: str):
        """Sets the init_image of this ImageInfo.


        :param init_image: The init_image of this ImageInfo.
        :type init_image: str
        """

        self._init_image = init_image

    @property
    def init_image_strength(self) -> float:
        """Gets the init_image_strength of this ImageInfo.


        :return: The init_image_strength of this ImageInfo.
        :rtype: float
        """
        return self._init_image_strength

    @init_image_strength.setter
    def init_image_strength(self, init_image_strength: float):
        """Sets the init_image_strength of this ImageInfo.


        :param init_image_strength: The init_image_strength of this ImageInfo.
        :type init_image_strength: float
        """

        self._init_image_strength = init_image_strength

    @property
    def mask_prompt(self) -> str:
        """Gets the mask_prompt of this ImageInfo.


        :return: The mask_prompt of this ImageInfo.
        :rtype: str
        """
        return self._mask_prompt

    @mask_prompt.setter
    def mask_prompt(self, mask_prompt: str):
        """Sets the mask_prompt of this ImageInfo.


        :param mask_prompt: The mask_prompt of this ImageInfo.
        :type mask_prompt: str
        """

        self._mask_prompt = mask_prompt

    @property
    def mask_image(self) -> str:
        """Gets the mask_image of this ImageInfo.


        :return: The mask_image of this ImageInfo.
        :rtype: str
        """
        return self._mask_image

    @mask_image.setter
    def mask_image(self, mask_image: str):
        """Sets the mask_image of this ImageInfo.


        :param mask_image: The mask_image of this ImageInfo.
        :type mask_image: str
        """

        self._mask_image = mask_image

    @property
    def mask_mode(self) -> str:
        """Gets the mask_mode of this ImageInfo.


        :return: The mask_mode of this ImageInfo.
        :rtype: str
        """
        return self._mask_mode

    @mask_mode.setter
    def mask_mode(self, mask_mode: str):
        """Sets the mask_mode of this ImageInfo.


        :param mask_mode: The mask_mode of this ImageInfo.
        :type mask_mode: str
        """

        self._mask_mode = mask_mode

    @property
    def mask_modify_original(self) -> bool:
        """Gets the mask_modify_original of this ImageInfo.


        :return: The mask_modify_original of this ImageInfo.
        :rtype: bool
        """
        return self._mask_modify_original

    @mask_modify_original.setter
    def mask_modify_original(self, mask_modify_original: bool):
        """Sets the mask_modify_original of this ImageInfo.


        :param mask_modify_original: The mask_modify_original of this ImageInfo.
        :type mask_modify_original: bool
        """

        self._mask_modify_original = mask_modify_original

    @property
    def steps(self) -> int:
        """Gets the steps of this ImageInfo.


        :return: The steps of this ImageInfo.
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps: int):
        """Sets the steps of this ImageInfo.


        :param steps: The steps of this ImageInfo.
        :type steps: int
        """

        self._steps = steps

    @property
    def height(self) -> str:
        """Gets the height of this ImageInfo.


        :return: The height of this ImageInfo.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height: str):
        """Sets the height of this ImageInfo.


        :param height: The height of this ImageInfo.
        :type height: str
        """

        self._height = height

    @property
    def width(self) -> str:
        """Gets the width of this ImageInfo.


        :return: The width of this ImageInfo.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width: str):
        """Sets the width of this ImageInfo.


        :param width: The width of this ImageInfo.
        :type width: str
        """

        self._width = width

    @property
    def fix_faces(self) -> bool:
        """Gets the fix_faces of this ImageInfo.


        :return: The fix_faces of this ImageInfo.
        :rtype: bool
        """
        return self._fix_faces

    @fix_faces.setter
    def fix_faces(self, fix_faces: bool):
        """Sets the fix_faces of this ImageInfo.


        :param fix_faces: The fix_faces of this ImageInfo.
        :type fix_faces: bool
        """

        self._fix_faces = fix_faces

    @property
    def fix_faces_fidelity(self) -> str:
        """Gets the fix_faces_fidelity of this ImageInfo.


        :return: The fix_faces_fidelity of this ImageInfo.
        :rtype: str
        """
        return self._fix_faces_fidelity

    @fix_faces_fidelity.setter
    def fix_faces_fidelity(self, fix_faces_fidelity: str):
        """Sets the fix_faces_fidelity of this ImageInfo.


        :param fix_faces_fidelity: The fix_faces_fidelity of this ImageInfo.
        :type fix_faces_fidelity: str
        """

        self._fix_faces_fidelity = fix_faces_fidelity

    @property
    def sampler_type(self) -> str:
        """Gets the sampler_type of this ImageInfo.


        :return: The sampler_type of this ImageInfo.
        :rtype: str
        """
        return self._sampler_type

    @sampler_type.setter
    def sampler_type(self, sampler_type: str):
        """Sets the sampler_type of this ImageInfo.


        :param sampler_type: The sampler_type of this ImageInfo.
        :type sampler_type: str
        """

        self._sampler_type = sampler_type

    @property
    def conditioning(self) -> str:
        """Gets the conditioning of this ImageInfo.


        :return: The conditioning of this ImageInfo.
        :rtype: str
        """
        return self._conditioning

    @conditioning.setter
    def conditioning(self, conditioning: str):
        """Sets the conditioning of this ImageInfo.


        :param conditioning: The conditioning of this ImageInfo.
        :type conditioning: str
        """

        self._conditioning = conditioning

    @property
    def model(self) -> str:
        """Gets the model of this ImageInfo.


        :return: The model of this ImageInfo.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this ImageInfo.


        :param model: The model of this ImageInfo.
        :type model: str
        """

        self._model = model

    @property
    def seed(self) -> int:
        """Gets the seed of this ImageInfo.


        :return: The seed of this ImageInfo.
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed: int):
        """Sets the seed of this ImageInfo.


        :param seed: The seed of this ImageInfo.
        :type seed: int
        """

        self._seed = seed

    @property
    def upscale(self) -> bool:
        """Gets the upscale of this ImageInfo.


        :return: The upscale of this ImageInfo.
        :rtype: bool
        """
        return self._upscale

    @upscale.setter
    def upscale(self, upscale: bool):
        """Sets the upscale of this ImageInfo.


        :param upscale: The upscale of this ImageInfo.
        :type upscale: bool
        """

        self._upscale = upscale

    @property
    def tile_mode(self) -> bool:
        """Gets the tile_mode of this ImageInfo.


        :return: The tile_mode of this ImageInfo.
        :rtype: bool
        """
        return self._tile_mode

    @tile_mode.setter
    def tile_mode(self, tile_mode: bool):
        """Sets the tile_mode of this ImageInfo.


        :param tile_mode: The tile_mode of this ImageInfo.
        :type tile_mode: bool
        """

        self._tile_mode = tile_mode

    @property
    def weighted_prompt(self) -> List[WeightedPrompt]:
        """Gets the weighted_prompt of this ImageInfo.


        :return: The weighted_prompt of this ImageInfo.
        :rtype: List[WeightedPrompt]
        """
        return self._weighted_prompt

    @weighted_prompt.setter
    def weighted_prompt(self, weighted_prompt: List[WeightedPrompt]):
        """Sets the weighted_prompt of this ImageInfo.


        :param weighted_prompt: The weighted_prompt of this ImageInfo.
        :type weighted_prompt: List[WeightedPrompt]
        """

        self._weighted_prompt = weighted_prompt
