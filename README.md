# Remote Shell Based on MPI

## Introduction
This project is a simple remote shell system based on MPI (Message Passing Interface), allowing users to control and execute commands on different processing nodes in a parallel computing system.

## Usage
### Requirements
- Install MPI on your computer.
- Install the `mpi4py` library for Python. You can install it using the following command:
pip install mpi4py


### Running the Program
- Run the master node:

mpirun -np 1 python master_node.py

- Run the worker nodes:
mpirun -np N python worker_node.py

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

