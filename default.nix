with import <nixpkgs> { };

let
  pythonPackages = python310Packages; # Python 3.10
in pkgs.mkShell rec {
  name = "impurePythonEnv";
  venvDir = "./.venv";
  buildInputs = [
    pkgs.stdenv.cc.cc.lib
    pkgs.libstdcxx5              # Add libstdc++ to resolve missing library issue
    pkgs.gcc
    git-crypt
    pythonPackages.ipykernel
    pythonPackages.scipy
    pythonPackages.scikit-learn
    pythonPackages.jupyterlab
    pythonPackages.notebook
    pythonPackages.pyzmq
    pythonPackages.venvShellHook
    pythonPackages.matplotlib
    pythonPackages.pip
    pythonPackages.numpy
    pythonPackages.pandas
    pythonPackages.requests
    pythonPackages.tensorflow # Use TensorFlow with CUDA
    pythonPackages.pytorch-bin
    pythonPackages.seaborn
    pythonPackages.python-dotenv 
    pythonPackages.tabulate
    taglib
    openssl
    git
    libxml2
    libxslt
    libzip
    zlib                   
  ];
  # Run this command, only after creating the virtual environment
  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
    python -m ipykernel install --user --name=myenv4 --display-name="myenv4"
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip3 install -r requirements.txt

  '';

  # Optional commands within the virtual environment
  postShellHook = ''
    unset SOURCE_DATE_EPOCH
    LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib/"; # fix the problem of dynamic link in python package
    # Add LD_LIBRARY_PATH to the activate script
    echo 'export LD_LIBRARY_PATH="/nix/store/p3ffjixpnfgkqh20nsrc13vrj3yfi0nj-gcc-13.2.0-lib/lib:$LD_LIBRARY_PATH"' >> .venv/bin/activate
    jupyter notebook --no-browser
  '';
}
