from setuptools import setup, find_packages

setup(name="AICity_Action_Recognition", version="1.0", author="TRAN DAI CHI", author_email="ctran743@gmail.com", description="README.md", url="",
      py_modules=["FastFlowNet", "JUN_boat_2023", "Track_3_2024", "VTCC_UTVM_2022", "aicity24-eval-script-track3", "cut_inference_A2"],
      license="LICENSE", python_requires=">=3.8", include_package_data=True, install_requires="requirements.txt")