from IPython.display import display
from PIL import Image
import ipywidgets as widgets
from diffusers import DiffusionPipeline, StableDiffusionXLImg2ImgPipeline
import torch
model_path = "/content/Train-Dreambooth"
model = "stabilityai/stable-diffusion-xl-base-1.0"

pipe = DiffusionPipeline.from_pretrained(model, torch_dtype=torch.float16)
pipe.to("cuda")
pipe.load_lora_weights(model_path, weight_name="pytorch_lora_weights.safetensors")

'''
refiner = StableDiffusionXLImg2ImgPipeline.from_pretrained(

     "stabilityai/stable-diffusion-xl-refiner-1.0",
     torch_dtype=torch.float16,
)

refiner.to("cuda")
'''
heading = widgets.HTML("<h2>Inferencing</h2>")
PROMPT_I = widgets.Text(description='Prompt:')
NUM = widgets.BoundedIntText(value=3, min=0, max=20, description="Image Num:")
submit = widgets.Button(description='Generate')

def generate(prompt, num):

  for seed in range(num):
    generator = torch.Generator("cuda").manual_seed(seed)
    image = pipe(prompt=prompt, generator=generator, num_inference_steps=25).images[0]
    #image = refiner(prompt=prompt, generator=generator, image=image).images[0]
    image.show()
    image.save(f"Generated-Image-{seed}.png")

def submit_clicked(b):

  generate(PROMPT_I.value, NUM.value)

submit.on_click(submit_clicked)

display(heading, PROMPT_I, NUM, submit)

