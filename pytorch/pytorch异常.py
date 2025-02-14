
# 问题：模型蒸馏时，出现错误：
element 0 of tensors does not require grad and does not have a grad_fn
问题原因及解决方法：
出现这种问题是因为我们需要对变量求梯度，但是系统默认的是False, 也就是不对这个变量求梯度。
loss.backward()之前添加：
loss = Variable(loss, requires_grad = True)

# torch.load(model_path)出错：
保存模型：torch.save(model, 'model.pkl')
但是加载模型：
model = torch.load('model.pkl')
报错：
ModuleNotFoundError: No module named '***'
解决方案，修改保存模型的方法：
在保存模型同样的环境下加载。

# 错误：
AttributeError: 'Tensor' object has no attribute 'numpy'
原因可能有两个
第一个是TensorFlow的版本问题，要TensorFlow1.14以上版本才有，所以就解决方案就是升级TensorFlow到1.14以上版本
具体语句为pip install tensorflow==版本号
或者改写代码：
y = result.numpy()
改为：
with tf.Session() as sess:
    y = sess.run(result)

第二个原因，如果你升级了以后还是报错那么就添加以下语句tf.enable_eager_execution()
切换到eager模式即可解决。

解决方式：（版本1.14后才有的特性）
import tensorflow as tf
tf.enable_eager_execution() # 关键
 
m = tf.keras.metrics.Accuracy()
m.update_state([1, 2, 3, 4], [1, 2, 3, 4])
print('Final result: ', m.result().numpy())

# 错误：
RuntimeError: tf.placeholder() is not compatible with eager execution.
解决方法：
在代码中添加这样一句：
tf.compat.v1.disable_eager_execution()
如：
import tensorflow as tf
import numpy as np
tf.compat.v1.disable_eager_execution()

# 模型在预测时，开始时候正常，预测到后面报错，如预测到10%出现错误：
RuntimeError: CUDA out of memory. Tried to allocate 12.00MiB (GPU 0; 15.75 GiB total capacity; 14.25 GiB already allocated; 1.62 MiB free; 368.20 MiB cached)
问题原因及解决方法：
主要是在预测时候没有禁止求梯度，改为下面这样就可以了：
with torch.no_grad():
    logits = model(input_ids, input_mask, None)

# Pytorch: list, numpy. Tensor 格式转化 （附 only one element tensors can be converted to Python scalars 解决）
# list -> torch.Tensor 转 numpy
a = torch.tensor([1,2,3])
a
Out[9]: tensor([1, 2, 3])
a.numpy()
Out[10]: array([1, 2, 3], dtype=int64)

# numpy 转 torch.Tensor
torch.from_numpy(np.array([1,2,3]))
Out[11]: tensor([1, 2, 3], dtype=torch.int32)

# list 转 torch.Tensor
torch.tensor([1,2,3])
Out[12]: tensor([1, 2, 3])

注意：有时，上面操作会出现报错：ValueError:only one element tensors can be converted to Python scalars
原因是：要转换的list里面的元素包含多维的tensor。
在 gpu 上的解决方法是：
val= torch.tensor([item.cpu().detach().numpy() for item in val]).cuda() 
这是因为 gpu上的 tensor 不能直接转为 numpy； 需要先在 cpu 上完成操作，再回到 gpu 上
如果是在 cpu 上，上面的 .cpu() 和 .cuda() 可以省略

# torch.Tensor 转 list
list = tensor.numpy().tolist()   # 先转 numpy，后转 list
ts = torch.tensor([1,2,3])
ts
Out[17]: tensor([1, 2, 3])
ts.numpy().tolist()
Out[18]: [1, 2, 3]

# list 转 numpy
ndarray = np.array(list)

# numpy 转 list
list = ndarray.tolist()

# import torch 导入报错：
OSError: [WinError 126] 找不到指定的模块。 Error loading "D:\Users\Users1\AppData\Roaming\Python\Python36\site-packages\torch\lib\asmjit.dll" or one of its dependencies.
可能是因为安装的torch版本不对，重新安装对应的torch版本：
可在下面的页面查找到对应的torch版本：
https://download.pytorch.org/whl/torch_stable.html
根据前面的对应关系，下载好适合你的版本的 torch 、torchvision。
cu102 # 表示CUDA=10.2
cp37 # 表示python=3.7
linux or win # 表示对应的宿主机操作系统环境
下载好后，用pip安装，先cd 到下载的文件夹
pip install torch-1.7.0+cu101-cp36-cp36m-win_amd64.whl
pip install torchvision-0.8.0-cp36-cp36m-win_amd64.whl
测试GPU版本的torch是否安装成功
(torch) D:\MyData\xiaCN\Desktop\Work\unbiased> python
Python 3.6.13 (default, Feb 19 2021, 05:17:09) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True

# 但有时候版本对应好了，但是import troch还是报错：
>>> import torch
Microsoft Visual C++ Redistributable is not installed, this may lead to the DLL load failure.
                 It can be downloaded at https://aka.ms/vs/16/release/vc_redist.x64.exe
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Users\user3\AppData\Roaming\Python\Python36\site-packages\torch\__init__.py", line 135, in <modu
le>
    raise err
OSError: [WinError 126] 找不到指定的模块。 Error loading "D:\Users\user3\AppData\Roaming\Python\Python36\si
te-packages\torch\lib\asmjit.dll" or one of its dependencies.
# 实际上错误原因是说了，是因为 没有安装 Microsoft Visual C++ Redistributable, 在 https://aka.ms/vs/16/release/vc_redist.x64.exe 下载安装即可。
# 但本人发现自己电脑安装的Microsoft Visual C++ Redistributable，却为何还报这个错误呢，猜测可能是因为Microsoft Visual C++ Redistributable版本不对。
于是卸载本机已经安装的 Microsoft Visual C++ 2010 Redistributable
重新安装 Microsoft Visual C++ 2015-2019 Redistributable，安装完成后，重启电脑，结果就正常了：
~$ python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.__version__
'1.9.0+cpu'
>>> torch.cuda.is_available()
False

