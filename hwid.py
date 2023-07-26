import platform
import hashlib
import pyperclip


def get_device_id():
    # 获取计算机的硬件设备号（UUID）
    device_uuid = platform.node()

    # 获取操作系统相关信息
    os_info = platform.system() + platform.release()

    # 组合设备标识信息
    combined_info = device_uuid + os_info

    # 使用MD5哈希算法生成设备识别码
    device_id = hashlib.md5(combined_info.encode()).hexdigest()

    return device_id


# 获取设备识别码
device_idx = get_device_id()
print("设备识别码:", device_idx, ' --已经粘贴到剪贴板')
pyperclip.copy(device_idx)
