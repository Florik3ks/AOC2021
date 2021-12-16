
def solve(data):
    binary = get_bin_data(data)
    return decode_package(binary)[0]


def decode_package(binary):
    if len(binary) <= 7:
        return 0, ""
    version = int(binary[:3], 2)
    type_ = binary[3:6]
    if type_ == "100":
        package_data = ""
        for i in range(6, ((len(binary)) // 5) * 5, 5):
            start = binary[i]
            num_data = binary[i + 1: i+5]
            package_data += num_data
            b = binary[i + 5:]
            if start == '0':
                return int(package_data, 2), binary[i + 5:]
    else:
        mode = binary[6]
        values = []
        binary_snippet = ""
        if mode == '0':
            length = int(binary[7: 7 + 15], 2)
            binary_snippet = binary[7 + 15: 7 + 15 + length]
            binary_rest = binary[7 + 15 + length:]
            while len(binary_snippet) > 0:
                v, binary_snippet = decode_package(binary_snippet)
                values.append(v)
            binary_snippet += binary_rest
        elif mode == '1':
            number_of_packages = int(binary[7: 7 + 11], 2)
            binary_snippet = binary[7 + 11:]
            for i in range(number_of_packages):
                v, binary_snippet = decode_package(binary_snippet)
                values.append(v)

        type_ = int(type_, 2)
        if type_ == 0: return sum(values), binary_snippet
        elif type_ == 1:
            result = 1
            for v in values:
                result *= v
            return result, binary_snippet
        elif type_ == 2: return min(values), binary_snippet
        elif type_ == 3: return max(values), binary_snippet
        elif type_ == 5: return (1 if values[0] > values[1] else 0), binary_snippet
        elif type_ == 6: return (1 if values[0] < values[1] else 0), binary_snippet
        elif type_ == 7: return (1 if values[0] == values[1] else 0), binary_snippet
    return 0, binary


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
