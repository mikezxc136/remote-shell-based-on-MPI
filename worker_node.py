from mpi4py import MPI

# Khởi tạo MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank != 0:  # Các nút worker
    while True:
        command = comm.recv(source=0, tag=1)
        if command.lower() == "exit":
            break
        else:
            # Thực thi lệnh và gửi kết quả về cho master
            result = "Worker {} received command: {}".format(rank, command)
            comm.send(result, dest=0, tag=2)
