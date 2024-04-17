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

## What is mpi4py?

MPI for Python provides MPI bindings for the Python language, allowing programmers to exploit multiple processor computing systems. mpi4py is constructed on top of the MPI-1/2 specifications and provides an object oriented interface which closely follows MPI-2 C++ bindings.

## Documentation for mpi4py

The documentation for mpi4py can be found [here](https://mpi4py.scipy.org/).

However, it is still a work in progress and much of it assumes you are already familiar with the MPI standard. Therefore, you will probably also need to consult the [MPI standard documentation](http://mpi-forum.org/docs/).

The MPI docs only cover the C and Fortran implementations, but the extension to Python syntax is straightforward and in most cases much simpler than the equivalent C or Fortran statements.

Another useful place to look for help is the API reference for mpi4py:

[API Reference for mpi4py](https://mpi4py.scipy.org/docs/apiref/mpi4py.MPI-module.html)

In particular, the section for Class Comm lists all the methods you can use with a communicator object:

[Class Comm API Reference](https://mpi4py.scipy.org/docs/apiref/mpi4py.MPI.Comm-class.html)

## Running Python Scripts with MPI

Python programs that use MPI commands must be run using an MPI interpreter, which is provided with the command `mpirun`. On some systems this command is instead called `mpiexec` and mpi4py seems to include both.

Make sure your environment is correct by checking that `mpirun` is in your anaconda directory for `geo_scipy` by using the `which` Unix command:


### Running the Program
- Run the master node:

```bash
mpirun -np 1 python master_node.py
```

- Run the worker nodes:
```bash
mpirun -np N python worker_node.py
```

where N is the number of worker nodes you want to run.

After running, you can input commands from the master node, and they will be sent to the worker nodes for execution.

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

