from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call, call
import os 

# add follwing lines to setup.py 
# %cd /content/pifuhd/
# !sh ./scripts/download_trained_model.sh


class CustomInstallCommand(install):
    def run(self):
        # Run the additional commands after the installation
        if not os.path.exists("checkpoint_iter_370000.pth"):
            check_call(["wget", "https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth"])
        else:
            print("checkpoint_iter_370000.pth already exists")
        # check_call(["sh", "pifuhd/scripts/download_trained_model.sh"])
        # check_call(["set", "-ex"])
        # check_call(["mkdir", "-p", "pifuhd/checkpoints"])
        # check_call(["cd", "pifuhd/checkpoints"])
        if not os.path.exists("pifuhd.pt"):
            check_call(["wget", "https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt", "-O", "pifuhd.pt"])
        else:
            print("pifuhd.pt already exists")
        # check_call(["cd", ".."])
        # mkdir -p checkpoints
        # cd checkpoints
        # wget "https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt" pifuhd.pt
        # cd ..
        call(["pip", "install", "-r", "requirements.txt"])
        install.run(self)

setup(
    name='var2obj',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # 'torch==<version>',
        # 'torchvision==<version>',
        # 'git+https://github.com/facebookresearch/pytorch3d.git',
        # 'rembg==<version>',
        'torch',
        'torchvision',
        'rembg',
        'transformers',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)