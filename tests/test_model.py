from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "HuggingFaceH4/zephyr-7b-alpha"

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Model failed to load:")
    print(e)