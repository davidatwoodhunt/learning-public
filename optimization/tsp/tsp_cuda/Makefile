# Define the CUDA compiler
NVCC = nvcc

# Compiler flags for optimization and C++ standard
CXXFLAGS = -O3 -std=c++11

# The source file (adjust if there are more files)
SRC = tsp_cuda.cu

# Output binary
OUT = tsp_cuda

# CUDA architecture (adjust for your GPU)
ARCH = -gencode arch=compute_86,code=sm_86

# Default build rule
all: $(OUT)

# How to compile the .cu file into the binary
$(OUT): $(SRC)
	$(NVCC) $(CXXFLAGS) $(ARCH) -o $(OUT) $(SRC) -lm

# Clean rule to remove the binary
clean:
	rm -f $(OUT)
