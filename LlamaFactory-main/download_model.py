from modelscope import snapshot_download

# 下载 Qwen2-1.5B-Instruct 模型
# cache_dir 是你存放模型的路径，你可以改，但我建议就用这个
model_dir = snapshot_download('qwen/Qwen2-1.5B-Instruct', cache_dir='D:/python/RAG-project/models')

print(f"\n>>> 模型已下载完成！路径是: {model_dir}")