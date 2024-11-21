{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation {
  pname = "tsp_cuda";
  version = "1.0";

  # Define the directory where the source files are
  srcs = [ ./tsp_cuda.cu ./Makefile ];

  # Add the CUDA toolkit and make to the build environment
  buildInputs = [ pkgs.cudatoolkit pkgs.gnumake ];

  # Skip the unpack phase since we're dealing with a directory, not an archive
  dontUnpack = true;

  # Set the source root directory
  sourceRoot = ".";

  # Build the project using Makefile
  buildPhase = ''
    echo "Building with Makefile..."
    ls -l
    make
  '';

  # Install the binary to the output directory
  installPhase = ''
    mkdir -p $out/bin
    cp tsp_cuda $out/bin/
  '';

  # Meta information
  meta = with pkgs.lib; {
    description = "CUDA-based Traveling Salesman Problem solution";
    license = licenses.gpl3;
    platforms = platforms.linux;
  };
}
