# unsigned integer
#torch.uint8 - 8 bit unsigned
import torch

result = torch.iinfo(torch.uint8)
print(result)

result = torch.iinfo(torch.int8)
print(result)

result = torch.iinfo(torch.int64)
print(result)

result = torch.finfo(torch.bfloat16)
print(result)



