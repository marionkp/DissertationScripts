import csv
import os

# patients=[002_S_0413, 006_S_4485, 011_S_6618, 020_S_6449, 027_S_5288, 033_S_4176, 037_S_6144, 070_S_5040, 100_S_6713, 123_S_6118, 129_S_6830, 135_S_6359, 153_S_6755, 301_S_6811, 002_S_1155, 006_S_4713, 011_S_6714, 020_S_6470, 027_S_6002, 033_S_4177, 037_S_6187, 070_S_6191, 109_S_4380, 123_S_6825, 129_S_6848, 135_S_6360, 168_S_6049, 305_S_6157, 002_S_1261, 006_S_4960, 012_S_4094, 020_S_6504, 027_S_6034, 033_S_4179, 037_S_6204, 070_S_6229, 109_S_6213, 126_S_0605, 129_S_6852, 135_S_6389, 168_S_6051, 305_S_6188, 002_S_1280, 006_S_6209, 012_S_4188, 020_S_6513, 027_S_6183, 033_S_5198, 037_S_6216, 070_S_6236, 109_S_6215, 126_S_0680, 129_S_6857, 135_S_6411, 168_S_6059, 305_S_6263, 002_S_4213, 006_S_6234, 012_S_4643, 020_S_6566, 027_S_6317, 033_S_5259, 037_S_6222, 070_S_6386, 109_S_6218, 126_S_4507, 130_S_0969, 135_S_6446, 168_S_6062, 305_S_6313, 002_S_4229, 006_S_6243, 012_S_5157, 022_S_2263, 027_S_6327, 033_S_6266, 037_S_6230, 070_S_6394, 109_S_6219, 126_S_4514, 130_S_2373, 135_S_6473, 168_S_6064, 305_S_6378, 002_S_4654, 006_S_6252, 012_S_5195, 022_S_2379, 027_S_6370, 033_S_6298, 037_S_6271, 070_S_6542, 109_S_6220, 126_S_4891, 130_S_2403, 135_S_6509, 168_S_6065, 305_S_6438, 002_S_4799, 006_S_6277, 012_S_6073, 022_S_5004, 027_S_6463, 033_S_6352, 037_S_6377, 070_S_6548, 109_S_6221, 126_S_4896, 130_S_4294, 135_S_6510, 168_S_6085, 305_S_6498, 002_S_5178, 006_S_6291, 013_S_2389, 022_S_6013, 027_S_6516, 033_S_6497, 037_S_6620, 082_S_2121, 109_S_6300, 126_S_5214, 130_S_4343, 135_S_6544, 168_S_6086, 305_S_6631, 002_S_5230, 006_S_6375, 013_S_4268, 022_S_6069, 027_S_6577, 033_S_6572, 037_S_6627, 082_S_4224, 109_S_6363, 126_S_5243, 130_S_4352, 135_S_6545, 168_S_6098, 305_S_6742, 002_S_6007, 006_S_6441, 013_S_4580, 022_S_6280, 027_S_6582, 033_S_6697, 051_S_5285, 082_S_4428, 109_S_6364, 126_S_6559, 130_S_4405, 135_S_6586, 168_S_6107, 305_S_6744, 002_S_6009, 006_S_6500, 013_S_6206, 022_S_6716, 027_S_6640, 033_S_6705, 051_S_6527, 082_S_5278, 109_S_6373, 126_S_6683, 130_S_4415, 135_S_6622, 168_S_6108, 305_S_6810, 002_S_6030, 006_S_6610, 013_S_6725, 022_S_6796, 027_S_6643, 033_S_6824, 051_S_6719, 082_S_5282, 109_S_6376, 126_S_6721, 130_S_4417, 135_S_6687, 168_S_6121, 305_S_6845, 002_S_6053, 006_S_6651, 013_S_6768, 022_S_6797, 027_S_6648, 035_S_0156, 051_S_6761, 082_S_6197, 109_S_6405, 126_S_6724, 130_S_4817, 135_S_6703, 168_S_6128, 305_S_6850, 002_S_6066, 006_S_6672, 013_S_6780, 022_S_6822, 027_S_6733, 035_S_0555, 052_S_1352, 082_S_6283, 109_S_6406, 127_S_1427, 130_S_5175, 135_S_6840, 168_S_6131, 341_S_6494, 002_S_6103, 006_S_6674, 014_S_2308, 022_S_6847, 027_S_6788, 035_S_4114, 052_S_4944, 082_S_6287, 114_S_0416, 127_S_2234, 130_S_5258, 136_S_0086, 168_S_6142, 341_S_6605, 002_S_6456, 006_S_6677, 014_S_4401, 023_S_0031, 027_S_6793, 035_S_4414, 052_S_6305, 082_S_6415, 114_S_2392, 127_S_4148, 130_S_6019, 136_S_0184, 168_S_6151, 341_S_6653, 002_S_6652, 006_S_6681, 014_S_4576, 023_S_1190, 027_S_6842, 035_S_4464, 052_S_6412, 082_S_6563, 114_S_4404, 127_S_4210, 130_S_6027, 136_S_0195, 168_S_6180, 341_S_6686, 002_S_6680, 006_S_6682, 014_S_6076, 023_S_2068, 027_S_6849, 035_S_4785, 052_S_6832, 082_S_6564, 114_S_5047, 127_S_4604, 130_S_6035, 136_S_0196, 168_S_6233, 341_S_6764, 002_S_6695, 006_S_6689, 014_S_6087, 023_S_4115, 029_S_2395, 035_S_6156, 052_S_6844, 082_S_6629, 114_S_5234, 127_S_5132, 130_S_6037, 136_S_0299, 168_S_6281, 341_S_6820, 002_S_6864, 006_S_6696, 014_S_6145, 023_S_4164, 029_S_4290, 035_S_6160, 053_S_2396, 082_S_6690, 114_S_6039, 127_S_5185, 130_S_6043, 136_S_0429, 168_S_6285, 941_S_1195, 003_S_0908, 006_S_6727, 014_S_6148, 023_S_4448, 029_S_4384, 035_S_6195, 053_S_4813, 094_S_6468, 114_S_6057, 127_S_5200, 130_S_6047, 136_S_0579, 168_S_6318, 941_S_4036, 003_S_1074, 006_S_6770, 014_S_6199, 023_S_6270, 029_S_4585, 035_S_6200, 053_S_5272, 094_S_6485, 114_S_6063, 127_S_5228, 130_S_6072, 137_S_4299, 168_S_6320, 941_S_4100, 003_S_1122, 007_S_1222, 014_S_6210, 023_S_6334, 029_S_5158, 035_S_6306, 053_S_5296, 098_S_0896, 114_S_6113, 127_S_5266, 130_S_6105, 137_S_4482, 168_S_6321, 941_S_4187, 003_S_2374, 007_S_2394, 014_S_6366, 023_S_6346, 029_S_5219, 035_S_6380, 053_S_6598, 098_S_4003, 114_S_6251, 127_S_6024, 130_S_6111, 137_S_4520, 168_S_6350, 941_S_4292, 003_S_4119, 007_S_4272, 014_S_6424, 023_S_6356, 029_S_6289, 035_S_6480, 053_S_6861, 098_S_4275, 114_S_6309, 127_S_6147, 130_S_6137, 137_S_4536, 168_S_6371, 941_S_4365, 003_S_4288, 007_S_4387, 014_S_6437, 023_S_6369, 029_S_6505, 035_S_6488, 057_S_0934, 098_S_4506, 114_S_6347, 127_S_6173, 130_S_6161, 137_S_4631, 168_S_6413, 941_S_4376, 003_S_4350, 007_S_4488, 014_S_6502, 023_S_6374, 029_S_6579, 035_S_6551, 057_S_5292, 098_S_6155, 114_S_6368, 127_S_6241, 130_S_6319, 137_S_4862, 168_S_6426, 941_S_5124, 003_S_4354, 007_S_4620, 014_S_6522, 023_S_6399, 029_S_6726, 035_S_6641, 057_S_6746, 098_S_6343, 114_S_6429, 127_S_6330, 130_S_6329, 137_S_6557, 168_S_6467, 941_S_5193, 003_S_4441, 007_S_4637, 014_S_6765, 023_S_6400, 029_S_6798, 035_S_6650, 067_S_0056, 098_S_6362, 114_S_6462, 127_S_6433, 130_S_6361, 137_S_6576, 168_S_6492, 941_S_6052, 003_S_4644, 007_S_5265, 014_S_6831, 023_S_6535, 031_S_0618, 035_S_6660, 067_S_0059, 098_S_6534, 114_S_6487, 127_S_6436, 130_S_6372, 137_S_6654, 168_S_6541, 941_S_6054, 003_S_4900, 007_S_6120, 018_S_2133, 023_S_6547, 031_S_2018, 035_S_6722, 067_S_2301, 098_S_6593, 114_S_6524, 127_S_6512, 130_S_6388, 137_S_6659, 168_S_6561, 941_S_6058, 003_S_5130, 007_S_6255, 018_S_2155, 023_S_6661, 031_S_2233, 035_S_6730, 067_S_2304, 098_S_6601, 114_S_6595, 127_S_6549, 130_S_6390, 137_S_6685, 168_S_6591, 941_S_6068, 003_S_5154, 007_S_6310, 018_S_2180, 023_S_6702, 031_S_4021, 035_S_6739, 067_S_4072, 098_S_6655, 114_S_6597, 128_S_0200, 130_S_6391, 137_S_6693, 168_S_6619, 941_S_6080, 003_S_6014, 007_S_6323, 018_S_4313, 023_S_6723, 031_S_4149, 035_S_6841, 067_S_4184, 098_S_6658, 114_S_6813, 128_S_0205, 130_S_6469, 137_S_6794, 168_S_6634, 941_S_6094, 003_S_6067, 007_S_6341, 018_S_4399, 023_S_6795, 031_S_4721, 036_S_2380, 067_S_4212, 098_S_6707, 116_S_0382, 128_S_0272, 130_S_6558, 137_S_6812, 168_S_6735, 941_S_6254, 003_S_6092, 007_S_6421, 018_S_4400, 024_S_2239, 031_S_6715, 036_S_4538, 067_S_4767, 098_S_6734, 116_S_4043, 128_S_2002, 130_S_6604, 137_S_6826, 168_S_6754, 941_S_6333, 003_S_6256, 007_S_6455, 018_S_4868, 024_S_4084, 032_S_0677, 036_S_6088, 067_S_4782, 098_S_6747, 116_S_4199, 128_S_2036, 130_S_6611, 141_S_0767, 168_S_6815, 941_S_6345, 003_S_6257, 007_S_6515, 018_S_6207, 024_S_4674, 032_S_1169, 036_S_6179, 067_S_6045, 099_S_4076, 116_S_4453, 128_S_2123, 130_S_6612, 141_S_1052, 168_S_6817, 941_S_6384, 003_S_6258, 007_S_6521, 018_S_6351, 024_S_5290, 032_S_2119, 036_S_6316, 067_S_6117, 099_S_4086, 116_S_4483, 128_S_2130, 130_S_6639, 141_S_1378, 168_S_6821, 941_S_6392, 003_S_6259, 009_S_0751, 018_S_6414, 024_S_6005, 032_S_4277, 037_S_0150, 067_S_6138, 099_S_6016, 116_S_4855, 128_S_2220, 130_S_6646, 141_S_2333, 168_S_6827, 941_S_6422, 003_S_6260, 009_S_4324, 019_S_4293, 024_S_6033, 032_S_4429, 037_S_0303, 067_S_6442, 099_S_6025, 116_S_6100, 128_S_4607, 130_S_6647, 141_S_4160, 168_S_6828, 941_S_6454, 003_S_6264, 009_S_4388, 019_S_4367, 024_S_6184, 032_S_5289, 037_S_0377, 067_S_6443, 099_S_6038, 116_S_6119, 128_S_4742, 130_S_6688, 141_S_6008, 168_S_6843, 941_S_6471, 003_S_6268, 009_S_4612, 019_S_4835, 024_S_6202, 032_S_6055, 037_S_0454, 067_S_6474, 099_S_6077, 116_S_6129, 128_S_4842, 130_S_6823, 141_S_6015, 168_S_6851, 941_S_6495, 003_S_6307, 009_S_5176, 019_S_6186, 024_S_6385, 032_S_6211, 037_S_4028, 067_S_6525, 099_S_6097, 116_S_6133, 129_S_2332, 131_S_0384, 141_S_6041, 168_S_6860, 941_S_6496, 003_S_6432, 009_S_6163, 019_S_6315, 024_S_6472, 032_S_6279, 037_S_4030, 067_S_6528, 099_S_6175, 116_S_6428, 129_S_4369, 131_S_6143, 141_S_6042, 177_S_6328, 941_S_6499, 003_S_6479, 009_S_6212, 019_S_6483, 024_S_6846, 032_S_6293, 037_S_4071, 067_S_6529, 099_S_6379, 116_S_6439, 129_S_4396, 131_S_6170, 141_S_6061, 177_S_6335, 941_S_6514, 003_S_6490, 009_S_6286, 019_S_6533, 027_S_0074, 032_S_6294, 037_S_4214, 068_S_0127, 099_S_6396, 116_S_6458, 129_S_4422, 131_S_6519, 141_S_6075, 177_S_6408, 941_S_6546, 003_S_6606, 009_S_6402, 019_S_6573, 027_S_0120, 032_S_6600, 037_S_4302, 068_S_0210, 099_S_6476, 116_S_6517, 129_S_6082, 131_S_6616, 141_S_6116, 177_S_6409, 941_S_6570, 003_S_6644, 010_S_6567, 019_S_6585, 027_S_2219, 032_S_6602, 037_S_4308, 068_S_0473, 099_S_6632, 116_S_6537, 129_S_6146, 131_S_6692, 141_S_6178, 177_S_6420, 941_S_6574, 003_S_6678, 010_S_6748, 019_S_6630, 027_S_2245, 032_S_6699, 037_S_4410, 068_S_0802, 100_S_0069, 116_S_6543, 129_S_6228, 131_S_6805, 141_S_6240, 177_S_6448, 941_S_6575, 003_S_6833, 011_S_0021, 019_S_6635, 027_S_4869, 032_S_6700, 037_S_4706, 068_S_2184, 100_S_1286, 116_S_6550, 129_S_6288, 135_S_4356, 141_S_6253, 301_S_6056, 941_S_6580, 005_S_0602, 011_S_4105, 019_S_6668, 027_S_4919, 032_S_6701, 037_S_5126, 068_S_2187, 100_S_4469, 116_S_6624, 129_S_6304, 135_S_4446, 141_S_6416, 301_S_6224, 941_S_6581, 005_S_0610, 011_S_4278, 019_S_6712, 027_S_5079, 032_S_6709, 037_S_5222, 068_S_2315, 100_S_4556, 116_S_6750, 129_S_6452, 135_S_4489, 141_S_6423, 301_S_6297, 941_S_6803, 005_S_4185, 011_S_4547, 019_S_6757, 027_S_5083, 032_S_6717, 037_S_6031, 068_S_4061, 100_S_5091, 116_S_6775, 129_S_6457, 135_S_4598, 141_S_6589, 301_S_6326, 005_S_6084, 011_S_4827, 020_S_5140, 027_S_5093, 032_S_6728, 037_S_6032, 068_S_4067, 100_S_6164, 123_S_0072, 129_S_6459, 135_S_4722, 141_S_6787, 301_S_6501, 005_S_6093, 011_S_4893, 020_S_5203, 027_S_5109, 032_S_6804, 037_S_6046, 068_S_4332, 100_S_6273, 123_S_0106, 129_S_6482, 135_S_4723, 153_S_6237, 301_S_6508, 005_S_6427, 011_S_6303, 020_S_6185, 027_S_5118, 032_S_6855, 037_S_6083, 068_S_4340, 100_S_6308, 123_S_0298, 129_S_6621, 135_S_5113, 153_S_6274, 301_S_6592, 006_S_0498, 011_S_6367, 020_S_6227, 027_S_5169, 033_S_0734, 037_S_6115, 068_S_4424, 100_S_6349, 123_S_1300, 129_S_6704, 135_S_6104, 153_S_6336, 301_S_6615, 006_S_0731, 011_S_6418, 020_S_6282, 027_S_5170, 033_S_1016, 037_S_6125, 068_S_4431, 100_S_6493, 123_S_4127, 129_S_6763, 135_S_6110, 153_S_6450, 301_S_6698, 006_S_4357, 011_S_6465, 020_S_6358, 027_S_5277, 033_S_1098, 037_S_6141, 070_S_4856, 100_S_6578, 123_S_4170, 129_S_6784, 135_S_6284, 153_S_6665, 301_S_6777]

def listfiles(folder, ext):
    for root, folders, files in os.walk(folder):
        for filename in files:
            if filename.lower().endswith(ext):
                yield os.path.join(root, filename)

basepath = "/data/mkp42/ADNI_data/ADNI"

# endpathL = "LLL_L_MPRAGE.txt"
# endpathR = "LLL_R_MPRAGE.txt"


rows = []

i = 0
for f in listfiles(basepath, "_l.txt"):
    if f.endswith("hipp_manseg_l.txt"):
        continue
    txt = open(f , "r")
    content = txt.read()
    txt.close()
    rows.append(f + " " + content + " ")
    i+= 1
print("first total", i)

i = 0
for f in listfiles(basepath, "_r.txt"):
    if f.endswith("hipp_manseg_r.txt"):
        continue
    txt = open(f , "r")
    content = txt.read()
    txt.close()
    rows[i] += f + " " + content
    i += 1
print("second total", i)
input()

for r in rows:
    r = r.replace('\n', '').replace("  ", ' ').split()
    print(r)
    with open("/data/mkp42/ADNI_data/ADNI/volumeLLL_ADNI.csv", 'a') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(r)