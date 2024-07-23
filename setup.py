from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='rle',
    description="a package used for compress sparse tensor",
    packages=find_packages('rle'),
    ext_modules=[
        CUDAExtension('rle_cuda', [
            'rle_cuda.cpp',
            'rle_cuda_kernel.cu',
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
