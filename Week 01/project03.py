from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 텍스트 파일 경로
dataset_path = "path/to/training_data.txt"

# GPT 모델과 토크나이저 로드
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 데이터셋 로드
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path=dataset_path,
    block_size=128
)

# 데이터 콜레이터 설정
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# 트레이닝 아큐먼트 설정
training_args = TrainingArguments(
    output_dir="./gpt_finetuned",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

# 트레이너 설정
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

# 훈련 시작
trainer.train()

# 훈련된 모델 저장
model.save_pretrained("./gpt_finetuned")
tokenizer.save_pretrained("./gpt_finetuned")
