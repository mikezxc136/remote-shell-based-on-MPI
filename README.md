# Remote Shell Based on MPI

## Introduction
This project is a simple remote shell system based on MPI (Message Passing Interface), allowing users to control and execute commands on different processing nodes in a parallel computing system.

## Usage
### Requirements
- Install MPI on your computer.
- Install the `mpi4py` library for Python. You can install it using the following command:

```bash
pip install mpi4py
```

### What is mpi4py?

MPI for Python provides MPI bindings for the Python language, allowing programmers to exploit multiple processor computing systems. mpi4py is constructed on top of the MPI-1/2 specifications and provides an object oriented interface which closely follows MPI-2 C++ bindings.

### Documentation for mpi4py

The documentation for mpi4py can be found [here](https://mpi4py.scipy.org/).

However, it is still a work in progress and much of it assumes you are already familiar with the MPI standard. Therefore, you will probably also need to consult the [MPI standard documentation](http://mpi-forum.org/docs/).

The MPI docs only cover the C and Fortran implementations, but the extension to Python syntax is straightforward and in most cases much simpler than the equivalent C or Fortran statements.

Another useful place to look for help is the API reference for mpi4py:

[API Reference for mpi4py](https://mpi4py.scipy.org/docs/apiref/mpi4py.MPI-module.html)

In particular, the section for Class Comm lists all the methods you can use with a communicator object:

[Class Comm API Reference](https://mpi4py.scipy.org/docs/apiref/mpi4py.MPI.Comm-class.html)

### Running the Program
- Run the python script on MPI:

```bash
mpirun -np N python pythonscript.py
```

where N is the number of worker nodes you want to run. pythonscipt is a file that you want to run

### Communicators and Ranks
This example demonstrates basic MPI usage in Python using mpi4py. It prints out the rank of each process within the MPI communicator.

## Note
- Ensure that you have correctly installed MPI and mpi4py before running the program.
- This program is just a simple example and does not have high security. In a real-world environment, you need to consider issues such as authentication and access control.

## Directory Structure
- `master_node.py`: Source code for the master node.
- `worker_node.py`: Source code for the worker nodes.
- `README.md`: This file.

## Extensions
You can extend this project by adding features such as user authentication, access control, or improving the user interface to make the remote shell system more flexible and useful.

## Author
This project is developed by Tuan.

