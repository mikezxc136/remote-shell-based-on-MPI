from mpi4py import MPI

# Khởi tạo MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:  # Nút chính (master)
    while True:
        command = input("Enter command: ")
        for worker_rank in range(1, size):
            comm.send(command, dest=worker_rank, tag=1)
        if command.lower() == "exit":
            break
else:
    while True:
        command = comm.recv(source=0, tag=1)
        if command.lower() == "exit":
            break
        else:
            # Thực thi lệnh và gửi kết quả về cho master
            result = "Worker {} received command: {}".format(rank, command)
            comm.send(result, dest=0, tag=2)
