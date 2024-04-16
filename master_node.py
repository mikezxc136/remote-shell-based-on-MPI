from mpi4py import MPI
from mpi4py.futures import MPICommExecutor


def execute_command(command):
    # Thực hiện logic thực thi lệnh ở đây
    # Trong ví dụ này, tôi chỉ trả về kết quả là phản hồi giả
    return f"Worker {rank} received command: {command}"

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:  # Master node
    with MPICommExecutor(MPI.COMM_WORLD) as executor:
        while True:
            command = input("Enter command: ")
            if command.lower() == "exit":
                break
            else:
                # Gửi lệnh đến các worker nodes và nhận kết quả
                futures = [executor.submit(execute_command, command) for _ in range(comm.Get_size() - 1)]
                for future in futures:
                    print(future.result())
else:
    while True:
        # Worker nodes chỉ chờ nhận lệnh từ master node và thực thi
        command = comm.recv(source=0, tag=1)
        if command.lower() == "exit":
            break
        else:
            # Thực thi lệnh và gửi kết quả về cho master node
            result = execute_command(command)
            comm.send(result, dest=0, tag=2)


