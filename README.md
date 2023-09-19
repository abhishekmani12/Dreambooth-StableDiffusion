# Dreambooth-StableDiffusion
A fun experiment on finetuning Stable Diffusion models for text2img generation

- Intended for users to finetune and train the model with their own images for custom text2img generation.
- Training dataset can be as small as 5 images
- Currently hosted on Colab with ipywidgets to simplify interfacing with it.
- Refiner model was not used due to the memory constraints of Colab (Free Version)
- Each training step takes 8 minutes on average

## Usage:
- Follow the steps specified in [run.ipynb](https://github.com/abhishekmani12/Dreambooth-StableDiffusion/blob/main/run.ipynb)
- Run it on Colab if you don't have CUDA enabled GPU with atleast 15GB of memory

### My run:
- Used 7 images of Lewis Hamilton as the training set for `100 steps` at `512 resolution` with `batch size 1`
- Prompt: `"Photo of Lewis Hamilton singing at the opera"`

### Generated Image:
![Generated-Image-1](https://github.com/abhishekmani12/Dreambooth-StableDiffusion/assets/76105443/fe043345-2486-4d54-932d-22d66fef2fc9)

- Since the resolution was set to 512, the image is pixelated. Increasing the prameter values will result in better quality images but will overshoot the memory cap imposed on the free version of Colab.
- You can even try using your own faces to generate new backgrounds or actions.


