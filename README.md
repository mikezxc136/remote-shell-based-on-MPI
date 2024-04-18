# Remote Shell Based on MPI

## Introduction
This project is a simple remote shell system based on MPI (Message Passing Interface), allowing users to control and execute commands on different processing nodes in a parallel computing system.

## What is mpi4py?

MPI for Python provides MPI bindings for the Python language, allowing programmers to exploit multiple processor computing systems. mpi4py is constructed on top of the MPI-1/2 specifications and provides an object oriented interface which closely follows MPI-2 C++ bindings.

## Usage
### Requirements
- Install [MPI](https://www.microsoft.com/en-us/download/details.aspx?id=57467) on your computer.
- Install the `mpi4py` library for Python. You can install it using the following command:

```bash
pip install mpi4py
```
### Running the Program
- Run the python script on MPI:

```bash
mpiexec -np N python pythonscript.py
```

where N is the number of worker nodes you want to run. 
`pythonscipt.py` is a file that you want to run

### Master node and Worker node
- Run the master node:

```bash
mpiexec -np 1 python master_node.py
```

- Run the worker nodes:

```bash
mpiexec -np N python worker_node.py
```
where N is the number of worker nodes you want to run.

After running, you can input commands from the master node, and they will be sent to the worker nodes for execution.
### Communicators and Ranks
This example demonstrates basic MPI usage in Python using mpi4py. It prints out the rank of each process within the MPI communicator.

Run the script using mpiexec with the desired number of processes. For example, to run with 4 processes:

```bash
mpiexec -n 4 python comm.py
```

### Point-to-Point Communication
This code snippet showcases how to use MPI (Message Passing Interface) for inter-process communication in Python using mpi4py. It involves two processes exchanging data: process 0 sending data to process 1.
#### Explanation:
- The code begins by importing MPI and NumPy libraries.
- It initializes MPI communication by creating a communicator (`comm`) representing all processes.
- Each process retrieves its rank within the communicator using `comm.Get_rank()`.
- Process 0 generates data and sends it to process 1 using `comm.send()` and `comm.Send()`.
- Process 1 receives the data from process 0 using `comm.recv()` and `comm.Recv()`.

Run the script using `mpiexec` with exactly 2 processes:
```bash
mpiexec -n 2 python point-to-point.py
```

### Collective Communication
MPI supports collective communication operations that involve multiple processes within a communicator. These operations enable efficient data exchange and computation across the processes.

Broadcasting: Broadcasting sends an exact copy of a variable to all processes in a communicator.
Scattering: Scattering distributes contiguous sections of an array across the ranks of a communicator.
Gathering: Gathering collects subsets of an array distributed across the ranks and gathers them back into the full array.
Reduction: Reduction aggregates values from all processes in an array and reduces them to a single result on the root process.

These collective communication operations facilitate efficient parallel computing by enabling processes to exchange data and synchronize their computations.

Run the script using `mpiexec` with exactly 4 processes:
```bash
mpiexec -n 4 python collective_xxxx.py
```

## Note
- Ensure that you have correctly installed MPI and mpi4py before running the program.
- This program is just a simple example and does not have high security. In a real-world environment, you need to consider issues such as authentication and access control.

## Directory Structure
- `comm.py`: Source code for communicators and ranks.
- `point-to-point.py`: Source code for point-to-point communication.
- `collective_xxxx.py`: Source code for collective communication.
- `master_node.py`: Source code for the master node.
- `worker_node.py`: Source code for the worker nodes.
- `README.md`: This file.

## Extensions
You can extend this project by adding features such as user authentication, access control, or improving the user interface to make the remote shell system more flexible and useful.

## Documentation for mpi4py

The documentation for mpi4py can be found [here](https://mpi4py.scipy.org/).

However, it is still a work in progress and much of it assumes you are already familiar with the MPI standard. Therefore, you will probably also need to consult the [MPI standard documentation](http://mpi-forum.org/docs/).

The MPI docs only cover the C and Fortran implementations, but the extension to Python syntax is straightforward and in most cases much simpler than the equivalent C or Fortran statements.

Another useful place to look for help is the API reference for mpi4py:

[API Reference for mpi4py](https://mpi4py.scipy.org/docs/apiref/mpi4py.MPI-module.html)

In particular, the section for Class Comm lists all the methods you can use with a communicator object:

[Class Comm API Reference](https://mpi4py.scipy.org/docs/apiref/mpi4py.MPI.Comm-class.html)

## Author
This project is developed by Tuan.

