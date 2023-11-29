from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call, call
import os 
import requests
# add follwing lines to setup.py 
# %cd /content/pifuhd/
# !sh ./scripts/download_trained_model.sh


class CustomInstallCommand(install):
    def run(self):
        # Run the additional commands after the installation
        url = "https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth"
        try:
            if not os.path.exists("checkpoint_iter_370000.pth"):
                check_call(["wget", url])
            else:
                print("checkpoint_iter_370000.pth already exists")
        except Exception as e:
            print("Error: in dowlaoding ", e)
            print("Downloading using request library ...")
            response = requests.get(url)
            if response.status_code == 200:
                with open("checkpoint_iter_370000.pth", 'wb') as file:
                    file.write(response.content)
                    print("Download successful using requests library.")
            else:
                print(f"Error: Unable to download file. HTTP Status Code: {response.status_code}")


        # check_call(["sh", "pifuhd/scripts/download_trained_model.sh"])
        # check_call(["set", "-ex"])
        # check_call(["mkdir", "-p", "pifuhd/checkpoints"])
        # check_call(["cd", "pifuhd/checkpoints"])
        url2 = "https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt"
        try:
            if not os.path.exists("pifuhd.pt"):
                check_call(["wget", "https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt", "-O", "pifuhd.pt"])
            else:
                print("pifuhd.pt already exists")
        except Exception as e:
            print("Error: in dowlaoding ", e)
            print("Downloading using request library ...")
            response = requests.get(url2)
            if response.status_code == 200:
                with open("pifuhd.pt", 'wb') as file:
                    file.write(response.content)
                    print("Download successful using requests library.")
            else:
                print(f"Error: Unable to download file. HTTP Status Code: {response.status_code}")
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
