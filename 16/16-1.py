
def solve(data):
    binary = get_bin_data(data)
    return decode_package(binary)[0]


def decode_package(binary):
    if len(binary) == 0:
        return 0, ""
    version = int(binary[:3], 2)
    versions = version
    type_ = binary[3:6]
    if type_ == "100":
        for i in range(6, ((len(binary)) // 5) * 5, 5):
            start = binary[i]
            b = binary[i + 5:]
            if start == '0':
                return version, b
    else:
        mode = binary[6]
        if mode == '0':
            length = int(binary[7: 7 + 15], 2)
            binary_snippet = binary[7 + 15: 7 + 15 + length]
            binary_rest = binary[7 + 15 + length:]
            while len(binary_snippet) > 0:
                v, binary_snippet = decode_package(binary_snippet)
                versions += v
            return versions, binary_snippet + binary_rest
        elif mode == '1':
            number_of_packages = int(binary[7: 7 + 11], 2)
            binary_snippet = binary[7 + 11:]
            for i in range(number_of_packages):
                v, binary_snippet = decode_package(binary_snippet)
                versions += v
            return versions, binary_snippet
    return versions, binary


def get_bin_data(data):
    result = ""
    for c in data.strip():
        binary = bin(int(c, 16))[2:].zfill(4)
        result += binary
    return result


if __name__ == "__main__":
    with open("16/input.txt", "r") as f:
        data = f.readlines()[0]
        print(solve(data))
