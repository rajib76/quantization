import torch

value = 1/3
result = format(value, '.60f')
print(result)

tensor_fp64 = torch.tensor(value,dtype=torch.float64)
print(f"fp64 tensor: {format(tensor_fp64.item(), '.60f')}")

tensor_fp32 = torch.tensor(value,dtype=torch.float32)
print(f"fp32 tensor: {format(tensor_fp32.item(), '.60f')}")

tensor_fp16 = torch.tensor(value,dtype=torch.float16)
print(f"fp16 tensor: {format(tensor_fp16.item(), '.60f')}")

tensor_fp32 = torch.rand(1000, dtype = torch.float32)
# first 5 elements of the random tensor
result = tensor_fp32[:5]

print(result)

tensor_fp32_to_bf16 = tensor_fp32.to(dtype = torch.bfloat16)
# first 5 elements of the random tensor
result = tensor_fp32_to_bf16[:5]

print(result)
