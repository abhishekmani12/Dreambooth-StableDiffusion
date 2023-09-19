#!pip install -U autotrain-advanced
#!autotrain setup

def train(PROMPT, PATH, BATCH_SIZE, STEP_NUMBER):

  os.environ["prompt"] = PROMPT
  os.environ["batch_size"] = str(BATCH_SIZE)
  os.environ["step_number"] = str(STEP_NUMBER)
  os.environ["path"] = str(PATH)

  !autotrain dreambooth \
  --model stabilityai/stable-diffusion-xl-base-1.0 \
  --project-name Train-Dreambooth \
  --image-path ${PATH} \
  --prompt "${prompt}" \
  --resolution 512 \
  --batch-size ${batch_size} \
  --num-steps ${step_number} \
  --fp16 \
  --xformers \
  --train-text-encoder \
  --gradient-accumulation 4\
  --lr 1e-4 \
  --use-8bit-adam
