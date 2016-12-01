from pysphere import VIServer
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
server = VIServer()
server.connect("192.168.15.245", "root", "1111111")
vm = server.get_vm_by_path("[datastore1] Coordinator-1-16/Coordinator-1-16.vmx")
vm.login_in_guest("root", "aaaaaa")
vm.send_file("E:\\server_1_16\\server_1_16\\abn_05fa.dst", r"/mnt/abn_05fa.dst")
print vm.get_status()