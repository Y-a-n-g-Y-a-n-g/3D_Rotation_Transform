import numpy as np
#将旋转矩阵转换为四元数矩阵
def rotation_matrix_to_quaternion(R):

    #print(R)
    qw = np.sqrt(1 + R[0] + R[4] + R[8]) / 2
    qx = (R[7] - R[5]) / (4 * qw)
    qy = (R[2] - R[6]) / (4 * qw)
    qz = (R[3] - R[1]) / (4 * qw)

    return [qw, qx, qy, qz]
#将四元数矩阵转换为旋转矩阵
def quaternion_to_rotation_matrix(quaternion):
    # 标准化四元数
    quaternion = np.array(quaternion) / np.linalg.norm(quaternion)
    # 提取四元数的元素
    w, x, y, z = quaternion
    # 计算旋转矩阵的元素
    m00 = 1 - 2*y*y - 2*z*z
    m01 = 2*x*y - 2*z*w
    m02 = 2*x*z + 2*y*w
    m10 = 2*x*y + 2*z*w
    m11 = 1 - 2*x*x - 2*z*z
    m12 = 2*y*z - 2*x*w
    m20 = 2*x*z - 2*y*w
    m21 = 2*y*z + 2*x*w
    m22 = 1 - 2*x*x - 2*y*y
    # 构建旋转矩阵
    rotation_matrix = np.array([[m00, m01, m02],
                                [m10, m11, m12],
                                [m20, m21, m22]])
    return rotation_matrix